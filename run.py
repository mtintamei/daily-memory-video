from app.drive import DriveClient

SUPPORTED_TYPES = (
    "image/",
    "video/",
)


def main():
    drive = DriveClient()

    root = drive.find_folder("DailyMemory")

    if not root:
        print("❌ DailyMemory folder not found.")
        return

    print(f"✅ Found folder: {root['name']}")

    incoming = drive.find_folder(
        "Incoming",
        root["id"]
    )

    if not incoming:
        print("❌ Incoming folder not found.")
        return

    print(f"✅ Found folder: {incoming['name']}")

    print("\nMedia files:\n")

    files = drive.list_files(incoming["id"])

    for file in files:
        if file["mimeType"].startswith(SUPPORTED_TYPES):
            print(f"{file['name']} ({file['mimeType']})")


if __name__ == "__main__":
    main()