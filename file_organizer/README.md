# File Organizer

Organizes files in a given directory into subfolders by **type** (extension), **date** (last-modified date), or **custom rules** (extension-to-folder mapping).

---

## Setup & Run

```bash
# No third-party dependencies (Python stdlib only)

# Organize by file type (default)
python main.py /path/to/messy/folder

# Organize by last-modified date (creates folders like: 2026-03-04)
python main.py /path/to/messy/folder --mode date

# Organize by custom rules (defined in main.py)
python main.py /path/to/messy/folder --mode custom
```

---

## Modes

### `type` (default)

- Creates folders based on extension (example: `pdf/`, `jpg/`)
- Files without extension go to `no_extension/`

### `date`

- Creates folders based on last modified date (example: `2026-03-04/`)

### `custom`

- Uses the `custom_rules` mapping inside `main.py`
- Unknown extensions go to `Others/`

---

## Why I use this approach

- Simple to implement and run
- Cross-platform safe (works on Linux, Mac, and Windows)
- `pathlib.Path` makes file operations clean and readable
