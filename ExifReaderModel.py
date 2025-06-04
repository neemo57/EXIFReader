import exifread

class ExifReaderModel:

    def __init__(self):
        pass

    @staticmethod
    def read_image_metadata(image_path):
        """
        Reads the MetaData from an image file.

        :returns
            True, Metadata if metadata exists
            False, None otherwise.
        """
        try:
            with open(image_path, "rb") as f:
                tags = exifread.process_file(f)
            return tags
        except Exception:
            return None

