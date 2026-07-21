from app.state import StateManager
from app.config import INCOMING, SUPPORTED_TYPES


class Collector:

    def __init__(self, drive):
        self.drive = drive
        self.state = StateManager()

    def collect(self):

        root = self.drive.find_folder("DailyMemory")

        if not root:
            raise Exception("DailyMemory folder not found.")

        incoming = self.drive.find_folder(
            "Incoming",
            root["id"]
        )

        if not incoming:
            raise Exception("Incoming folder not found.")

        files = self.drive.list_files(incoming["id"])

        INCOMING.mkdir(parents=True, exist_ok=True)

        downloaded = []

        for file in files:

            if not file["mimeType"].startswith(SUPPORTED_TYPES):
                continue

            destination = INCOMING / file["name"]

            if not self.state.should_download(file["id"]):
                print(f"Skipping {file['name']} (already downloaded)")

                downloaded.append({
                    "id": file["id"],
                    "path": destination
                })

                continue

            print(f"Downloading {file['name']}...")

            self.drive.download_file(
                file["id"],
                destination
            )

            self.state.mark_downloaded(
                file["id"],
                file["name"],
                destination
            )

            downloaded.append({
                "id": file["id"],
                "path": destination
            })

        return downloaded