from pathlib import Path

from app.models import MediaItem


class MetadataExtractor:

    def build_media_item(self, path: Path):

        suffix = path.suffix.lower()

        if suffix in [".jpg", ".jpeg", ".png", ".avif"]:
            media_type = "image"
        else:
            media_type = "video"

        return MediaItem(
            filename=path.name,
            path=path,
            media_type=media_type,
        )