import argparse
from pathlib import Path

from utils import organize_by_type, organize_by_date, organize_by_custom


def main():
    parser = argparse.ArgumentParser(description="File Organizer")
    parser.add_argument("folder", help="Path to the folder to organize")
    parser.add_argument(
        "--mode",
        choices=["type", "date", "custom"],
        default="type",
        help="Mode of organization (default: type)"
    )
    args = parser.parse_args()

    folder_path = Path(args.folder)
    mode = args.mode

    if not folder_path.is_dir():
        print("----Invalid folder path!----")
        return

    if mode == "type":
        organize_by_type(folder_path)
    elif mode == "date":
        organize_by_date(folder_path)
    elif mode == "custom":
        # Example custom rules, can be loaded from JSON/config file
        custom_rules = {
            "Images": ["jpg", "jpeg", "png", "gif"],
            "Documents": ["pdf", "docx", "txt", "xlsx"],
            "Videos": ["mp4", "mov", "avi"]
        }
        organize_by_custom(folder_path, custom_rules)

if __name__ == "__main__":
    main()