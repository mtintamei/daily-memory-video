from pathlib import Path
from datetime import datetime

from moviepy import (
    ImageClip,
    VideoFileClip,
    ColorClip,
    CompositeVideoClip,
    concatenate_videoclips,
)

VIDEO_SIZE = (1920, 1080)


class Renderer:

    def render(self, media_items):

        clips = []

        for item in media_items:

            if item.media_type == "image":

                clip = (
                    ImageClip(str(item.path))
                    .resized(height=1080)
                    .with_duration(3)
                )

                if clip.w > 1920:
                    clip = clip.resized(width=1920)

                background = ColorClip(
                    size=VIDEO_SIZE,
                    color=(0, 0, 0),
                    duration=3,
                )

                clip = clip.with_position("center")

                final_clip = CompositeVideoClip(
                    [background, clip],
                    size=VIDEO_SIZE
                ).without_audio()

            else:

                clip = VideoFileClip(str(item.path))

                clip = clip.resized(height=1080)

                if clip.w > 1920:
                    clip = clip.resized(width=1920)

                background = ColorClip(
                    size=VIDEO_SIZE,
                    color=(0, 0, 0),
                    duration=clip.duration,
                )

                clip = clip.with_position("center")

                final_clip = CompositeVideoClip(
                    [background, clip],
                    size=VIDEO_SIZE
                ).with_audio(clip.audio)

            clips.append(final_clip)

        final = concatenate_videoclips(
            clips,
            method="compose"
        )

        output = Path("output")
        output.mkdir(exist_ok=True)

        capture_dates = [
            item.capture_time
            for item in media_items
            if item.capture_time is not None
        ]

        if capture_dates:
            video_date = min(capture_dates)
        else:
            video_date = datetime.now()

        filename = video_date.strftime(
            "Memory - %A %d %B %Y.mp4"
        )

        final.write_videofile(
            str(output / filename),
            codec="libx264",
            audio_codec="aac",
            fps=30,
        )