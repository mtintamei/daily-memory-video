from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


class DriveClient:

    def __init__(self):
        self.creds = self.authenticate()
        self.service = build("drive", "v3", credentials=self.creds)

    def authenticate(self):
        creds = None

        if Path("token.json").exists():
            creds = Credentials.from_authorized_user_file(
                "token.json",
                SCOPES
            )

        if not creds or not creds.valid:

            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())

            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json",
                    SCOPES
                )

                creds = flow.run_local_server(port=0)

            with open("token.json", "w") as token:
                token.write(creds.to_json())

        return creds

    def list_recent_files(self, limit=10):

        results = self.service.files().list(
            pageSize=limit,
            fields="files(id, name, mimeType, createdTime)"
        ).execute()

        return results.get("files", [])