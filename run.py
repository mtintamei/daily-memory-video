from app.drive import DriveClient
from app.collector import Collector


def main():

    drive = DriveClient()

    collector = Collector(drive)

    downloaded = collector.collect()

    print()

    print("Downloaded files:")

    for file in downloaded:
        print(file.name)

    print()
    print(f"Downloaded {len(downloaded)} files.")


if __name__ == "__main__":
    main()