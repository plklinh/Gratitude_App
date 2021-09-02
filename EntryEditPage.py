
import tkinter as tk
from tkinter import ttk
from CustomWidgets import ScrollableFrame, DisplayOnlyText
from CustomStyle import *


class EditEntryPage(ttk.Frame):
    def __init__(self, root, entry, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
