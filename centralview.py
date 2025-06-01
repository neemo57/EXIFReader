import tkinter
import tkinter as tk

import os


class MainView(tk.Frame):

    def __init__(self, root_window:tk.Tk, main_controller):
        super().__init__(root_window)

        self.main_controller = main_controller
        self.root_window = root_window

        # Load the background
        self.load_background()

        # Finally, attach
        self.pack()

    def load_background(self):
        image_label = tkinter.Label(self, image=self.main_controller.assets["background"])
        image_label.pack()

    def start(self):
        self.mainloop()