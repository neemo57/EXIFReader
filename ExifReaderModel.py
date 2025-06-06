import os.path

from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ImageTk import PhotoImage


class ExifReaderModel:

    def __init__(self):
        pass

    @staticmethod
    def read_image_metadata(image_path, thumbnail_size):
        """
        Reads the MetaData from an image file.

        @returns
            True, Metadata, Thumbnail if metadata exists
            False, Error, None Message otherwise.
        """
        try:
            if os.path.exists(image_path) and os.path.isfile(image_path):
                img = Image.open(image_path)

                # Read meta data
                image_metadata = img.info
                output = []
                if image_metadata:
                    for key, value in image_metadata.items():
                        if key != "exif":
                            entry = (str(key), str(value))
                            output.append(entry)

                # Read EXIF data
                exif_data = img.getexif()
                if exif_data:
                    # Padding
                    output.append(("", ""))
                    output.append(("EXIF DATA", ""))

                    for id_, value in exif_data.items():
                        true_id = TAGS.get(id_, id_)
                        output.append(( str(true_id), str(value) ))

                # Get general details
                general_details = [("Image Width", f"{img.width}px"),
                                   ("Image Height", f"{img.height}px"),
                                   ("Image Size", f"{img.size}bytes"),
                                   ("Image Path", f"{img.filename}"),
                                   ("Image Format", f"{img.format}")]

                # Produce thumbnail
                img.thumbnail(thumbnail_size)
                thumbnail = PhotoImage(img)


                if not output:
                    output.append(("No metadata found", "No metadata found"))
                return True, output, thumbnail, general_details
            else:
                return False, f"Image {image_path} does not exist.", None, None
        except Image.UnidentifiedImageError:
            return False, f"Image {image_path} is not a readable\\valid image.", None, None
        except Exception:
             return False, "Failed to read Image. Unhandled Exception !", None, None

