from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import networkx as nx
import matplotlib.pyplot as plt

from graph_parser import get_matrix


class Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Chromatic polynomial")

        icon = ImageTk.PhotoImage(Image.open("assets/logo.ico"))
        self.root.wm_iconphoto(True, icon)

        self.label = tk.Label(root, text="Calculate chromatic polynomial")
        self.button = tk.Button(
            root, text="Select file", command=self.open_file)
        self.center_widgets()

        self.root.bind("<Return>", self.open_file)

    def center_widgets(self):
        self.root.update_idletasks()  # necessary to get width of widgets
        label_center_padding = (self.root.winfo_width() -
                                self.label.winfo_width()) / 2
        self.label.grid(row=0, column=0, padx=label_center_padding, pady=20)

        button_center_padding = (
            self.root.winfo_width() - self.label.winfo_width()) / 2
        self.button.grid(row=1, column=0, padx=button_center_padding, pady=20)

    def open_file(self, event):
        filetypes = (("XGml file", "*.xgml"), ("All files", "*.*"))
        filename_path = filedialog.askopenfilename(
            initialdir=Path.cwd(),
            title="Choose an xgml file",
            filetypes=filetypes)

        graph = nx.from_numpy_array(get_matrix(filename=filename_path))

        nx.draw_spring(G=graph)
        plt.show()
