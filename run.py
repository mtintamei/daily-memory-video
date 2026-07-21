from app.drive import DriveClient
from app.collector import Collector
from app.metadata import MetadataExtractor


def main():

    drive = DriveClient()

    collector = Collector(drive)

    extractor = MetadataExtractor()

    downloaded = collector.collect()

    print()

    print("Media Items\n")

    for file in downloaded:

        item = extractor.build_media_item(file)

        print(item)


if __name__ == "__main__":
    main()