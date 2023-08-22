import torch
from diffusers import (
    AutoPipelineForText2Image,
    DiffusionPipeline,
    DPMSolverMultistepScheduler,
)
from diffusers.utils import export_to_video
from PIL import Image

from text_analysis import text_analyzer


def generate_kandinsky_image(prompt, negative_prompt):
    torch.cuda.empty_cache()
    pipe = AutoPipelineForText2Image.from_pretrained(
        "kandinsky-community/kandinsky-2-2-decoder", torch_dtype=torch.float16
    )
    pipe.enable_model_cpu_offload()

    image = pipe(
        prompt=f"cinematic, colorful, {prompt}",
        negative_prompt=f"non-cinematic, dull scene of {negative_prompt}",
        prior_guidance_scale=1.0,
        height=768,
        width=768,
    ).images[0]
    return image


def save_image(image, output_path):
    image.save(output_path)


def generate_clip(prompt):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    pipe = DiffusionPipeline.from_pretrained(
        "cerspense/zeroscope_v2_576w", torch_dtype=torch.float16
    ).to(device)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_model_cpu_offload()

    video_frames = pipe(
        prompt, num_inference_steps=100, num_frames=11, height=320, width=576
    ).frames
    torch.cuda.empty_cache()
    return video_frames


# Upscale video Clip from text need 16GB of VRAM to run
def upscale_clip(prompt, video_frames):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    pipe = DiffusionPipeline.from_pretrained(
        "cerspense/zeroscope_v2_XL", torch_dtype=torch.float16
    ).to(device)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_slicing()
    video = [Image.fromarray(frame).resize((1024, 576)) for frame in video_frames]
    upscaled_frames = pipe(prompt, video=video, strength=0.6).frames
    return upscaled_frames


def save_video(video_frames, output_path):
    print(export_to_video(video_frames, output_video_path=output_path))


def generate_video_from_text(text):
    paragraphs = text_analyzer.get_sentences(text)
    for count, paragraph in enumerate(paragraphs):
        image_prompt = text_analyzer.generate_descriptive_phrases_of_text(paragraph)
        negative_image_prompt = text_analyzer.generate_negative_prompt(image_prompt)
        image = generate_kandinsky_image(image_prompt, negative_image_prompt)
        save_image(image, f"temporary/image/image{count}.png")
