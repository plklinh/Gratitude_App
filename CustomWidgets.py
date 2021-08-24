"""
Credit: 
https://blog.teclado.com/tkinter-scrollable-frames/
https://stackoverflow.com/questions/16820520/tkinter-canvas-create-window
"""
import tkinter as tk
from tkinter import ttk


class ScrollableText(tk.Text):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.config(font=("TkDefaultFont", 13),
                    foreground="#5c616c",
                    highlightcolor="#5294e2",
                    highlightthickness=1
                    )

        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.yview)
        self.scrollbar.pack(side="right", fill="y")
        self['yscrollcommand'] = self.scrollbar.set


class DisplayOnlyText(tk.Text):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(background="#f2f4f5",
                    foreground="#5c616c",
                    highlightcolor="#5294e2",
                    highlightthickness=1
                    )


class ScrollableFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        self.canvas.configure(highlightthickness=0)
        self.canvas.pack(side="left", fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y",)

        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.interior = self.canvas.create_window(
            (10, 10), window=self.scrollable_frame, anchor="nw", tags="_frame")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.resize_frame)

    def resize_frame(self, e):
        self.canvas.itemconfig(self.interior,
                               width=self.canvas.winfo_width()-20)
