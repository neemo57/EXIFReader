from model import Model
from view import View
from tkinter import Tk

"""
    Main controller class for the EXIFReader App.
"""

class MainController:

    ROOT_WINDOW_WIDTH_RATIO = 0.6
    ROOT_WINDOW_HEIGHT_RATIO = 0.6
    BORDERLESS = True
    DEFAULT_TITLE = "EXIF Reader v1.1.0"
    DEFAULT_OPACITY = 0.9

    def __init__(self, root_window:Tk, title=DEFAULT_TITLE, opacity=DEFAULT_OPACITY):
        """
        Constructor for the main controller
        :param root_window: The root window to be used for the view.
        """
        self.root_window = root_window
        self.title = title
        self.opacity = opacity

        self.view = View()
        self.model = Model()

        self.configure_window()

    def configure_window(self):
        """
        Configures the window for the EXIF reader app.
        :return: None
        """
        # Set appropriate height and width
        width = int(self.root_window.winfo_screenwidth() * self.ROOT_WINDOW_WIDTH_RATIO)
        height =  int(self.root_window.winfo_screenheight() * self.ROOT_WINDOW_HEIGHT_RATIO)

        start_x = (self.root_window.winfo_screenwidth() - width) // 2
        start_y = (self.root_window.winfo_screenheight() - height) // 2

        self.root_window.geometry(f"{width}x{height}+{start_x}+{start_y}")

        # For borderless window
        self.root_window.overrideredirect(self.BORDERLESS)

        # Set title
        self.root_window.title(self.title)

        # Set opacity
        self.root_window.attributes("-alpha", self.opacity)


    def start(self):
        self.view.start()

if __name__ == "__main__":
    app = MainController(Tk())
    app.root_window.mainloop()