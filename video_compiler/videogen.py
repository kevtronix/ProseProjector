import os
from moviepy.editor import *
from utilities import utils


def generate_video():
    # set the voice 
    voice = AudioFileClip("temporary/voice.wav")
    total_duration = voice.duration
    # set the music and loop it to match the length of the voice
    background_music = AudioFileClip("temporary/music.wav")
    looped_music = background_music.audio_loop(duration=total_duration)
    # Combine the voice and music
    final_audio = CompositeAudioClip([looped_music.volumex(0.1), voice.volumex(0.9)])

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
