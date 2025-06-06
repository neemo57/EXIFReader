from ExifReaderModel import ExifReaderModel
from ExifReaderView import ExifReaderView
from MainView import MainView
from tkinter import Tk, Event
import os
from PIL import Image, ImageTk

"""
    Main controller class for the EXIFReader App.
"""

class MainController:

    # Main Window Properties
    ROOT_WINDOW_WIDTH_RATIO = .7
    ROOT_WINDOW_HEIGHT_RATIO = .7
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
        self.mouse_x = None
        self.mouse_y = None

        # Configure the main window
        self.configure_window()

        # Fix paths and load Assets
        self.path_fix()
        self.load_assets()

        # Attach the view to the main window
        self.main_view = MainView(root_window, self)
        self.reader_view = ExifReaderView(root_window, self)
        self.views = [self.main_view, self.reader_view]

        # Create the Model
        self.model = ExifReaderModel()

        # Set the default view
        self.set_view(0)

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

        self.set_geometry()

        # For borderless window
        self.root_window.overrideredirect(self.BORDERLESS)

        # Set title
        self.root_window.title(self.title)

        # Set opacity
        self.root_window.attributes("-alpha", self.opacity)
        self.root_window.attributes("-transparentcolor", "blue")

        # Add key bind
        self.root_window.bind("<KeyRelease>", self.handle_key_release)

        # Add mouse binds
        self.root_window.bind("<Motion>", self.on_mouse_move)
        self.root_window.bind("<B1-Motion>", self.on_drag)

    def set_view(self, view_index):
        """
        Sets the current view
        @:param view_index: The integer index to the view in self.views list.
        :return: None
        """
        try:
            self.views[view_index].grid(row=0, column=0, sticky="nsew")
            self.views[view_index].tkraise()
        except IndexError:
            self.main_view.show_error(f"Invalid Frame Index {view_index}. Aborting application.")

    def set_geometry(self):
        """
        Update the geometry of the root window
        :return:None
        """
        self.root_window.geometry(f"{self.width}x{self.height}+{self.start_x}+{self.start_y}")

    def handle_key_release(self, event:Event):
        """
        Process Key inputs
        :param event: A key input, passed by the root window on key press
        :return: None
        """
        if event.keysym == 'Escape':
            self.close()

    def on_mouse_move(self, event:Event):
        """
        Updates self.mouse_x and self.mouse_y on cursor movement
        :param event: The event object
        :return: None
        """
        self.mouse_x = event.x
        self.mouse_y = event.y

    def on_drag(self, event:Event):
        """
        Move window on mouse drag with left button clicked
        :param event:  Event object
        :return: None
        """
        x_offset = event.x - self.mouse_x
        y_offset = event.y - self.mouse_y

        self.start_x += x_offset
        self.start_y += y_offset
        self.set_geometry()

    def on_click_upload(self):
        """
        Handle the file upload button.
        Calls the file browser from main view
        :return: None.
        """
        self.main_view.select_file()

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
                    if "background" in basename.lower():
                        image = image.resize((self.width, self.height))
                    usable_image = ImageTk.PhotoImage(image)
                    self.assets[basename.lower()] = usable_image

    def read_image(self, image_path):
        """
        Reads metadata from an image and switches the view to MetaDataView
        :param image_path: Path to the image, chosen from MainView's file chooser
        :return: None
        """
        metadata = self.model.read_image_metadata(image_path)
        if metadata:
            self.main_view.show_info("Metadata found I guess")
            self.set_view(1)
        else:
            self.main_view.show_error("WTF Choose a good image")


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