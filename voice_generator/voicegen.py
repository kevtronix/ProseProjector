import scipy
import torch
from transformers import AutoProcessor, BarkModel

from text_analysis.text_analyzer import get_sentences
from utilities.utils import reduce_noise


# Generate voice using the model
def generate_voice(text, voice_preset):
    # Load Model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = AutoProcessor.from_pretrained("suno/bark")
    model = BarkModel.from_pretrained("suno/bark").to(device)
    # Generate silence
    sample_rate = model.generation_config.sample_rate
    total_speech = []
    for sentence in get_sentences(text):
        inputs = processor(
            text=[sentence],
            voice_preset=voice_preset,
            return_tensors="pt",
        ).to(device)
        sentence_speech_values = model.generate(**inputs)
        total_speech.append(sentence_speech_values)
    full_speech = torch.cat(total_speech, dim=1)
    return full_speech.cpu().numpy().squeeze(), sample_rate


# Save the voice to a file
def save_voice(full_speech, sampling_rate, output_path):
    scipy.io.wavfile.write(output_path, sampling_rate, full_speech)


# Construct voice recording file from text
def generate_voice_from_text(text, voice_preset):
    full_speech, sampling_rate = generate_voice(text, voice_preset)
    full_speech = reduce_noise(full_speech, sampling_rate)
    save_voice(full_speech, sampling_rate, output_path="temporary/voice.wav")
