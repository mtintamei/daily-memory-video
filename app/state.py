import json
from pathlib import Path


class StateManager:

    def __init__(self):
        self.state_file = Path("state.json")

        if self.state_file.exists():
            with open(self.state_file, "r") as f:
                self.state = json.load(f)
        else:
            self.state = {
                "files": {}
            }

    def save(self):
        with open(self.state_file, "w") as f:
            json.dump(self.state, f, indent=4)

    def get(self, file_id):
        return self.state["files"].get(file_id)

    def should_download(self, file_id):

        record = self.get(file_id)

        if record is None:
            return True

        local_path = Path(record["local_path"])

        return not local_path.exists()

    def mark_downloaded(self, file_id, filename, local_path):

        self.state["files"][file_id] = {
            "filename": filename,
            "local_path": str(local_path)
        }

        self.save()