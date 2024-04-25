import io
from pathlib import Path
import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import networkx as nx  # type: ignore
import matplotlib.pyplot as plt

from graph_parser import get_matrix  # type: ignore

from views.confirm_file_gui import ConfirmFileGui  # type: ignore
from model.chromatic_poly_alg import ChromaticPolyAlg


class InputGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Chromatic polynomial")

        self.is_img_selected = False

        icon = ImageTk.PhotoImage(Image.open("assets/logo.ico"))
        self.root.wm_iconphoto(True, icon)

        self.label = tk.Label(root, text="Calculate chromatic polynomial")
        self.button = tk.Button(
            root, text="Select file", command=self.open_file)
        self.center_widgets()

        self.root.bind("<Return>", self.open_file_bind)

    def center_widgets(self):
        self.root.update_idletasks()  # necessary to get width of widgets
        label_center_padding = (self.root.winfo_width() -
                                self.label.winfo_width()) / 2
        self.label.grid(row=0, column=0, padx=label_center_padding, pady=20)

        button_center_padding = (
            self.root.winfo_width() - self.label.winfo_width()) / 2
        self.button.grid(row=1, column=0, padx=button_center_padding, pady=20)

    def open_file_bind(self, event):
        self.open_file()

    def open_file(self):
        filetypes = (("XGml file", "*.xgml"), ("All files", "*.*"))
        filename_path = filedialog.askopenfilename(
            initialdir=Path.cwd(),
            title="Choose an xgml file",
            filetypes=filetypes)

        if filename_path:
            graph = nx.from_numpy_array(get_matrix(filename=filename_path))

            img_io = io.BytesIO()  # a binary stream where the image will be saved
            # creates a matplotlib Axes object used to store the graph drawing
            fig, ax = plt.subplots()

            nx.draw(G=graph, ax=ax, pos=nx.spring_layout(graph))

            fig.savefig(img_io, format="png")
            img = Image.open(img_io)

            confirmation_popup = ConfirmFileGui(master=self.root, img=img)
            print(confirmation_popup.get_selection())

            ###
            # after that we need to call a func/method that calculates the polynomial
            # and then we show that in another window, while this one is (destroyed ?)
            ###

            poly = ChromaticPolyAlg.calculate_poly(graph)
