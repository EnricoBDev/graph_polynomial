import tkinter as tk
from PIL import Image, ImageTk


class ConfirmFileGui(tk.Toplevel):
    def __init__(self, master, img):
        super().__init__(master=master)

        self.is_img_selected = False

        self.lift()
        self.focus_force()
        self.title("Chromatic polynomial")

        self.preview = ImageTk.PhotoImage(img)
        self.preview_lbl = tk.Label(self, image=self.preview)
        self.preview_lbl.grid(column=0, row=0, pady=(10, 0))

        # label and buttons layout
        self.text_lbl = tk.Label(self, text="Is this the graph you wanted?")
        self.text_lbl.grid(column=0, row=1, pady=10)

        self.btn_frame = tk.Frame(self, height=200, width=200)
        self.btn_frame.grid(column=0, row=2, pady=(5, 10))

        self.y_btn = tk.Button(self.btn_frame, text="Yes",
                               command=self.preview_accepted)
        self.y_btn.grid(column=0, row=0, padx=10)

        self.n_btn = tk.Button(self.btn_frame, text="No",
                               command=self.preview_declined)
        self.n_btn.grid(column=1, row=0, padx=10)

    def preview_accepted(self):
        self.is_img_selected = True
        self.destroy()

    def preview_declined(self):
        self.is_img_selected = False
        self.destroy()

    def get_selection(self):
        self.wait_window(self)
        return self.is_img_selected
