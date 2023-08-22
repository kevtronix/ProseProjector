import scipy
from transformers import AutoProcessor, MusicgenForConditionalGeneration
from text_analysis import text_analyzer


# Analyze the main theme and generate music using facebook/musicgen-small
def generate_music(prompt):
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained(
        "facebook/musicgen-small"
    ).to("cuda")
    inputs = processor(
        text=[f"melody, piano,{prompt}"],
        padding=True,
        return_tensors="pt",
    ).to("cuda")

    audio_values = model.generate(**inputs, max_new_tokens=1000)
    sample_rate = model.config.audio_encoder.sampling_rate
    return audio_values, sample_rate


# Create a music file from audio values
def save_music(audio_values, sampling_rate, output_path):
    scipy.io.wavfile.write(
        output_path, sampling_rate, audio_values.cpu().numpy().squeeze()
    )


# Construct music file from text
def generate_music_from_text(text):
    prompt = text_analyzer.generate_musical_description(text)
    audio_values, sampling_rate = generate_music(prompt)
    save_music(audio_values, sampling_rate, output_path="temporary/music.wav")
