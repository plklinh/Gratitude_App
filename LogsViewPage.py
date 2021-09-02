import tkinter as tk
from tkinter import ttk
from CustomWidgets import ScrollableFrame, DisplayOnlyText
from CustomStyle import *

from NavMenu import NavMenu
from EntrySingleFrame import SingleEntry


class ViewLogsPage(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        """
        Menu Pane
        """
        self.menu_container = NavMenu(self, root)
        self.menu_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD)

        """
        Form Box
        """
        self.drafts_container = ScrollableFrame(self)
        self.drafts_container.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        self.draft_li = self.drafts_container.scrollable_frame
        s = ttk.Style()
        s.configure('Frame1.TFrame', background=MAIN_BG)
        self.draft_li.config(style="Frame1.TFrame")

        """
        List of Entries
        """
        self.test_entry = SingleEntry(
            self.draft_li, root, MOCK_ENTRY)
        self.test_entry.pack(side=tk.TOP,
                             padx=SMALL_PAD, pady=SMALL_PAD
                             )

        self.test_entry_1 = SingleEntry(
            self.draft_li, root, MOCK_ENTRY)
        self.test_entry_1.pack(side=tk.TOP,
                               padx=SMALL_PAD, pady=SMALL_PAD
                               )
