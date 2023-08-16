import scipy
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoProcessor, MusicgenForConditionalGeneration


# use T5 model to identify main theme of a given input
def generate_main_theme(input_text):
    # load tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
    model = T5ForConditionalGeneration.from_pretrained(
        "google/flan-t5-small", device_map="auto"
    )
    # generate main theme
    input = f"generate main theme of: {input_text}"
    input_ids = tokenizer(input, return_tensors="pt").input_ids
    input_ids = input_ids.to(model.device)
    outputs = model.generate(input_ids, max_length=59)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Analyze the main theme and generate music using facebook/musicgen-small
def generate_music(main_theme):
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained(
        "facebook/musicgen-small"
    ).to("cuda") 
    inputs = processor(
        text=[main_theme],
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
    main_theme = generate_main_theme(text)
    audio_values, sampling_rate = generate_music(main_theme)
    save_music(audio_values, sampling_rate, output_path="temporary/music.wav")
