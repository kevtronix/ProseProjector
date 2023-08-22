import os
from dotenv import load_dotenv
from webscraper import generate_input
from voice_generator import voicegen
from music_generator import musicgen
from image_generator import clipgen
from video_compiler import videogen


def main():
    # Load the environment variables
    load_dotenv()
    # Scrap the data from the website and save to a file
    generate_input.generate_input_files(os.environ.get("URL"))
    # Generate voice from input file
    # Generate music from input file
    # Generate images / video clips from input file
    if os.path.exists("temporary/input.txt"):
        with open("temporary/input.txt", "r") as f:
            text = f.read()
            voicegen.generate_voice_from_text(text, os.environ.get("VOICE_PRESET"))
            musicgen.generate_music_from_text(text)
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
