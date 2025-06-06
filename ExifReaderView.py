import tkinter
from tkinter import Frame, Label
from tkinter import Tk
from tkinter.ttk import Treeview

from PIL.ImageTk import PhotoImage


class ExifReaderView(Frame):

    DEFAULT_BACKGROUND_COLOR = "#95d3e6"

    def __init__(self, root_window:Tk, main_controller):
        super().__init__(root_window, bg=self.DEFAULT_BACKGROUND_COLOR)

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
        """
        Load the background for the current view
        :return:
        """
        self.image_label = tkinter.Label(self, image=self.main_controller.assets["background"])
        self.image_label.pack()


class LeftView(Frame):

    DEFAULT_BACKGROUND_COLOR = "#e37fd4"
    DEFAULT_IMG_VIEWER_BACKGROUND_COLOR = "#e37fd4"

    FIELD_COLUMN_WIDTH_RATIO = 0.3
    VALUE_COLUMN_WIDTH_RATIO = 0.7

    def __init__(self, root_window:tkinter.Frame, main_controller):

        super().__init__(root_window, bg=self.DEFAULT_BACKGROUND_COLOR)

        # Grab tk and main controller
        self.root_window = root_window
        self.main_controller = main_controller

        # Set up the image viewer
        self.image_viewer = None
        self.add_image_viewer()

        # Set up the general details table
        self.general_details_table = None
        self.add_general_details_table()

    def add_image_viewer(self):
        """
        Adds an image viewer on the top half
        :return:
        """
        self.image_viewer = Label(self, bg=self.DEFAULT_IMG_VIEWER_BACKGROUND_COLOR)
        self.image_viewer.place(
            relx=0.02,
            rely=0.02,
            relwidth=0.96,
            relheight=0.48)

    def add_general_details_table(self):
        """
        Adds a general details viewer for the image
        :return:
        """
        self.general_details_table = Treeview(self, columns=("Field", "Value"), show="headings")

        self.general_details_table.heading("Field", text="Field")
        self.general_details_table.heading("Value", text="Value")

        # Pack it up
        self.general_details_table.place(
            relx=0.02,
            rely=0.51,
            relwidth=0.96,
            relheight=0.48)

        # Blank row
        self.general_details_table.insert("", tkinter.END, values=("", ""))

    def set_image(self, image:PhotoImage):
        """
        Change the image of the image viewer widget
        :return:
        """
        self.image_viewer.config(image=image)
        self.image_viewer.image = image

    def add_to_table(self, data):
        """
        Adds a tuple of data into the table
        :param data: A tuple of data, has to match the number of columns in the table
        :return: None
        """
        self.general_details_table.insert("", tkinter.END, values=data)

    def clear_table(self):
        """
        Remove all the entries in the table
        :return:
        """
        for item in self.general_details_table.get_children():
            self.general_details_table.delete(item)

    def update_column_widths(self):
        """
        Update the width of the columns in the table
        :return:
        """
        # Change the column width
        self.general_details_table.column("Field", width=int(self.FIELD_COLUMN_WIDTH_RATIO * self.general_details_table.winfo_width()))
        self.general_details_table.column("Value", width=int(self.VALUE_COLUMN_WIDTH_RATIO * self.general_details_table.winfo_width()))


class RightView(Frame):

    DEFAULT_BACKGROUND_COLOR = "#fff"
    FIELD_COLUMN_WIDTH_RATIO = 0.3
    VALUE_COLUMN_WIDTH_RATIO = 0.7

    def __init__(self, root_window:tkinter.Frame, main_controller):

        super().__init__(root_window, bg=self.DEFAULT_BACKGROUND_COLOR)

        # Grab tk and main controller
        self.root_window = root_window
        self.main_controller = main_controller

        # Set up a tree view for adding the metadata
        self.table = None
        self.setup_table()

    def setup_table(self):
        """
        Sets up a table on the right view, using ttk.TreeView
        :return:
        """
        self.table = Treeview(self, columns=("Field", "Value"), show="headings")

        # Add heading labels
        self.table.heading("Field", text="Field")
        self.table.heading("Value", text="Value")

        # Pack the shit up
        self.table.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.94)

        # Add a blank row for gap
        self.add_to_table(("", ""))

        # Update the column widths
        self.update_column_widths()

    def add_to_table(self, data):
        """
        Adds a tuple of data into the table
        :param data: A tuple of data, has to match the number of columns in the table
        :return: None
        """
        self.table.insert("", tkinter.END, values=data)

    def clear_table(self):
        """
        Remove all the entries in the table
        :return:
        """
        for item in self.table.get_children():
            self.table.delete(item)

    def update_column_widths(self):
        """
        Update the width of the columns in the table
        :return:
        """
        # Change the column width
        self.table.column("Field", width=int(self.FIELD_COLUMN_WIDTH_RATIO * self.table.winfo_width()))
        self.table.column("Value", width=int(self.VALUE_COLUMN_WIDTH_RATIO * self.table.winfo_width()))
