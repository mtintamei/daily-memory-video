import io
from googleapiclient.http import MediaIoBaseDownload

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


    def find_folder(self, folder_name, parent_id=None):
        query = (
            f"name='{folder_name}' "
            "and mimeType='application/vnd.google-apps.folder' "
            "and trashed=false"
        )

        if parent_id:
            query += f" and '{parent_id}' in parents"

        response = self.service.files().list(
            q=query,
            fields="files(id,name)"
        ).execute()

        folders = response.get("files", [])

        if not folders:
            return None

        return folders[0]


    def list_files(self, folder_id):
        response = self.service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields="files(id,name,mimeType)"
        ).execute()

        return response.get("files", [])
    def download_file(self, file_id, destination):
        request = self.service.files().get_media(fileId=file_id)

        with open(destination, "wb") as fh:
            downloader = MediaIoBaseDownload(fh, request)

            done = False

            while not done:
                status, done = downloader.next_chunk()
    
    
