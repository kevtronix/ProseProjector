import os
from dotenv import load_dotenv
from webscraper import generate_input
from voice_generator import voicegen
from music_generator import musicgen

def main():
    # Load the environment variables
    load_dotenv()
    # Scrap the data from the website and save to a file
    generate_input.generate_input_files(os.environ.get("URL"))
    # Generate voice from input file 
    # Generate music from input file
    if os.path.exists("temporary/input.txt"):
        with open("temporary/input.txt", "r") as f:
            text = f.read()
        voicegen.generate_voice_from_text(text, os.environ.get("VOICE_PRESET"))
        musicgen.generate_music_from_text(text)
    else:
        raise Exception("Error: Input file does not exist!!")


if __name__ == "__main__":
    main()
