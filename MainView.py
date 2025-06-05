import tkinter
import tkinter as tk
from tkinter import Button, filedialog, messagebox


class MainView(tk.Frame):

    DEFAULT_BUTTON_TEXT = "Click here to upload a file.\n Or press CTRL + V"
    BUTTON_REL_WIDTH = 0.2
    BUTTON_REL_HEIGHT = 0.1
    BUTTON_DEF_BACKGROUND = "purple"
    BUTTON_DEF_FOREGROUND = "yellow"

    BUTTON_SECONDARY_BACKGROUND = "black"
    BUTTON_SECONDARY_FOREGROUND = "white"

    DEFAULT_ERROR_TITLE = "Error"
    DEFAULT_NO_FILE_WARNING = "Failed to select a file. Please try again or use Ctrl + V "
    DEFAULT_INFO_TITLE = "Info"

    def __init__(self, root_window:tk.Tk, main_controller):
        super().__init__(root_window)

        self.main_controller = main_controller
        self.root_window = root_window

        # Load the background
        self.image_label = None
        self.load_background()

        # Add the button
        self.choose_file_button = None
        self.add_button()

    def load_background(self):
        self.image_label = tkinter.Label(self, image=self.main_controller.assets["background"])
        self.image_label.pack()

    def add_button(self):
        """
        Adds a button which calls the file browser
        :return:
        """
        self.choose_file_button = Button(self, text=self.DEFAULT_BUTTON_TEXT, bg=self.BUTTON_DEF_BACKGROUND, fg=self.BUTTON_DEF_FOREGROUND, command=self.main_controller.on_click_upload)
        precise_width = self.BUTTON_REL_WIDTH * self.main_controller.width
        precise_height = self.BUTTON_REL_HEIGHT * self.main_controller.height
        precise_x = (self.main_controller.width / 2) - (precise_width / 2)
        precise_y = (self.main_controller.height / 2) - (precise_height / 2)

        self.choose_file_button.place(x=int(precise_x), y=int(precise_y), width=int(precise_width), height=int(precise_height))

        # Bind with on_hover and on_unhover functions
        self.choose_file_button.bind("<Enter>", self.on_button_hover)
        self.choose_file_button.bind("<Leave>", self.on_button_unhover)

    def on_button_hover(self, event):
        """
        Change the button's background on hover // enter
        :return:
        """
        self.choose_file_button.config(bg=self.BUTTON_SECONDARY_BACKGROUND, fg=self.BUTTON_SECONDARY_FOREGROUND)

    def on_button_unhover(self, event):
        """
        Change the button's background on hover // enter
        :return:
        """
        self.choose_file_button.config(bg=self.BUTTON_DEF_BACKGROUND, fg=self.BUTTON_DEF_FOREGROUND)

    def select_file(self):
        """
        Choose an image file for processing.
        :return: Image path if valid image selected, None otherwise.
        """
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp *.avif"), ("All files", "*.*")]
        )
        if file_path:
            self.main_controller.read_image(file_path)
        else:
            self.show_error(self.DEFAULT_NO_FILE_WARNING)

    @staticmethod
    def show_error(msg, title=DEFAULT_ERROR_TITLE):
        """
        One method to show all the errors
        :return:
        """
        messagebox.showerror(title, msg)

    @staticmethod
    def show_info(msg, title=DEFAULT_INFO_TITLE):
        """
        One method to show all the infos
        :return:
        """
        messagebox.showinfo(title, msg)


    def start(self):
        self.mainloop()