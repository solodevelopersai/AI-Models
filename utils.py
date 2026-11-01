import shutil
from datetime import datetime
from pathlib import Path

CATEGORIES = {
    "Documents": {
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".rtf",
        ".odt",
        ".ppt",
        ".pptx",
        ".xls",
        ".xlsx",
        ".csv",
        ".md",
        ".json",
        ".xml",
        ".html",
        ".htm",
    },
    "Images": {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".svg",
        ".webp",
        ".tif",
        ".tiff",
    },
    "Videos": {
        ".mp4",
        ".mkv",
        ".mov",
        ".avi",
        ".wmv",
        ".flv",
        ".webm",
        ".mpeg",
        ".mpg",
    },
    "Audio": {
        ".mp3",
        ".wav",
        ".flac",
        ".aac",
        ".ogg",
        ".m4a",
    },
    "Archives": {
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
        ".bz2",
        ".xz",
    },
}


def get_category(file_path: Path) -> str:
    extension = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def build_unique_path(destination_dir: Path, original_name: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_stem = Path(original_name).stem
    file_ext = Path(original_name).suffix

    candidate = destination_dir / f"{timestamp}_{file_stem}{file_ext}"
    counter = 1

    while candidate.exists():
        candidate = destination_dir / f"{timestamp}_{file_stem}_{counter}{file_ext}"
        counter += 1

    return candidate


def organize_directory(directory: Path, dry_run: bool = False) -> None:
    """Sort files inside a directory into category folders and rename them with timestamps."""
    directory = directory.expanduser().resolve()

    if not directory.exists() or not directory.is_dir():
        raise ValueError(f"Invalid directory: {directory}")

    organized_files = 0

    for item in sorted(directory.iterdir()):
        if item.is_dir():
            continue

        category = get_category(item)
        destination_dir = directory / category
        destination_dir.mkdir(exist_ok=True)

        new_path = build_unique_path(destination_dir, item.name)

        if dry_run:
            print(f"[DRY RUN] {item.name} -> {new_path.relative_to(directory)}")
            continue

        shutil.move(str(item), str(new_path))
        print(f"Moved: {item.name} -> {new_path.relative_to(directory)}")
        organized_files += 1

    if organized_files == 0:
        print("No files were moved. The directory is already organized or contains no supported files.")
    else:
        print(f"\nFinished organizing {organized_files} file(s).")
