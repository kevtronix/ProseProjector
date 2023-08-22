import os
import shutil


def list_files_in_directory(directory_path):
    all_entries = os.listdir(directory_path)
    files = [
        entry
        for entry in all_entries
        if os.path.isfile(os.path.join(directory_path, entry))
    ]
    return files


# Clear temporary directory
def remove_temporary_directory():
    try:
        shutil.rmtree("temporary")
    except FileNotFoundError:
        pass


# Generate temporary directory and needed subdirectories
def generate_temporary_directory():
    os.makedirs("temporary", exist_ok=True)
    os.makedirs("temporary/image", exist_ok=True)
