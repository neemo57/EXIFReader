from model import Model
from centralview import MainView
from tkinter import Tk, Event
import os
from PIL import Image, ImageTk

"""
    Main controller class for the EXIFReader App.
"""

class MainController:

    # Main Window Properties
    ROOT_WINDOW_WIDTH_RATIO = 0.6
    ROOT_WINDOW_HEIGHT_RATIO = 0.6
    BORDERLESS = True
    DEFAULT_TITLE = "EXIF Reader v1.1.0"
    DEFAULT_OPACITY = 0.95

    # Path Variables
    ASSETS_FOLDER = "Assets"
    BACKGROUND_IMAGE = "background.jpg"

    # For Image Loading
    VALID_EXTENSIONS = [".jpeg", ".jpg", ".png"]

    def __init__(self, root_window:Tk, title=DEFAULT_TITLE, opacity=DEFAULT_OPACITY):
        """
        Constructor for the main controller
        :param root_window: The root window to be used for the view.
        """
        self.assets = None
        self.root_window = root_window
        self.title = title
        self.opacity = opacity
        self.width = None
        self.height = None
        self.start_x = None
        self.start_y = None

        # Configure the main window
        self.configure_window()

        # Fix paths and load Assets
        self.path_fix()
        self.load_assets()

        # Attach the view to the main window
        self.view = MainView(root_window, self)
        self.model = Model()

    def configure_window(self):
        """
        Configures the window for the EXIF reader app.
        :return: None
        """
        # Set appropriate height and width
        self.width = int(self.root_window.winfo_screenwidth() * self.ROOT_WINDOW_WIDTH_RATIO)
        self.height =  int(self.root_window.winfo_screenheight() * self.ROOT_WINDOW_HEIGHT_RATIO)

        self.start_x = (self.root_window.winfo_screenwidth() - self.width) // 2
        self.start_y = (self.root_window.winfo_screenheight() - self.height) // 2

        self.root_window.geometry(f"{self.width}x{self.height}+{self.start_x}+{self.start_y}")

        # For borderless window
        self.root_window.overrideredirect(self.BORDERLESS)

        # Set title
        self.root_window.title(self.title)

        # Set opacity
        self.root_window.attributes("-alpha", self.opacity)
        self.root_window.attributes("-transparentcolor", "blue")

        # Add key bind
        self.root_window.bind("<KeyRelease>", self.handle_key_release)

    def handle_key_release(self, event:Event):
        """
        Process Key inputs
        :param event: A key input, passed by the root window on key press
        :return: None
        """
        if event.keysym == 'Escape':
            self.close()

    def close(self):
        """
        Close the window and exit the program
        :return:
        """
        self.root_window.destroy()


    def load_assets(self):
        """"
            Loads images from the Assets folder as an image dictionary.
        """
        self.assets = {}
        for file in os.listdir(self.ASSETS_FOLDER):
            if "." in file:
                full_path = os.path.join(self.ASSETS_FOLDER, file)
                filename = os.path.basename(full_path)
                basename, extension = os.path.splitext(filename)
                if extension.lower() in self.VALID_EXTENSIONS:
                    image = Image.open(full_path)
                    if basename.lower() == "background":
                        image = image.resize((self.width, self.height))
                    usable_image = ImageTk.PhotoImage(image)
                    self.assets[basename.lower()] = usable_image

    @staticmethod
    def path_fix():
        """
        Fixes the assets folder path for the Main Controller
        Every other class gets their path from the Main Controller, so it all works out !!!
        :return: None
        """
        current_dir = os.getcwd()
        MainController.ASSETS_FOLDER = os.path.join(current_dir, MainController.ASSETS_FOLDER)


if __name__ == "__main__":
    app = MainController(Tk())
    app.root_window.mainloop()