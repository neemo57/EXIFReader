import tkinter
from tkinter import Frame
from tkinter import Tk

class ExifReaderView(Frame):

    def __init__(self, root_window:Tk, main_controller):
        super().__init__(root_window)

        # Grab tk and main controller
        self.root_window = root_window
        self.main_controller = main_controller

        # Load the background
        self.image_label = None
        self.load_background()
        
    def load_background(self):
        self.image_label = tkinter.Label(self, image=self.main_controller.assets["background"])
        self.image_label.pack()

