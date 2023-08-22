import os
import shutil
import logging


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


# Validate configured temporary directory and needed subdirectories
def validate_initial_temporary_directory_structure():
    if not os.path.exists("temporary"):
        raise FileNotFoundError("Error: Temporary directory does not exist!!")
    if not os.path.exists("temporary/input.txt"):
        raise FileNotFoundError("Error: Temporary input file does not exist!!")
    if not os.path.exists("temporary/image"):
        raise FileNotFoundError("Error: Temporary image directory does not exist!!")


# Validate temporary directory and needed subdirectories and files
def validate_filled_temporary_directory():
    if not os.path.exists("temporary"):
        raise FileNotFoundError("Error: Temporary directory does not exist!!")
    if not os.path.exists("temporary/image"):
        raise FileNotFoundError("Error: Temporary image directory does not exist!!")
    if len(os.listdir("temporary/image")) == 0:
        raise FileNotFoundError("Error: Temporary image directory is empty!!")
    if not os.path.exists("temporary/voice.wav"):
        raise FileNotFoundError("Error: Temporary voice file does not exist!!")
    if not os.path.exists("temporary/music.wav"):
        raise FileNotFoundError("Error: Temporary music file does not exist!!")


def configure_logging(debug):
    if debug:
        pass 
    else:
        logging.getLogger("transformers").setLevel(logging.ERROR) 

def configure_settings(debugString):
    if debugString == "True":
        configure_logging(True)
    else:
        configure_logging(False)
    