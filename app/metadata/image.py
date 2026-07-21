from datetime import datetime

import exifread
from PIL import Image


class ImageMetadataExtractor:

    def extract(self, media_item):

        with Image.open(media_item.path) as img:
            media_item.width = img.width
            media_item.height = img.height

        with open(media_item.path, "rb") as f:

            tags = exifread.process_file(f, details=False)

        if "EXIF DateTimeOriginal" in tags:

            media_item.capture_time = datetime.strptime(
                str(tags["EXIF DateTimeOriginal"]),
                "%Y:%m:%d %H:%M:%S"
            )

        if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:

            media_item.gps = (
                str(tags["GPS GPSLatitude"]),
                str(tags["GPS GPSLongitude"])
            )

        return media_item