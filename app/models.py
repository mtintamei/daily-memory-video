from dataclasses import dataclass
from pathlib import Path
from datetime import datetime


@dataclass
class MediaItem:
    filename: str
    path: Path
    media_type: str          # "image" or "video"
    capture_time: datetime | None = None
    duration: float | None = None
    width: int | None = None
    height: int | None = None
    gps: tuple | None = None