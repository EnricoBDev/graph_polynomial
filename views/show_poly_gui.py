from io import BytesIO
import tkinter as tk
from sympy import preview
from PIL import ImageTk, Image


class ShowPolyGui(tk.Toplevel):
    def __init__(self, master, poly, img) -> None:
        super().__init__(master=master)

        self.lift()
        self.focus_force()
        self.title("Chromatic polynomial")

        self.master = master
        self.poly = poly
        self.img = img

        self.graph_lbl = tk.Label(self, image=self.img)
        self.poly_lbl = tk.Label(self)

        self.render_tex()

        self.graph_lbl.grid(row=0, column=0)
        self.poly_lbl.grid(row=1, column=0)

    def render_tex(self):
        self.file = BytesIO()

        preview(expr=self.poly, viewer="BytesIO",
                output="ps", outputbuffer=self.file)

        self.file.seek(0)

        # NOTE FOR FUTURE SELF
        # the image reference needs to be a class attribute
        # otherwise python garbage collector just deletes it

        self.poly_img = Image.open(self.file)
        self.poly_img.load(scale=5)
        self.poly_photo = ImageTk.PhotoImage(self.poly_img)

        self.file.close()

        self.poly_lbl.config(image=self.poly_photo)
