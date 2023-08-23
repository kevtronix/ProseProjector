import noisereduce as nr
import scipy
import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration

from utilities.utils import reduce_noise


# Analyze the main theme and generate music using facebook/musicgen-small
def generate_music(prompt):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained(
        "facebook/musicgen-small"
    ).to(device)
    inputs = processor(
        text=[prompt],
        padding=True,
        return_tensors="pt",
    ).to(device)

    audio_values = model.generate(**inputs, max_new_tokens=1000)
    sample_rate = model.config.audio_encoder.sampling_rate
    return audio_values.cpu().numpy().squeeze(), sample_rate


# Create a music file from audio values
def save_music(audio_values, sampling_rate, output_path):
    scipy.io.wavfile.write(
        output_path, sampling_rate, audio_values.cpu().numpy().squeeze()
    )


# Construct music file from text
def generate_music_from_text(prompt):
    audio_values_array, sampling_rate = generate_music(prompt)
    audio_values = reduce_noise(audio_values_array, sampling_rate)
    save_music(audio_values, sampling_rate, output_path="temporary/music.wav")
