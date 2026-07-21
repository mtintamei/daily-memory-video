from app.drive import DriveClient
from app.collector import Collector
from app.metadata.extractor import MetadataExtractor
from app.timeline.builder import TimelineBuilder
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

        media_items.append(
            extractor.extract(item)
        )

    media_items = timeline.build(media_items)

    print("\nTimeline\n")

    for item in media_items:
        print(item)


if __name__ == "__main__":
    main()