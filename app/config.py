from pathlib import Path

# Project paths
PROJECT_ROOT = Path.cwd()

WORKSPACE = PROJECT_ROOT / "workspace"

INCOMING = WORKSPACE / "incoming"
PROCESSING = WORKSPACE / "processing"
ARCHIVE = WORKSPACE / "archive"
FAILED = WORKSPACE / "failed"

# Supported media
SUPPORTED_IMAGE_TYPES = (
    "image/",
)

SUPPORTED_VIDEO_TYPES = (
    "video/",
)

SUPPORTED_TYPES = SUPPORTED_IMAGE_TYPES + SUPPORTED_VIDEO_TYPES