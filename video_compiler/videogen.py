from moviepy.editor import *


def generate_video():
    # set the voice
    voice = AudioFileClip("temporary/voice.wav")
    # set the music and loop it to match the length of the voice
    music = AudioFileClip("temporary/music.wav").set_duration(voice.duration)

    # Combine the voice and music
    final_audio = CompositeAudioClip([music.volumex(0.3), voice.volumex(0.7)])
