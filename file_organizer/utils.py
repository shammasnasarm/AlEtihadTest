import os
import shutil
from datetime import datetime

def get_file_type(file_name):
    return file_name.split('.')[-1].lower() if '.' in file_name else 'no_extension'

def organize_by_type(folder_path):
    print("----Organizing files by type...----")
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            ext = get_file_type(item)
            target_folder = os.path.join(folder_path, ext)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(target_folder, item))
    print("----Files organized by type!----")

def organize_by_date(folder_path):
    print("----Organizing files by date...----")
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            mod_time = os.path.getmtime(item_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
            target_folder = os.path.join(folder_path, date_folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(target_folder, item))
    print("----Files organized by date!----")

def organize_by_custom(folder_path, custom_rules):
    """
    custom_rules: dict mapping folder_name -> list of extensions
    Example: {"Images": ["jpg", "png"], "Documents": ["pdf", "docx"]}
    """
    print("----Organizing files by custom rules...----")
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            ext = get_file_type(item)
            moved = False
            for folder_name, ext_list in custom_rules.items():
                if ext in ext_list:
                    target_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(item_path, os.path.join(target_folder, item))
                    moved = True
                    break
            if not moved:
                # Move unknown extensions to 'Others'
                target_folder = os.path.join(folder_path, 'Others')
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(item_path, os.path.join(target_folder, item))
    print("----Files organized by custom rules!----")