"""
Credit: 
https://blog.teclado.com/tkinter-scrollable-frames/
https://stackoverflow.com/questions/16820520/tkinter-canvas-create-window
https://stackoverflow.com/questions/46081798/automatically-resize-text-widgets-height-to-fit-all-text
"""
import tkinter as tk
from tkinter import ttk
from CustomStyle import *


class ScrollableText(tk.Text):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.config(font=("TkDefaultFont", 13),
                    foreground=MID_BG,
                    highlightcolor=HIGHLIGHT_BG,
                    highlightthickness=1
                    )

        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.yview)
        self.scrollbar.pack(side="right", fill="y")
        self['yscrollcommand'] = self.scrollbar.set


class DisplayOnlyText(tk.Text):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(background=TEXT_BG,
                    foreground=MID_BG,
                    highlightcolor=HIGHLIGHT_BG,
                    highlightthickness=1
                    )
        self.bind("<Configure>", self.reset_height)

    def reset_height(self, e):
        height = self.tk.call(
            (self._w, "count", "-update", "-displaylines", "1.0", "end"))
        self.configure(height=height)


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
