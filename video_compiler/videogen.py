import scipy
from moviepy.editor import *

from utilities import utils


def configure_voice(
    source_audio_path="temporary/voice.wav",
):
    voice = AudioFileClip(source_audio_path)
    voice = voice.fx(afx.volumex, 2)
    return voice


def configure_music(duration, source_audio_path="temporary/music.wav"):
    music = AudioFileClip(source_audio_path)
    music = music.fx(afx.volumex, 0.01)
    music = music.audio_loop(duration=duration)
    return music


def generate_video():
    # set the voice
    voice = configure_voice()
    total_duration = voice.duration
    # set the music and loop it to match the length of the voice
    music = configure_music(total_duration)
    # Combine the voice and music
    final_audio = CompositeAudioClip([music, voice])

    # set the images
    images = utils.list_files_in_directory("temporary/image")
    images.sort()
    duration_of_clip = total_duration / len(images)

    # convert the images to video clips
    clips = [
        ImageClip(f"temporary/image/{image}").set_duration(duration_of_clip)
        for image in images
    ]

    video = concatenate_videoclips(clips, method="compose").set_audio(final_audio)

    video.write_videofile("output.mp4", fps=24)
