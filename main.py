import os

from dotenv import load_dotenv

from image_generator import clipgen
from music_generator import musicgen
from utilities import utils
from video_compiler import videogen
from voice_generator import voicegen
from webscraper import generate_input


def main():
    # Load the environment variables
    load_dotenv()
    # Configure Settings
    utils.configure_settings(os.environ.get("DEBUG")) 
    # Clear temporary directory
    utils.remove_temporary_directory()
    # Generate temporary directory
    utils.generate_temporary_directory()
    # Scrap the data from the website and save to a file
    generate_input.generate_input_files(os.environ.get("URL"))
    # Generate images / video clips from input file
    utils.validate_initial_temporary_directory_structure()
    with open("temporary/input.txt", "r") as f:
        text = f.read()
        # voicegen.generate_voice_from_text(text, os.environ.get("VOICE_PRESET"))
        musicgen.generate_music_from_text(os.environ.get("MUSIC_PRESET"))
        # clipgen.generate_video_from_text(text)
    utils.validate_filled_temporary_directory()
    videogen.generate_video()


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexcepected error occurred: {e}")
