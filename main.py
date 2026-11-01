import argparse
from pathlib import Path

from utils import organize_directory


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by type and rename them with timestamps."
    )
    parser.add_argument(
        "directory",
        help="Path to the directory containing files to organize.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Display what would happen without moving any files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_dir = Path(args.directory).expanduser().resolve()

    if not target_dir.exists():
        raise FileNotFoundError(f"Directory does not exist: {target_dir}")
    if not target_dir.is_dir():
        raise NotADirectoryError(f"Not a directory: {target_dir}")

    organize_directory(target_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
