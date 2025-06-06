import os
import pyperclip
import win32clipboard
import win32con
import ExifReaderModel


class ClipboardReader:

    @staticmethod
    def read_metadata_from_clipboard(thumb_size):
        """
        Reads the clipboard for a possible image file
        :return: Returns True, Metadata directly if metadata found anywhere.
                None otherwise.
        """

        # Check if there is a file copied from the Windows Explorer
        files = ClipboardReader.get_copied_files()
        if files:
            for file in files:
                has_metadata, metadata, thumbnail, general_details = ExifReaderModel.ExifReaderModel.read_image_metadata(file, thumb_size)
                if has_metadata:
                    return has_metadata, metadata, thumbnail, general_details

        clipboard_content = pyperclip.paste()
        clipboard_content = clipboard_content.strip('"')
        clipboard_content = clipboard_content.strip("'")
        if os.path.exists(clipboard_content) and os.path.isfile(clipboard_content):
            has_metadata, metadata, thumbnail, general_details = ExifReaderModel.ExifReaderModel.read_image_metadata(clipboard_content, thumb_size)
            if has_metadata:
                return has_metadata, metadata, thumbnail, general_details
        return False, "No metadata found", None, None

    @staticmethod
    def get_clipboard():
        """
        Returns the clipboard's content
        :return: String of the clipboard content if there's any
        """
        return pyperclip.paste()

    @staticmethod
    def get_copied_files():
        """
        Get a list of files copied
        :return:
            A list of files if there's any file in the clipboard.
            Empty list otherwise
        """
        if os.name == "nt":
            win32clipboard.OpenClipboard()
            try:
                if win32clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP):
                    files = win32clipboard.GetClipboardData(win32con.CF_HDROP)
                    return list(files)  # This will be a list of file paths
                else:
                    return []
            finally:
                win32clipboard.CloseClipboard()
        else:
            return []
