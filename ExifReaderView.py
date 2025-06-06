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

        # Create the left and right views
        self.left_view = LeftView(self, self.main_controller)
        self.right_view = RightView(self, self.main_controller)

        # Place them correctly homie
        self.left_view.place(relx=0.05, rely=0.05, relwidth=0.28, relheight=0.9)
        self.right_view.place(relx=0.35, rely=0.05, relwidth=0.6, relheight=0.9)
        
    def load_background(self):
        self.image_label = tkinter.Label(self, image=self.main_controller.assets["background"])
        self.image_label.pack()



class LeftView(Frame):

    def __init__(self, root_window:tkinter.Frame, main_controller):

        super().__init__(root_window)

        # Grab tk and main controller
        self.root_window = root_window
        self.main_controller = main_controller




class RightView(Frame):

    def __init__(self, root_window:tkinter.Frame, main_controller):

        super().__init__(root_window)

        # Grab tk and main controller
        self.root_window = root_window
        self.main_controller = main_controller