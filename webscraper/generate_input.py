import webscraper.web_parser


def generate_input_files(url):
    # generate voice input
    content = webscraper.web_parser.get_url_content(url)
    with open("temporary/input.txt", "w") as f:
        f.write(content)
