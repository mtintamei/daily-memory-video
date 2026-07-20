from app.drive import DriveClient


def main():

    drive = DriveClient()

    files = drive.list_recent_files()

    print("\nRecent files:\n")

    for file in files:
        print(f"{file['name']} ({file['mimeType']})")


if __name__ == "__main__":
    main()