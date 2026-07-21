from app.drive import DriveClient
from app.collector import Collector
from app.metadata.extractor import MetadataExtractor
from app.timeline.builder import TimelineBuilder
from app.ffmpeg.normalize import Normalizer
from app.renderer.renderer import Renderer
from app.models import MediaItem


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".avif",
}


def main():

    drive = DriveClient()
    collector = Collector(drive)
    extractor = MetadataExtractor()
    timeline = TimelineBuilder()
    normalizer = Normalizer()
    renderer = Renderer()

    downloaded = collector.collect()

    media_items = []

    for media in downloaded:

        path = media["path"]
        file_id = media["id"]

        media_type = (
            "image"
            if path.suffix.lower() in IMAGE_EXTENSIONS
            else "video"
        )

        item = MediaItem(
            id=file_id,
            filename=path.name,
            path=path,
            media_type=media_type,
        )

        media_items.append(extractor.extract(item))

    media_items = timeline.build(media_items)

    media_items = normalizer.normalize(media_items)

    renderer.render(media_items)


if __name__ == "__main__":
    main()