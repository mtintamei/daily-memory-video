from app.metadata.image import ImageMetadataExtractor
from app.metadata.video import VideoMetadataExtractor


class MetadataExtractor:

    def __init__(self):

        self.image = ImageMetadataExtractor()
        self.video = VideoMetadataExtractor()

    def extract(self, media_item):

        if media_item.media_type == "image":
            return self.image.extract(media_item)

        return self.video.extract(media_item)