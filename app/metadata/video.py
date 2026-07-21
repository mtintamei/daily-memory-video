from pymediainfo import MediaInfo
from datetime import datetime


class VideoMetadataExtractor:

    def extract(self, media_item):

        media = MediaInfo.parse(media_item.path)

        for track in media.tracks:

            if track.track_type == "Video":

                media_item.width = track.width
                media_item.height = track.height

                if track.frame_rate:
                    media_item.fps = float(track.frame_rate)

                if track.duration:
                    media_item.duration = float(track.duration) / 1000

                if track.tagged_date:
                    try:
                        media_item.capture_time = datetime.strptime(
                            track.tagged_date.replace(" UTC", ""),
                            "%Y-%m-%d %H:%M:%S"
                        )
                    except Exception:
                        pass

        return media_item