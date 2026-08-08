from moviepy import ImageClip, AudioFileClip
import os

IMAGE_PATH = "output/quote.png"
AUDIO_PATH = "assets/music.mp3"
OUTPUT_VIDEO = "output/short.mp4"

VIDEO_DURATION = 15   # seconds


def create_video():

    image = ImageClip(IMAGE_PATH)
    image = image.with_duration(VIDEO_DURATION)

    audio = AudioFileClip(AUDIO_PATH)

    # Trim music if longer than video
    if audio.duration > VIDEO_DURATION:
        audio = audio.subclipped(0, VIDEO_DURATION)

    # If music is shorter, loop it
    elif audio.duration < VIDEO_DURATION:
        audio = audio.with_effects([]).loop(duration=VIDEO_DURATION)

    video = image.with_audio(audio)

    video.write_videofile(
        OUTPUT_VIDEO,
        fps=30,
        codec="libx264",
        audio_codec="aac"
    )

    return OUTPUT_VIDEO


if __name__ == "__main__":
    create_video()