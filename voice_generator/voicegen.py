import scipy, torch 
from transformers import AutoProcessor, BarkModel
import nltk
from nltk.tokenize import sent_tokenize


# Helper function to split input text into sentences for processing
def get_sentences(text):
    # download puntk if not downloaded
    nltk.download("punkt", quiet=True)
    # split the text into sentences and return a list
    return sent_tokenize(text)


# Generate voice using the model
def generate_voice(text, voice_preset):
    # Load Model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = AutoProcessor.from_pretrained("suno/bark")
    model = BarkModel.from_pretrained("suno/bark").to(device)
    # Generate silence
    sample_rate = model.generation_config.sample_rate
    silence_duration = 0.1
    silence_length = int(silence_duration * sample_rate)

    total_speech = []
    for sentence in get_sentences(text):
        print("Progress: ", f"{len(total_speech) / len(get_sentences(text)) * 100} %")
        inputs = processor(
            text=[sentence],
            voice_preset=voice_preset,
            return_tensors="pt",
        ).to(device)

        sentence_speech_values = model.generate(**inputs)
        # Add silence to the end of each sentence
        batch_size = sentence_speech_values.size(0)
       #  silence = torch.zeros(batch_size, silence_length).to(device)

        total_speech.append(sentence_speech_values)
        # total_speech.append(silence)
        

    full_speech = torch.cat(total_speech, dim=1) 
    return full_speech, sample_rate


# Save the voice to a file
def save_voice(full_speech, sampling_rate, output_path):
    scipy.io.wavfile.write(
        output_path, sampling_rate, full_speech.cpu().numpy().squeeze()
    )


# Construct voice recording file from text
def generate_voice_from_text(text, voice_preset):
    full_speech, sampling_rate = generate_voice(text, voice_preset)
    save_voice(full_speech, sampling_rate, output_path="temporary/voice.wav")
