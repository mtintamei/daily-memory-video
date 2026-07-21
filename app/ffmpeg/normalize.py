import subprocess
from pathlib import Path
from PIL import Image


PROCESSING = Path("workspace/processing")
PROCESSING.mkdir(parents=True, exist_ok=True)


class Normalizer:

    def normalize(self, media_items):

        normalized = []

        for item in media_items:

            if item.media_type == "image":
                output = self._normalize_image(item)

            else:
                output = self._normalize_video(item)

            item.path = output
            normalized.append(item)

        return normalized

    def _normalize_image(self, item):

        output = PROCESSING / f"{item.id}.jpg"

        with Image.open(item.path) as img:

            img.thumbnail((1920, 1080))

            canvas = Image.new("RGB", (1920, 1080), (0, 0, 0))

            x = (1920 - img.width) // 2
            y = (1080 - img.height) // 2

            canvas.paste(img, (x, y))

            canvas.save(output, quality=95)

        return output

    def _normalize_video(self, item):

        output = PROCESSING / f"{item.id}.mp4"

        subprocess.run([
            "ffmpeg",
            "-y",
            "-i", str(item.path),
            "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2",
            "-c:v", "libx264",
            "-c:a", "aac",
            str(output)
        ], check=True)

        return output