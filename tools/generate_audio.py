#!/usr/bin/env python3
"""Generate Transmutatio audio from docs/ELEVENLABS_PROMPTS_RU.md via ElevenLabs and save WAV.

Usage:
  python3 tools/generate_audio.py --list
  python3 tools/generate_audio.py --first            # first-listen set from the doc
  python3 tools/generate_audio.py merge_fire stone_birth
  python3 tools/generate_audio.py --all [--takes 2] [--skip-existing]

Key: uses ELEVENLABS_API_KEY if set, otherwise relies on a proxy that injects it.
Output: work/transmutatio/audio/incoming/<group>/<name>[_tN].wav
"""
import argparse, os, re, subprocess, sys, time, wave
import urllib.request, urllib.error, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(ROOT, "docs", "ELEVENLABS_PROMPTS_RU.md")
OUT = os.path.join(ROOT, "work", "transmutatio", "audio", "incoming")
FIRST = ["music_base_loop", "merge_fire", "merge_ice", "merge_poison", "merge_note_c5", "stone_birth"]
API = "https://api.elevenlabs.io/v1"

# Sound Effects API accepts at most 450 characters; these doc prompts are longer, so use trimmed versions.
SHORT = {
    "stone_birth": "One rare philosopher stone creation for a fantasy alchemy game. A compact inward pull of shimmering energy, a warm rising crystal resonance, then one luminous rounded impact around one second and a beautiful high crystal bloom in A minor, with a delicate two-second sparkling decay. Awe and warmth, controlled bass, smooth treble. No destructive blast, braam, choir, voices, coin shower or music.",
    "bonus_trigger": "Fantasy alchemy bonus activation stinger in A minor. A compact furnace ignition rises into a playful ascending celesta-and-dulcimer figure with light pizzicato strings and one soft frame-drum accent, ending on a bright suspended magical shimmer. Excited discovery, warm fire, controlled celebration. Clean short tail. No vocals, announcer, brass fanfare, EDM drop or coin rain.",
    "win_mega": "Four-and-a-half-second fantasy alchemy mega-win fanfare in A minor. Bright celesta and dulcimer play a rising two-part motif over lively pizzicato strings, warm bass and two light frame-drum accents, ending in a wide glowing crystal flourish. Fuller than a small win, rounded treble, controlled bass, clean decisive ending. No voice, choir, cinematic brass, rock drums or coin avalanche.",
    "win_epic": "Six-second fantasy alchemy epic-win fanfare in A minor, the discovery of a legendary philosopher stone. A short celesta-and-dulcimer buildup opens into soaring warm strings, bright crystal accents, rounded bass and tasteful frame drums. Main triumphant arrival near the middle, then a luminous final chord and clean sparkling decay. Grand yet whimsical, smooth treble. No voice, choir, braam, aggressive brass or coin avalanche.",
}


def group(name):
    if name.startswith("music_"): return "music"
    if name.startswith("amb_") and name != "amb_steam_hiss": return "ambience"
    if name.startswith("ui_"): return "ui"
    if name.startswith(("char_", "voice_")): return "characters"
    if name in ("amb_steam_hiss", "props_glass_clink"): return "optional"
    return "gameplay"


def parse():
    text = open(DOC, encoding="utf-8").read()
    items = []
    pat = re.compile(r"### \d+\. .+? — `(\w+)`\n\n\*\*(Music|Sound Effects) · запрос ([\d.]+) с.*?Looping: (ON|OFF).*?```text\n(.+?)\n```", re.S)
    for m in pat.finditer(text):
        name, kind, secs, loop, prompt = m.groups()
        g = "optional" if name in ("voice_aurelius_match", "voice_aurelius_cheer", "voice_aurelius_wonder", "char_aurelius_cloth") else group(name)
        items.append(dict(name=name, kind=kind, secs=float(secs), loop=loop == "ON", prompt=prompt.strip(), group=g))
    for i in items:
        if i["name"] in SHORT: i["prompt"] = SHORT[i["name"]]
    return items


def post(path, body, fmt):
    req = urllib.request.Request(f"{API}{path}?output_format={fmt}", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    key = os.environ.get("ELEVENLABS_API_KEY")
    if key: req.add_header("xi-api-key", key)
    with urllib.request.urlopen(req, timeout=600) as r:
        return r.read()


def call(item, fmt):
    if item["kind"] == "Music":
        body = dict(prompt=item["prompt"], music_length_ms=int(item["secs"] * 1000), force_instrumental=True)
        return post("/music", body, fmt)
    body = dict(text=item["prompt"], duration_seconds=item["secs"], prompt_influence=0.5)
    if item["loop"]: body["loop"] = True
    return post("/sound-generation", body, fmt)


def save_wav(item, take, takes):
    dest_dir = os.path.join(OUT, item["group"]); os.makedirs(dest_dir, exist_ok=True)
    stem = item["name"] + (f"_t{take}" if takes > 1 else "")
    wav_path = os.path.join(dest_dir, stem + ".wav")
    try:  # native PCM -> WAV (lossless, no re-encode)
        pcm = call(item, "pcm_44100")
        with wave.open(wav_path, "wb") as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(44100); w.writeframes(pcm)
        return wav_path
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:300]
        if e.code in (401, 403) and "output_format" not in detail and "tier" not in detail.lower():
            raise RuntimeError(f"HTTP {e.code}: {detail}")
        print(f"  pcm_44100 unavailable ({e.code}), falling back to MP3 -> WAV", file=sys.stderr)
    mp3_path = os.path.join(dest_dir, stem + ".mp3")
    open(mp3_path, "wb").write(call(item, "mp3_44100_192"))  # original MP3 kept
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3_path, wav_path], check=True)
    return wav_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="*"); ap.add_argument("--all", action="store_true")
    ap.add_argument("--first", action="store_true"); ap.add_argument("--list", action="store_true")
    ap.add_argument("--takes", type=int, default=1); ap.add_argument("--skip-existing", action="store_true")
    a = ap.parse_args()
    items = parse()
    if a.list:
        for i in items: print(f"{i['name']:26} {i['kind']:14} {i['secs']:>5}s loop={i['loop']} -> {i['group']}")
        return print(len(items), "prompts")
    sel = items if a.all else [i for i in items if i["name"] in (FIRST if a.first else a.names)]
    if not sel: sys.exit("nothing selected (use --list / --first / --all / names)")
    for i in sel:
        for t in range(1, a.takes + 1):
            stem = i["name"] + (f"_t{t}" if a.takes > 1 else "")
            if a.skip_existing and os.path.exists(os.path.join(OUT, i["group"], stem + ".wav")): continue
            print("generating", stem, flush=True)
            try: print("  saved", save_wav(i, t, a.takes))
            except Exception as e: sys.exit(f"  failed: {e}")
            time.sleep(0.5)


if __name__ == "__main__":
    main()
