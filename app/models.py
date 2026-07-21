from dataclasses import dataclass
from pathlib import Path
from datetime import datetime


@dataclass
class MediaItem:
    id: str

    filename: str
    path: Path
    media_type: str

    capture_time: datetime | None = None
    duration: float | None = None

    width: int | None = None
    height: int | None = None

    fps: float | None = None

    gps: tuple | None = None