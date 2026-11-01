# Automated Local File Organizer

A Python-based tool that scans a directory, categorizes files by extension, moves them into folders such as `Documents`, `Images`, and `Videos`, and renames them using a timestamp.

## Features

- Automatically detects file types using extensions
- Sorts files into categories like:
  - Documents
  - Images
  - Videos
  - Audio
  - Archives
  - Others
- Renames files using a timestamp format such as `YYYYMMDD_HHMMSS`
- Supports a safe `--dry-run` preview mode before moving files
- Requires no third-party libraries

## Project Structure

```text
AI-Models/
├── main.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/solodevelopersai/AI-Models.git
cd AI-Models
```

2. Ensure Python 3.9+ is installed:

```bash
python --version
```

3. Install dependencies (if any):

```bash
pip install -r requirements.txt
```

Note: This project uses the Python standard library only, so the requirements file may be minimal.

## Usage

Run the script against a target folder:

```bash
python main.py /path/to/folder
```

Preview moves without changing files:

```bash
python main.py /path/to/folder --dry-run
```

## Example

If you have files such as:

```text
project/
├── report.pdf
├── photo.jpg
├── clip.mp4
├── notes.txt
```

After running:

```bash
python main.py project
```

The structure may become:

```text
project/
├── Documents/
│   ├── 20261101_143022_report.pdf
│   └── 20261101_143023_notes.txt
├── Images/
│   └── 20261101_143024_photo.jpg
├── Videos/
│   └── 20261101_143025_clip.mp4
```

## License

This project is provided as-is for local file organization and personal automation tasks.

## Notes

- Files are moved into category folders created within the same directory.
- Existing files with the same name may get a numeric suffix to prevent overwrites.
- Hidden/system files are ignored by default.
