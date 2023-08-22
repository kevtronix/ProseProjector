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
    # Clear temporary directory
    utils.remove_temporary_directory()
    # Generate temporary directory
    utils.generate_temporary_directory()
    # Scrap the data from the website and save to a file
    generate_input.generate_input_files(os.environ.get("URL"))
    # Generate images / video clips from input file
    if os.path.exists("temporary/input.txt"):
        with open("temporary/input.txt", "r") as f:
            text = f.read()
            # voicegen.generate_voice_from_text(text, os.environ.get("VOICE_PRESET"))
    #         musicgen.generate_music_from_text(os.environ.get("MUSIC_PRESET"))
            clipgen.generate_video_from_text(text)
    else:
        raise FileNotFoundError("Error: Input file does not exist!!")
    # Generate the final output file
    # check that all the needed files exist
    # if not, raise an exception
    if (
        os.path.exists("temporary/voice.wav")
        and os.path.exists("temporary/music.wav")
        and os.listdir("temporary/image")
    ):
        print("All files exist")
        videogen.generate_video()
        print("Generated video")
    # Combine the voice and music files
    else:
        raise FileNotFoundError("Error: One or more required files do not exist!!")


if __name__ == "__main__":
    main()
