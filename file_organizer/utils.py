from pathlib import Path
from datetime import datetime


def organize_by_type(folder_path):
    print("----Organizing files by type...----")
    folder = Path(folder_path)
    for item in folder.iterdir():
        if item.is_file():
            ext = item.suffix.lstrip('.').lower() or 'no_extension'
            target_folder = folder / ext
            target_folder.mkdir(exist_ok=True)
            item.rename(target_folder / item.name)
    print("----Files organized by type!----")


def organize_by_date(folder_path):
    print("----Organizing files by date...----")
    folder = Path(folder_path)
    for item in folder.iterdir():
        if item.is_file():
            mod_time = item.stat().st_mtime
            date_folder = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
            target_folder = folder / date_folder
            target_folder.mkdir(exist_ok=True)
            item.rename(target_folder / item.name)
    print("----Files organized by date!----")


def organize_by_custom(folder_path, custom_rules):
    print("----Organizing files by custom rules...----")
    folder = Path(folder_path)
    for item in folder.iterdir():
        if item.is_file():
            ext = item.suffix.lstrip('.').lower() or 'no_extension'
            moved = False
            for folder_name, ext_list in custom_rules.items():
                if ext in ext_list:
                    target_folder = folder / folder_name
                    target_folder.mkdir(exist_ok=True)
                    item.rename(target_folder / item.name)
                    moved = True
                    break
            if not moved:
                target_folder = folder / 'Others'
                target_folder.mkdir(exist_ok=True)
                item.rename(target_folder / item.name)
    print("----Files organized by custom rules!----")