# Chapter 1 — Practice Scripts ⚙️

A small collection of beginner Python exercises and example scripts for learning basic I/O and third-party modules.

---

## Files Overview

- `first.py` ✅
  - Prints "Hello, World!" to the console.

- `module.py` 😂
  - Uses the `pyjokes` package to fetch and print a joke.
  - Example output: `"I told my computer I needed a break, and it said: No problem — I’ll go to sleep."` (varies)

- `chapter1-ps/problem1.py` ✍️
  - Prints the nursery rhyme "Twinkle, Twinkle, Little Star" using a multiline string.

- `chapter1-ps/problem3.py` 🔊
  - Uses `pyttsx3` to speak the phrase "koi tumse pyar kyu karega" through the system TTS engine.
  - On Windows this typically uses SAPI5; ensure your audio is enabled.

- `chapter1-ps/problem4.py` 🔍
  - Attempts to list files in a directory path. Note: the `directory_path` variable uses `"/chapter 1/chapter1-ps/"` which will not work on Windows — see "Notes" below.

- `chapter1-ps/problem5.py` ⚠️
  - Currently empty.

---

## Requirements

- Python 3.8+ (recommended)
- Recommended packages:
  - `pyjokes` — for `module.py`
  - `pyttsx3` — for `chapter1-ps/problem3.py`

Install with pip:

```bash
pip install pyjokes pyttsx3
```

---

## How to run

From the project root (where `README.md` is located):

- Run a simple print script:

```bash
python first.py
```

- Run the jokes script:

```bash
python module.py
```

- Run the text-to-speech script (Windows example):

```bash
python chapter1-ps/problem3.py
```

- Run the directory listing script (fix path on Windows):

```bash
# Example fix for Windows paths in problem4.py
# change directory_path to an absolute Windows path, e.g.:
# directory_path = r"C:\Users\<you>\OneDrive\chapter 1\chapter1-ps"
python chapter1-ps/problem4.py
```

---

## Notes & Suggestions 💡

- `problem4.py` should use a valid path separator for the user OS. Use `os.path.join()` or `Path` from `pathlib` for cross-platform compatibility.
- Add content to `problem5.py` or remove it if unused.
- Consider adding a `requirements.txt` or `pyproject.toml` to pin dependencies.

---

If you'd like, I can:
- Create a `requirements.txt` with the detected dependencies ✅
- Fix the path handling in `problem4.py` to be cross-platform ✅
- Add a small sample to `problem5.py` (e.g., a simple function) ✅

Tell me which of these you'd like me to do next.