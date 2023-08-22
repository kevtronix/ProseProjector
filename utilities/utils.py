import os

def list_files_in_directory(directory_path):
    all_entries = os.listdir(directory_path)
    files = [entry for entry in all_entries if os.path.isfile(os.path.join(directory_path, entry))]
    return files