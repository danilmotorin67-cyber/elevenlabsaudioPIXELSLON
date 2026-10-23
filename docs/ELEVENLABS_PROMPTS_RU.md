# Transmutatio — полный набор промптов для ElevenLabs

Версия 1.0 · 23 октября 2026 · Статус: промпты готовы, аудио ещё не сгенерировано.

44 самостоятельных промпта: 38 основных и 6 дополнительных. Из одной основной ноты позднее получим ещё 6 высот без отдельных генераций. Это перечень ассетов, а не обещание 44 попыток: удачные варианты выбираются на слух. Промпты ниже готовы к копированию целиком; все указания внутри них относятся к желаемому результату генерации.

## Какой звук создаём

Тёплая, загадочная и немного комичная алхимическая лаборатория. Чистая современная запись с характером пиксельного фэнтези: челеста, дульцимер, щипковые струны, стекло, дерево, латунь, мягкий огонь и жидкости. Музыка не должна утомлять в длинной сессии. Резкие высокие частоты и тяжёлые удары не нужны. Музыка без вокала; голоса алхимика вынесены в необязательную группу.

## Как работать в ElevenLabs

1. Музыку создавай в **Music**, остальные файлы — в **Sound Effects**. Для музыки явно оставляем `Instrumental only`; если есть отдельный переключатель инструментала, включи его. [Music: официальное руководство](https://elevenlabs.io/docs/overview/capabilities/music/best-practices).
2. Копируй английский блок целиком. Русские пояснения и имена файлов не надо вставлять в поле промпта. Длительность задавай отдельным параметром; для SFX включай Looping только у строк с «Да». [Sound Effects: официальное руководство](https://elevenlabs.io/docs/overview/capabilities/sound-effects).
3. В таблице указаны отдельно длительность генерации и желаемая длина готового файла. Короткие клики запрашиваем по 0,5 с и позднее обрезаем. В официальном API SFX описан диапазон 0,5–30 с; интерфейс и отдельные модели могут иметь другие ограничения. [Параметры SFX](https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert).
4. Музыкальные петли запрашиваются текстом: 32 такта при 96 BPM ≈ 80 с для базы, при 128 BPM ≈ 60 с для бонуса. Бесшовность, реальную тональность и точную длину проверим после генерации; один промпт их не гарантирует. Не делай fade-in/fade-out у петель.
5. Начни с музыки базы и трёх эффектов слияния. Достаточно сначала получить 1–2 кандидата каждого. После выбора характера звука делай остальные; для часто повторяющегося приземления полезны 2–3 дубля.
6. Скачивай исходный файл в лучшем доступном качестве. Предпочтителен WAV, если он доступен; если доступен MP3 — сохраняй оригинальный MP3, не перекодируй его ради расширения WAV. Имена ниже — без расширения: например `merge_fire.wav` или `merge_fire.mp3`.
7. Сохраняй свои файлы в `work/transmutatio/audio/incoming/` в подпапки `music`, `ambience`, `ui`, `gameplay`, `characters`, `optional`. Редактуру, выравнивание громкости, петли и версии для турбо сделаем после выбора исходников.

## Очерёдность генерации

- Первая прослушка: `music_base_loop`, `merge_fire`, `merge_ice`, `merge_poison`, `merge_note_c5`, `stone_birth`.
- После утверждения стиля: музыка бонуса, поле, UI, бонусные и выигрышные акценты.
- Затем атмосфера и персонажи, последними — шесть необязательных деталей.

## Перечень

| Файл без расширения | Назначение | Раздел ElevenLabs | Запрос, с | Готовый, с | Петля | Приоритет |
|---|---|---|---:|---:|---|---|
| music_base_loop | Основная музыка лаборатории | Music | 80 | 80 | Да | Основной |
| music_bonus_loop | Музыка бесплатных вращений | Music | 60 | 60 | Да | Основной |
| amb_lab_room_loop | Тихая комната лаборатории | Sound Effects | 20 | 20 | Да | Основной |
| amb_furnace_loop | Огонь в печи | Sound Effects | 12 | 12 | Да | Основной |
| amb_flasks_bubble_loop | Тихое кипение колб | Sound Effects | 10 | 10 | Да | Основной |
| ui_click | Нажатие кнопки | Sound Effects | 0.5 | 0.15 | Нет | Основной |
| ui_toggle_on | Включение переключателя | Sound Effects | 0.5 | 0.22 | Нет | Основной |
| ui_toggle_off | Выключение переключателя | Sound Effects | 0.5 | 0.22 | Нет | Основной |
| ui_panel_open | Открытие панели | Sound Effects | 0.6 | 0.3 | Нет | Основной |
| ui_panel_close | Закрытие панели | Sound Effects | 0.6 | 0.28 | Нет | Основной |
| ui_unavailable | Действие недоступно | Sound Effects | 0.5 | 0.25 | Нет | Основной |
| grid_spin_start | Запуск вращения поля | Sound Effects | 0.8 | 0.55 | Нет | Основной |
| symbol_land_light | Лёгкая посадка символов | Sound Effects | 0.5 | 0.16 | Нет | Основной |
| symbol_land_heavy | Посадка тяжёлого символа | Sound Effects | 0.5 | 0.2 | Нет | Основной |
| symbol_wild_appear | Появление wild — алкахеста | Sound Effects | 0.9 | 0.65 | Нет | Основной |
| symbol_scatter_land | Посадка печи scatter | Sound Effects | 0.9 | 0.6 | Нет | Основной |
| merge_fire | Огненная линия слияния | Sound Effects | 1.2 | 0.8 | Нет | Основной |
| merge_ice | Морозная линия слияния | Sound Effects | 1.2 | 0.8 | Нет | Основной |
| merge_poison | Ядовитая линия слияния | Sound Effects | 1.2 | 0.8 | Нет | Основной |
| merge_note_c5 | Исходная нота слияния C5 | Sound Effects | 0.6 | 0.35 | Нет | Основной |
| cascade_chain_accent | Акцент длинной цепочки | Sound Effects | 1 | 0.7 | Нет | Основной |
| multiplier_step | Повышение множителя | Sound Effects | 0.6 | 0.3 | Нет | Основной |
| stone_birth | Рождение философского камня | Sound Effects | 3 | 3 | Нет | Основной |
| stone_pulse | Однократный импульс камня | Sound Effects | 0.9 | 0.65 | Нет | Основной |
| stone_dissolve | Растворение старого камня | Sound Effects | 0.8 | 0.55 | Нет | Основной |
| bonus_trigger | Запуск бесплатных вращений | Sound Effects | 3.5 | 3.5 | Нет | Основной |
| bonus_extra_spins | Дополнительные вращения | Sound Effects | 1.6 | 1.2 | Нет | Основной |
| bonus_summary | Завершение бонуса | Sound Effects | 3 | 3 | Нет | Основной |
| win_small | Обычный выигрыш | Sound Effects | 1 | 0.75 | Нет | Основной |
| win_big | BIG WIN | Sound Effects | 3 | 3 | Нет | Основной |
| win_mega | MEGA WIN | Sound Effects | 4.5 | 4.5 | Нет | Основной |
| win_epic | EPIC WIN / максимальный выигрыш | Sound Effects | 6 | 6 | Нет | Основной |
| win_count_loop | Петля подсчёта суммы | Sound Effects | 2 | 2 | Да | Основной |
| win_count_finish | Окончание подсчёта | Sound Effects | 0.7 | 0.45 | Нет | Основной |
| char_aurelius_stir | Алхимик смешивает реагент | Sound Effects | 1 | 0.75 | Нет | Основной |
| char_aurelius_boom | Комичный пых эксперимента | Sound Effects | 0.9 | 0.65 | Нет | Основной |
| char_salamander_jump | Прыжок саламандры | Sound Effects | 0.8 | 0.6 | Нет | Основной |
| char_salamander_chirp | Огненный писк саламандры | Sound Effects | 0.7 | 0.45 | Нет | Основной |
| voice_aurelius_match | Алхимик: довольное хмыканье | Sound Effects | 0.8 | 0.5 | Нет | Доп. |
| voice_aurelius_cheer | Алхимик: короткий смешок | Sound Effects | 1 | 0.65 | Нет | Доп. |
| voice_aurelius_wonder | Алхимик: удивлённый вдох | Sound Effects | 0.8 | 0.55 | Нет | Доп. |
| char_aurelius_cloth | Движение мантии алхимика | Sound Effects | 0.6 | 0.3 | Нет | Доп. |
| amb_steam_hiss | Короткий выход пара | Sound Effects | 1.2 | 0.8 | Нет | Доп. |
| props_glass_clink | Лёгкий звон стекла на столе | Sound Effects | 0.7 | 0.4 | Нет | Доп. |

## Музыка

### 01. Основная музыка лаборатории — `music_base_loop`

**Music · запрос 80 с · целевой готовый файл 80 с · Looping: ON · основной.**

Событие: basegame, ожидание и обычные вращения.

```text
Instrumental only. A seamless 32-bar fantasy game background loop at 96 BPM, 4/4, in A minor. A candlelit alchemist workshop at midnight: curious, warm, gently mischievous, with a sense of discovery. Intimate celesta, softly plucked dulcimer, pizzicato strings, muted viola, a rounded bass pulse, delicate wooden percussion and restrained 16-bit arpeggio accents. A memorable but sparse four-note motif, small variations every eight bars, steady low-to-medium energy. Modern clean game soundtrack production with a subtle retro character, soft treble and room for foreground sound effects. Begin inside the groove and end on a turnaround that leads naturally back to bar one. No intro, final cadence, fade-in or fade-out. No vocals, choir, speech, environmental sounds, heavy drums or harsh bitcrushing.
```

Первый кандидат для утверждения общего стиля. Цель 80 с = 32 такта при 96 BPM. Это запрос к генератору; точный темп и стык проверим по готовому файлу.

### 02. Музыка бесплатных вращений — `music_bonus_loop`

**Music · запрос 60 с · целевой готовый файл 60 с · Looping: ON · основной.**

Событие: enterBonus → freeSpinEnd.

```text
Instrumental only. A seamless 32-bar fantasy game bonus loop at 128 BPM, 4/4, in A minor. A magical alchemist furnace has awakened: playful momentum, excited discovery and controlled energy. Celesta and plucked dulcimer carry a concise four-note motif, supported by brisk pizzicato strings, light frame drums, warm rounded bass and restrained 16-bit arpeggios. Keep the intimate chamber-game palette; make it brighter and more rhythmically active than a quiet laboratory theme. Short variations every eight bars, stable intensity, clear space for magical impacts and reward sounds. Clean modern production, rounded transients, soft treble. Start in the groove and end with a turnaround back to bar one. No intro, final cadence, fade-in or fade-out. No vocals, choir, speech, environmental sounds, EDM drop or aggressive brass.
```

После утверждения базы можно приложить свой короткий фрагмент базы как Audio Reference, если эта функция доступна. Одинаковый текст сам по себе не гарантирует общую мелодию. Цель 60 с = 32 такта при 128 BPM.

## Атмосфера

### 03. Тихая комната лаборатории — `amb_lab_room_loop`

**Sound Effects · запрос 20 с · целевой готовый файл 20 с · Looping: ON · основной.**

Событие: постоянный тихий фон сцены.

```text
Seamless ambient loop of a small stone alchemist workshop at night. A very soft enclosed-room air tone, faint distant wind filtered through a closed window, and an occasional subtle wooden settling creak. Intimate, still and comfortable, with a light mysterious character. Consistent quiet level, no obvious beginning or ending. No fire, bubbling, voices, footsteps, music, thunder or prominent events.
```

Очень тихий слой. Печь и колбы находятся в отдельных файлах; не смешивать их в этот фон.

### 04. Огонь в печи — `amb_furnace_loop`

**Sound Effects · запрос 12 с · целевой готовый файл 12 с · Looping: ON · основной.**

Событие: печь в базе и бонусе.

```text
Seamless loop of a small steady fire inside a compact brick alchemist furnace. Soft rounded crackles, gentle ember ticks and a warm contained airflow. Close, cozy and controlled rather than a large bonfire. Even texture with no major pops or level changes, no opening ignition and no ending. Isolated fire only, no voices, music, outdoor ambience or bellows pumping.
```

Один файл для обоих режимов; в бонусе меняется громкость, отдельная генерация не нужна.

### 05. Тихое кипение колб — `amb_flasks_bubble_loop`

**Sound Effects · запрос 10 с · целевой готовый файл 10 с · Looping: ON · основной.**

Событие: редкие периоды кипения, видимые колбы.

```text
Seamless close-up loop of a small glass laboratory flask gently simmering. Tiny liquid bubbles, occasional delicate plips and a soft watery gurgle, light and intimate with restrained low frequencies. A steady texture without a distinct beginning or ending. Isolated bubbling only, no glass breaking, pouring, music, voices, fire or room ambience.
```

Включать негромко и с паузами; не озвучивать каждую анимационную петлю заново.

## Интерфейс

### 06. Нажатие кнопки — `ui_click`

**Sound Effects · запрос 0.5 с · целевой готовый файл 0.15 с · Looping: OFF · основной.**

Событие: обычные кнопки, изменение ставки, подтверждение.

```text
One short tactile press of a small brass-and-wood game button. A soft wooden tick with a tiny rounded metallic accent, crisp but gentle, close and dry. One event at the start, a very brief natural decay, then silence. Polished fantasy game interface sound. No additional clicks, musical phrase, voices or background ambience.
```

Переиспользовать для основных нажатий; наведение мыши оставляем без звука.

### 07. Включение переключателя — `ui_toggle_on`

**Sound Effects · запрос 0.5 с · целевой готовый файл 0.22 с · Looping: OFF · основной.**

Событие: auto/turbo и другие переключатели: включение.

```text
One tiny brass toggle switching on, followed immediately by a soft upward two-note glass confirmation. Light, warm, concise and dry, designed for a fantasy laboratory game interface. A single short action at the beginning with a clean decay. No repeated toggles, voices, melody or background noise.
```

При включении звука эффект разрешён только после восстановления громкости; при mute не проигрывать его через отключённый канал.

### 08. Выключение переключателя — `ui_toggle_off`

**Sound Effects · запрос 0.5 с · целевой готовый файл 0.22 с · Looping: OFF · основной.**

Событие: auto/turbo и другие переключатели: выключение.

```text
One tiny brass toggle switching off, followed immediately by a soft downward two-note glass confirmation. Gentle, neutral, concise and dry, designed for a fantasy laboratory game interface. A single short action at the beginning with a clean decay. No repeated toggles, failure buzzer, voices or background noise.
```

### 09. Открытие панели — `ui_panel_open`

**Sound Effects · запрос 0.6 с · целевой готовый файл 0.3 с · Looping: OFF · основной.**

Событие: правила, настройки, выбор ставки, окно покупки бонуса.

```text
One short opening movement of a parchment-and-brass interface panel. A light paper brush blended with a soft upward airy swish, ending in one delicate wooden stop. Compact and tactile, close and dry, understated fantasy game sound design. No magical explosion, speech, music or extra actions.
```

### 10. Закрытие панели — `ui_panel_close`

**Sound Effects · запрос 0.6 с · целевой готовый файл 0.28 с · Looping: OFF · основной.**

Событие: закрытие диалога или панели.

```text
One short closing movement of a parchment-and-brass interface panel. A gentle downward air swish with a small paper brush and a soft wooden stop. Compact, tactile and dry, quieter than an opening effect. One action only, no music, voices or dramatic impact.
```

### 11. Действие недоступно — `ui_unavailable`

**Sound Effects · запрос 0.5 с · целевой готовый файл 0.25 с · Looping: OFF · основной.**

Событие: непринятое действие или ошибка ввода.

```text
One restrained fantasy interface rejection sound: two muted hollow wooden taps falling slightly in pitch. Soft, brief, neutral and informative, never alarming. Close dry recording, clean ending. No harsh buzzer, siren, speech, music or repeated sequence.
```

Только на реальное отклонение действия. При сетевом ожидании не повторять циклически.

## Поле и символы

### 12. Запуск вращения поля — `grid_spin_start`

**Sound Effects · запрос 0.8 с · целевой готовый файл 0.55 с · Looping: OFF · основной.**

Событие: нажатие SPIN и начало reveal.

```text
One compact magical board activation: a small brass lever click immediately followed by a smooth airy upward sweep and a faint glass shimmer. The movement feels light and quick, suited to a six-column alchemy puzzle board. Clear attack, gently fading tail, close game sound design. No mechanical reel rattling, coin cascade, voice or music.
```

На SPIN этот звук заменяет ui_click, чтобы не было двойного нажатия.

### 13. Лёгкая посадка символов — `symbol_land_light`

**Sound Effects · запрос 0.5 с · целевой готовый файл 0.16 с · Looping: OFF · основной.**

Событие: посадка кувшинов/колб при reveal и tumbleBoard.

```text
One small rounded glass-and-ceramic token landing on a padded wooden surface. A light tactile clink with a soft low tap underneath, intact glass, warm and dry, very short decay. Designed for frequent repetition in a fantasy game. One landing only, no bounce sequence, shatter, music or ambience.
```

Достаточно 2–3 удачных дублей. Звук на небольшую пачку падающих символов, а не на все 30 клеток одновременно.

### 14. Посадка тяжёлого символа — `symbol_land_heavy`

**Sound Effects · запрос 0.5 с · целевой готовый файл 0.2 с · Looping: OFF · основной.**

Событие: посадка кристалла/золота/камня.

```text
One compact precious-metal token landing on a padded wooden surface. A warm low wooden knock with a tiny rounded brass ring, weighty but small and friendly. Close, dry and brief, with no booming bass. One landing only, no metallic scraping, coin shower, music or room ambience.
```

Для тяжёлых символов; само рождение камня озвучивается отдельно.

### 15. Появление wild — алкахеста — `symbol_wild_appear`

**Sound Effects · запрос 0.9 с · целевой готовый файл 0.65 с · Looping: OFF · основной.**

Событие: новый ALKAHEST в reveal/newSymbols.

```text
One magical solvent droplet appearing: a soft liquid plop opens into a brief prismatic glass shimmer, with a gently bending high tone and two tiny bubbles. Curious, fluid and bright, restrained fantasy game effect. Immediate attack, smooth clean tail. No splash storm, voice, music or background ambience.
```

Только для действительно нового wild, с ограничением частоты, не на каждое idle-мерцание.

### 16. Посадка печи scatter — `symbol_scatter_land`

**Sound Effects · запрос 0.9 с · целевой готовый файл 0.6 с · Looping: OFF · основной.**

Событие: новый FURNACE при reveal/newSymbols.

```text
One miniature alchemist furnace settling onto the board: a small warm iron-and-ceramic knock, a brief contained puff of flame, and a low rounded brass ping. Compact, tactile and magical, not explosive. One distinct event with a short clean decay. No jackpot fanfare, voice, music or continuing fire ambience.
```

Один исходник. Вторую печь можно чуть поднять по тону; запуск бонуса — только по freeSpinTrigger, без ложной фанфары.

## Слияния и каскады

### 17. Огненная линия слияния — `merge_fire`

**Sound Effects · запрос 1.2 с · целевой готовый файл 0.8 с · Looping: OFF · основной.**

Событие: mergeGroups: T3 IRON, T4 COPPER, T7 GOLD.

```text
A single controlled thread of magical fire travels across a short chain of symbols, beginning with a soft ignition, building into a smooth spreading flame whoosh, then gathering into one small warm puff. Delicate ember crackles, compact scale, clean transient, softened treble. Unpitched foreground game effect with a short natural tail. No explosion, musical chime, voice or background ambience.
```

Шумовой слой под восходящую ноту. Проход звучит один раз на волну; не на каждую клетку.

### 18. Морозная линия слияния — `merge_ice`

**Sound Effects · запрос 1.2 с · целевой готовый файл 0.8 с · Looping: OFF · основной.**

Событие: mergeGroups: T2 TIN, T6 SILVER.

```text
A single ribbon of magical frost spreads across a short chain of symbols. Soft icy air sweeps forward as tiny crystalline grains form in sequence, then converge into one delicate brittle tick. Cool, smooth and sparkling with rounded high frequencies, compact fantasy game scale. Short clean tail, mostly unpitched texture. No shattering glass, musical phrase, voice or background ambience.
```

### 19. Ядовитая линия слияния — `merge_poison`

**Sound Effects · запрос 1.2 с · целевой готовый файл 0.8 с · Looping: OFF · основной.**

Событие: mergeGroups: T1 LEAD, T5 MERCURY.

```text
A single thin trail of enchanted green vapor flows across a short chain of symbols. A soft wet airy sweep, a few tiny viscous bubbles, then one gentle liquid pop as the energy gathers. Mischievous and alchemical rather than disgusting, smooth and compact, close game sound design. Mostly unpitched with a short clean tail. No coughing, musical phrase, voice or room ambience.
```

### 20. Исходная нота слияния C5 — `merge_note_c5`

**Sound Effects · запрос 0.6 с · целевой готовый файл 0.35 с · Looping: OFF · основной.**

Событие: появление результата слияния; источник шкалы T1–T7.

```text
One isolated pitched magical glass-pluck note at middle-high C, C5, approximately 523 Hz. A rounded celesta-like attack blended with a delicate crystal ping, warm soft fundamental, restrained shimmering overtones. One note only, immediate attack, short smooth decay, dry and clean. A reusable fantasy game reward tone. No arpeggio, chord, second note, whoosh, voice, background noise or music bed.
```

Это единственный исходник для семи высот. Проверим фактическую ноту и получим остальные сдвигом высоты; генератор не гарантирует точные 523 Hz.

### 21. Акцент длинной цепочки — `cascade_chain_accent`

**Sound Effects · запрос 1 с · целевой готовый файл 0.7 с · Looping: OFF · основной.**

Событие: редкий акцент при длинной последовательности mergeGroups.

```text
One very short fantasy alchemy chain-success accent in A minor pentatonic: three soft ascending celesta plucks, C, E, A, ending with a delicate glass sparkle. Playful momentum and discovery, intimate scale, rounded attacks, compact decay. No drum hit, orchestral fanfare, coin rain, voice or background music.
```

Декоративный акцент, например после третьего шага каскада; максимум один раз за длинную цепочку. Не дублировать им каждое слияние.

### 22. Повышение множителя — `multiplier_step`

**Sound Effects · запрос 0.6 с · целевой готовый файл 0.3 с · Looping: OFF · основной.**

Событие: reactionMultiplier с reason=mergeStep и ростом value.

```text
One small alchemical gauge stepping upward: a crisp brass detent tick followed by a tiny rising glass chirp. Very short, precise and satisfying, dry and close, softened treble. The sound marks one increment rather than a major prize. No repeated ratchet, melody, voice, music or background ambience.
```

Не звучит при spinStart и сбросе шкалы; при нескольких шагах из-за камня — один сдержанный акцент.

## Философский камень

### 23. Рождение философского камня — `stone_birth`

**Sound Effects · запрос 3 с · целевой готовый файл 3 с · Looping: OFF · основной.**

Событие: stoneCreated: начало отдельной сцены.

```text
One rare philosopher stone creation for a fantasy alchemy game. Start immediately with a compact inward pull of shimmering energy, build a warm rising crystal resonance, then release into one luminous rounded impact and a beautiful high crystal bloom in A minor. The main reveal lands around one second, followed by a delicate two-second sparkling decay. Awe, discovery and warmth, with controlled bass and smooth treble. No destructive blast, trailer braam, choir, voices, coin shower or background music.
```

Самый узнаваемый эффект. Если одновременно несколько камней — один главный звук рождения, остальные тихие акценты. Для турбо позже сделаем короткую редакцию около 1 с.

### 24. Однократный импульс камня — `stone_pulse`

**Sound Effects · запрос 0.9 с · целевой готовый файл 0.65 с · Looping: OFF · основной.**

Событие: редкий видимый акцент уже существующего камня.

```text
One gentle pulse from a glowing philosopher stone. A warm rounded crystal resonance swells briefly, releases a few soft sparkling overtones, then fades cleanly. Quiet, intimate and precious, lightly centered on A, without deep rumble or piercing ringing. One pulse only, no rhythm, voices, melody or background ambience.
```

Декоративный эффект, не новая выплата. Не запускать постоянно на каждом idle-кадре; можно оставить выключенным по умолчанию.

### 25. Растворение старого камня — `stone_dissolve`

**Sound Effects · запрос 0.8 с · целевой готовый файл 0.55 с · Looping: OFF · основной.**

Событие: удаление камня перед новым reveal.

```text
One small enchanted crystal dissolving gently into fine dust. A soft descending airy shimmer with tiny delicate particles fading into silence, calm and graceful. Compact fantasy game effect, close and clean, rounded high frequencies. No hard break, sad sting, explosion, voice, musical phrase or background ambience.
```

Только если растворение показано визуально. При обычной быстрой смене поля достаточно grid_spin_start.

## Бонус

### 26. Запуск бесплатных вращений — `bonus_trigger`

**Sound Effects · запрос 3.5 с · целевой готовый файл 3.5 с · Looping: OFF · основной.**

Событие: freeSpinTrigger и переход enterBonus.

```text
One fantasy alchemy bonus activation stinger in A minor. A compact furnace ignition rises into a playful ascending celesta-and-dulcimer figure, supported by light pizzicato strings and one soft frame-drum accent. End on a bright suspended magical shimmer that can lead into an energetic background loop. Excited discovery, warm fire and controlled celebration. Immediate start, one clear reveal, clean short tail. No vocals, announcer, brass fanfare, EDM drop or coin rain.
```

Одинаково подходит бонусу от scatter и покупке. freeSpinTrigger + enterBonus не должны запускать его дважды.

### 27. Дополнительные вращения — `bonus_extra_spins`

**Sound Effects · запрос 1.6 с · целевой готовый файл 1.2 с · Looping: OFF · основной.**

Событие: freeSpinRetrigger с addedFs=4.

```text
One concise extra-turn reward in a magical alchemy game. A quick warm flame flick, followed by a bright upward three-note celesta figure in A minor pentatonic and a tiny glass sparkle. Cheerful and light, clearly smaller than a full bonus entrance. Immediate attack, clean short decay. No voice, spoken numbers, orchestral fanfare or background music.
```

### 28. Завершение бонуса — `bonus_summary`

**Sound Effects · запрос 3 с · целевой готовый файл 3 с · Looping: OFF · основной.**

Событие: freeSpinEnd: итоговая панель.

```text
One gentle completion stinger for a fantasy alchemy bonus round in A minor. A short descending dulcimer answer resolves into a warm celesta-and-pizzicato chord with a delicate crystal tail. Satisfied, calm and lightly whimsical, designed to return smoothly to a quiet laboratory theme. Modest celebration with a clean ending. No grand fanfare, voice, spoken amount, coin shower or background ambience.
```

Если одновременно открывается BIG/MEGA/EPIC, звучит выбранная фанфара выигрыша, а этот стингер пропускается.

## Выигрыши

### 29. Обычный выигрыш — `win_small`

**Sound Effects · запрос 1 с · целевой готовый файл 0.75 с · Looping: OFF · основной.**

Событие: finalWin.amount > 0 без крупной плашки.

```text
One modest fantasy game win confirmation in A minor pentatonic. Two warm celesta plucks rise into a tiny glass sparkle, light, pleasant and concise. Intimate scale, dry clear attack and a soft short decay. A small successful result, not a jackpot. No cheering, voice, coin rain, drums or background music.
```

При нулевой выплате тишина. Не играть заново за каждое обновление счётчика setTotalWin.

### 30. BIG WIN — `win_big`

**Sound Effects · запрос 3 с · целевой готовый файл 3 с · Looping: OFF · основной.**

Событие: открытие плашки BIG WIN.

```text
One three-second fantasy alchemy big-win fanfare in A minor. A bright rising celesta motif with plucked dulcimer, lively pizzicato strings and one rounded frame-drum accent resolves into a warm magical crystal flourish. Confident, playful and celebratory, clean modern game production with room for a visible number count. One compact musical gesture with a clean tail. No voice, choir, brass blast, EDM drop or coin avalanche.
```

Точные пороги BIG/MEGA/EPIC определим в клиенте; звук не должен зависеть от валюты.

### 31. MEGA WIN — `win_mega`

**Sound Effects · запрос 4.5 с · целевой готовый файл 4.5 с · Looping: OFF · основной.**

Событие: открытие плашки MEGA WIN.

```text
One four-and-a-half-second fantasy alchemy mega-win fanfare in A minor. Bright celesta and dulcimer play a rising two-part motif over lively pizzicato strings, warm bass and two light frame-drum accents. A wider glowing crystal flourish provides the payoff. More energetic and fuller than a small chamber-game reward, while keeping rounded treble and controlled bass. Clean decisive ending. No voice, choir, cinematic brass, rock drums or coin avalanche.
```

### 32. EPIC WIN / максимальный выигрыш — `win_epic`

**Sound Effects · запрос 6 с · целевой готовый файл 6 с · Looping: OFF · основной.**

Событие: открытие EPIC WIN или wincap.

```text
One six-second fantasy alchemy epic-win fanfare in A minor, the discovery of a legendary philosopher stone. A brief ascending celesta-and-dulcimer buildup opens into soaring warm strings, bright magical crystal accents, rounded bass and tasteful frame drums. A clear two-stage celebration with its main triumphant arrival near the middle, then a luminous final chord and clean sparkling decay. Grand within an intimate whimsical fantasy palette, smooth treble and controlled dynamics. No voice, choir, trailer braam, aggressive brass or coin avalanche.
```

Для wincap переиспользуем этот файл. Он заменяет меньшие фанфары и не накладывается на все предыдущие уровни.

### 33. Петля подсчёта суммы — `win_count_loop`

**Sound Effects · запрос 2 с · целевой готовый файл 2 с · Looping: ON · основной.**

Событие: анимированный подсчёт крупного выигрыша.

```text
A seamless two-second loop of soft evenly spaced tiny glass and brass ticks for a fantasy game number counter, about eight rounded ticks per second. Delicate, precise and lightly sparkling, consistent level, no melody or changing pitch. Quiet supportive texture with no obvious first or last tick. No loose coins, cash register, voice, background music or crescendo.
```

Звучит лишь пока растёт число. После пропуска анимации немедленно остановить; на обычных мелких числах можно не использовать.

### 34. Окончание подсчёта — `win_count_finish`

**Sound Effects · запрос 0.7 с · целевой готовый файл 0.45 с · Looping: OFF · основной.**

Событие: счётчик дошёл до фактической суммы.

```text
One soft final fantasy number-counter confirmation. A tiny tactile brass tick blooms into a single warm glass chime centered on A, with a short gentle decay. Clear but understated, close and clean. One event only, no arpeggio, second hit, coin shower, voice or background music.
```

## Персонажи

### 35. Алхимик смешивает реагент — `char_aurelius_stir`

**Sound Effects · запрос 1 с · целевой готовый файл 0.75 с · Looping: OFF · основной.**

Событие: видимое действие stir.

```text
One brief close-up stirring gesture in a small ceramic alchemist bowl. Two soft circular scrapes of a wooden spoon, a tiny liquid swirl and one delicate spoon tap at the end. Warm, tactile, restrained and slightly whimsical, dry recording. No voice, bubbling background, music, repeated long stirring or breaking glass.
```

Запускать на показанное движение, с большими паузами; не каждые 0,6 с циклической анимации.

### 36. Комичный пых эксперимента — `char_aurelius_boom`

**Sound Effects · запрос 0.9 с · целевой готовый файл 0.65 с · Looping: OFF · основной.**

Событие: видимое действие boom / fx_explosion.

```text
One small comic alchemy experiment puff. A cork-like soft pop opens into a short fluffy burst of air, followed by two tiny falling dust ticks. Friendly surprise, compact and light, no heavy bass, no destruction. One event with a clean ending. No coughing, voice, glass shatter, gunshot, music or room ambience.
```

Это небольшой пых возле алхимика; не заменяет эффект рождения камня.

### 37. Прыжок саламандры — `char_salamander_jump`

**Sound Effects · запрос 0.8 с · целевой готовый файл 0.6 с · Looping: OFF · основной.**

Событие: char_salamander_jump: прыжок и приземление.

```text
One tiny fire salamander hopping. A soft quick airy flick at takeoff, a brief delicate ember sparkle in flight, then a light padded two-foot tap on landing. Small, agile and playful, compact fantasy creature foley, close and clean. No voice, squeak, cartoon boing, large fire burst, music or ambience.
```

### 38. Огненный писк саламандры — `char_salamander_chirp`

**Sound Effects · запрос 0.7 с · целевой готовый файл 0.45 с · Looping: OFF · основной.**

Событие: редкая самостоятельная реакция саламандры.

```text
One tiny fantasy fire salamander chirp: a short warm breathy creature trill blended with a delicate ember crackle. Cute but not babyish, animal-like and lightly raspy, small scale with rounded treble. One concise call, isolated and dry. No human words, laughter, bird flock, dog bark, melody, music or background ambience.
```

Редко, отдельно от прыжка; не наслаивать с голосом алхимика.

## Дополнительно

### 39. Алхимик: довольное хмыканье — `voice_aurelius_match`

**Sound Effects · запрос 0.8 с · целевой готовый файл 0.5 с · Looping: OFF · дополнительно.**

Событие: необязательная реакция match.

```text
One brief nonverbal satisfied hum from a warm elderly male fantasy alchemist, a low gentle hm of pleased discovery. Slightly gravelly and expressive but friendly, understated comic character acting, close dry recording. A single natural vocal gesture. No words, sentence, singing, laughter, other people, music or ambience.
```

Необязательная озвучка. Голос в Sound Effects может отличаться между генерациями; утверждать единый тембр, иначе оставить реакции без голоса.

### 40. Алхимик: короткий смешок — `voice_aurelius_cheer`

**Sound Effects · запрос 1 с · целевой готовый файл 0.65 с · Looping: OFF · дополнительно.**

Событие: необязательная редкая реакция cheer.

```text
One short quiet delighted chuckle from a warm elderly male fantasy alchemist. A low slightly gravelly two-breath chuckle of successful discovery, intimate, friendly and understated, not a loud comedy laugh. Close dry character recording, one reaction only. No spoken words, singing, other people, applause, music or ambience.
```

Должен совпасть с тембром довольного хмыканья; не запускать на каждый выигрыш.

### 41. Алхимик: удивлённый вдох — `voice_aurelius_wonder`

**Sound Effects · запрос 0.8 с · целевой готовый файл 0.55 с · Looping: OFF · дополнительно.**

Событие: необязательная реакция wonder на камень.

```text
One brief breath of amazed discovery from a warm elderly male fantasy alchemist: a soft surprised inhale opening into a quiet breathy gasp, low register, slightly gravelly and friendly. Understated awe, close dry recording. One nonverbal reaction only. No word, sentence, scream, singing, other people, music or ambience.
```

Не перекрывать главный эффект stone_birth. Только если удастся сохранить тот же голос.

### 42. Движение мантии алхимика — `char_aurelius_cloth`

**Sound Effects · запрос 0.6 с · целевой готовый файл 0.3 с · Looping: OFF · дополнительно.**

Событие: необязательный жест match/chain/cheer.

```text
One short close-up movement of a soft heavy wool sleeve. A gentle fabric brush and a small cloth fold settling, warm and dry, intimate fantasy character foley, very restrained. One motion only. No footsteps, jewelry, voices, music or room ambience.
```

Переиспользуется для жестов. Idle остаётся тихим.

### 43. Короткий выход пара — `amb_steam_hiss`

**Sound Effects · запрос 1.2 с · целевой готовый файл 0.8 с · Looping: OFF · дополнительно.**

Событие: видимый разовый пар из перегонного аппарата.

```text
One small controlled release of steam from a glass-and-brass alchemy apparatus. A soft rounded hiss swells briefly and fades smoothly, light and airy with softened high frequencies. Close, compact and quiet, one puff only. No pressure explosion, whistle, bubbling, music, voice or background ambience.
```

Декоративно, с паузами. Не зацикливать на каждый проход спрайтового пара.

### 44. Лёгкий звон стекла на столе — `props_glass_clink`

**Sound Effects · запрос 0.7 с · целевой готовый файл 0.4 с · Looping: OFF · дополнительно.**

Событие: редкий видимый контакт колб/посуды.

```text
One delicate contact between two small intact laboratory glass vials. A soft high glass tick with a tiny warm wooden tabletop tap, clean, dry and brief. Restrained close-up fantasy workshop foley. One contact only, no shattering, long ringing, repeated clinks, voices, music or room ambience.
```

Использовать только при подходящем действии; статичные весы и колбы постоянно не звенят.

## Семь ступеней звука слияния — без семи разных генераций

Сначала выбираем `merge_note_c5`, проверяем фактическую высоту и приводим её к C5. Затем делаем копии с указанным сдвигом, сохраняя характер и длину. Одна и та же нота на всём ряду создаёт ощущение общей системы. Все ноты входят в A minor pentatonic. Генерировать их по отдельности не требуется; это последующая обработка.

| Исходный уровень группы | Результат | Файл | Нота | Сдвиг от C5 |
|---|---|---|---|---:|
| T1 LEAD | T2 TIN | merge_note_t1 | C5 | 0 полутонов |
| T2 TIN | T3 IRON | merge_note_t2 | D5 | +2 |
| T3 IRON | T4 COPPER | merge_note_t3 | E5 | +4 |
| T4 COPPER | T5 MERCURY | merge_note_t4 | G5 | +7 |
| T5 MERCURY | T6 SILVER | merge_note_t5 | A5 | +9 |
| T6 SILVER | T7 GOLD | merge_note_t6 | C6 | +12 |
| T7 GOLD | T8 STONE | merge_note_t7 | D6 | +14 |

При T7 → T8 длинное `stone_birth` занимает главное место; короткую D6 можно пропустить или оставить тихо в момент схождения. Не надо одновременно запускать обе на полной громкости. Точный музыкальный строй всех генерируемых фанфар также проверяется после прослушивания.

## Привязка к игре и порядок звуков

| Событие или действие | Основной звук | Правило |
|---|---|---|
| Ожидание в базе | music_base_loop + тихая атмосфера | Не перезапускать музыку с каждым вращением |
| SPIN / reveal | grid_spin_start → посадка | На SPIN заменяет обычный ui_click |
| Новый wild / scatter | symbol_wild_appear / symbol_scatter_land | Только при появлении, не на idle |
| mergeGroups | Стихия + нота исходного tier | Шумовая волна следует видимой линии, нота — в точке слияния |
| T1 LEAD / T5 MERCURY | merge_poison | Совпадает с текущими эффектами демо |
| T2 TIN / T6 SILVER | merge_ice | Совпадает с текущими эффектами демо |
| T3 IRON / T4 COPPER / T7 GOLD | merge_fire | Совпадает с текущими эффектами демо |
| tumbleBoard | symbol_land_light/heavy | Короткие пачки по времени посадки, не 30 слоёв сразу |
| reactionMultiplier(mergeStep) | multiplier_step | Только рост, без звука на сбросе |
| stoneCreated | stone_birth | Приоритет перед обычной фанфарой и голосом |
| freeSpinTrigger → enterBonus | bonus_trigger → music_bonus_loop | Один входной стингер на переход, не два |
| Покупка бонуса | ui_click, затем тот же bonus_trigger | После подтверждённого запуска, без второго отдельного интро |
| updateFreeSpin | Обычные звуки нового поля | Отдельный звук на номер вращения не нужен |
| freeSpinRetrigger | bonus_extra_spins | Только при реально добавленных вращениях |
| freeSpinEnd | bonus_summary или выигрышная фанфара | Выбрать один ведущий акцент; затем вернуть музыку базы |
| setTotalWin | Обычно тишина | Событие задаёт счётчик, не новую дополнительную выплату |
| finalWin > 0 | win_small либо BIG/MEGA/EPIC | Один выбранный уровень празднования; пороги зададим в клиенте |
| finalWin = 0 | Тишина | Музыка и атмосфера продолжаются |
| wincap | win_epic | Пропустить меньшие фанфары; остановить звуки дальнейшего поля |
| Подсчёт крупной суммы | win_count_loop → win_count_finish | Остановить петлю сразу по завершении или пропуску |
| Реакция алхимика | Foley / необязательный голос | Только при видимом действии, с паузами |
| Потеря/восстановление сети | ui_unavailable один раз при отклонении | Не создавать отдельный повторяющийся сигнал ожидания |

Если несколько групп сливаются одновременно, запускаем не более двух тихих стихийных текстур, а ведущую ноту выбираем по старшему tier. Несколько новых камней не должны превращаться в несколько одинаковых громких ударов. Общий приоритет: камень / вход в бонус / крупный итог → слияния → персонажи и окружение. Одновременные события разводим по времени или приглушаем нижние слои.

Обычные слияния укладываем в 0,6–0,8 с, турбо — около 0,3 с. Турбо-версии и камень около 1 с делаются монтажом выбранных исходников, без обязательных новых генераций. В режиме reduced motion звуки привязываются к игровому событию, а не числу кадров. При replay/восстановлении состояния старые звуки не воспроизводятся пачкой; пропущенный стингер не догоняем после возврата на вкладку.

## Что не требуется генерировать

Отдельный звук для каждого кадра свечи, мерцания символов и пара; щелчок на каждую цифру баланса; звуки наведения; проигрышную фанфару; семь разных исходников нот; отдельную музыку покупки бонуса; отдельную максимальную фанфару поверх EPIC. Статичные весы и свеча сами по себе постоянно не звучат.

## Как будем принимать готовые файлы

- В петлях нет слышимого стыка, скачка громкости, вступления и финального затухания.
- Короткие эффекты начинаются без пустой паузы, не клипуют и не обрываются щелчком.
- В музыке отсутствуют случайные голоса, а шумы лаборатории находятся в отдельных слоях.
- Огонь, лёд и яд различаются на слух, но одинаково сдержанны по громкости.
- Камень, бонус и крупный выигрыш различимы; персонажи не перекрывают их.
- Проверяем готовую смесь на телефоне и в наушниках; громкость, стыки и ducking настраиваются при интеграции.

Готов набор заданий на генерацию. Аудиофайлы ещё предстоит создать, выбрать на слух и подключить к игре.
