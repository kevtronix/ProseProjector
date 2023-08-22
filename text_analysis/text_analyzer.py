import nltk
import torch
from nltk.tokenize import sent_tokenize
from transformers import T5ForConditionalGeneration, T5Tokenizer


def get_sentences(text):
    # download puntk if not downloaded
    nltk.download("punkt", quiet=True)
    # split the text into sentences and return a list
    return sent_tokenize(text)


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
    input_text = f"take the following text and turn into detailed prompt used for image generation: '{text}'"
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
    input_text = f"Generate a negative prompt for the following prompt: '{text}'"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    input_ids = input_ids.to(device)
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
