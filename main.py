import os
from dotenv import load_dotenv
from webscraper import generate_input


def main():
    # Load the environment variables
    load_dotenv()
    print(os.environ.get("URL"))
    # Scrap the data from the website and save to a file
    generate_input.generate_input_files(os.environ.get("URL"))


if __name__ == "__main__":
    main()
