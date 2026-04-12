# 🎬 translator

> Learn English through movies and TV shows — extract subtitles from any video, get a bilingual dialogue, and build your personal vocabulary list with translations.

Watch a series in English → pull out every word you didn't know → get translations → repeat. That's the idea.

---

## How it works

The pipeline has two steps:

**Step 1 — Extract subtitles from a video file** (`subtitle_mp4.py`)  
Uses `ffprobe` to detect subtitle tracks inside an `.mkv` or `.mp4` file, then extracts each track as a separate `.srt` file via `ffmpeg`.

**Step 2 — Translate subtitles and collect vocabulary** (`text_from_subtitle.py`)  
Reads the `.srt` file, translates each line from English to Russian using Google Translate, and saves the bilingual dialogue to `dialogue.txt`. Then extracts all unique words, sorts them alphabetically, translates each one, and saves two files: `unique_words.txt` and `translated_words.txt`.

---

## Output files

| File | Description |
|---|---|
| `subtitles/subtitle_N_lang.srt` | Extracted subtitle tracks |
| `dialogue.txt` | Original lines + Russian translation |
| `unique_words.txt` | Sorted list of unique words from the subtitles |
| `translated_words.txt` | Word-by-word EN → RU dictionary |

---

## Requirements

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/) (must be available in `PATH`)
- Python dependencies:

```bash
pip install -r requirements.txt
```

The main dependency is [`deep-translator`](https://github.com/nidhaloff/deep-translator), which wraps Google Translate.

---

## Usage

### 1. Extract subtitles

Edit the path to your video file in `subtitle_mp4.py`:

```python
extract_subtitles_from_mp4("path/to/your/movie.mkv", output_dir="subtitles")
```

Then run:

```bash
python subtitle_mp4.py
```

Subtitle files will appear in the `subtitles/` folder.

### 2. Translate and build vocabulary

Edit the path to the extracted `.srt` file in `text_from_subtitle.py`:

```python
extract_subtitle_text_with_translation("./subtitles/subtitle_3_und.srt", "./dialogue.txt")
extract_unique_words("./dialogue.txt", "./unique_words.txt", "./translated_words.txt")
```

Then run:

```bash
python text_from_subtitle.py
```

---

## Example

Input subtitle line:
```
You gotta go. Right now.
```

`dialogue.txt` output:
```
You gotta go. Right now.
— Тебе нужно идти. Прямо сейчас.
```

`translated_words.txt` output:
```
gotta — нужно
go — идти
now — сейчас
right — правый / сейчас
you — ты
```

---

## License

[GPL-3.0](LICENSE)