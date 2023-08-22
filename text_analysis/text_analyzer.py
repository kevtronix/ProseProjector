from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import nltk, torch
from nltk.tokenize import sent_tokenize


def get_sentences(text):
    # download puntk if not downloaded
    nltk.download("punkt", quiet=True)
    # split the text into sentences and return a list
    return sent_tokenize(text)

def generate_musical_description(text):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # load tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
    model = T5ForConditionalGeneration.from_pretrained(
        "google/flan-t5-large", 
        torch_dtype=torch.float16,
        device_map="auto",
    )
    # generate main theme
    input_text = f"take the following text and turn into a detailed description of music that matches what the text is talking about: '{text}'"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    input_ids = input_ids.to(device)
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# use T5 model to identify main theme of a given input
def generate_descriptive_phrases_of_text(text):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # load tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
    model = T5ForConditionalGeneration.from_pretrained(
        "google/flan-t5-large", 
        torch_dtype=torch.float16,
        device_map="auto",
    )
    # generate main theme
    input_text = f"take the following text and turn into a general description of a scene that represents what it is saying which can be turned into an image: '{text}'"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    input_ids = input_ids.to(device)
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def generate_negative_prompt(text):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # load tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
    model = T5ForConditionalGeneration.from_pretrained(
        "google/flan-t5-large",
        torch_dtype=torch.float16,
        device_map="auto",
    )
    # generate main theme
    input_text = f"Generate a negative prompt for the following text: '{text}'"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    input_ids = input_ids.to(device)
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
