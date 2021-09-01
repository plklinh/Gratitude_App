import tkinter as tk
from tkinter import ttk
from CustomWidgets import ScrollableFrame, DisplayOnlyText
from CustomStyle import *
from EntrySingleFrame import SingleEntry


class ViewDraftsPage(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        """
        Menu Pane
        """
        self.menu_container = ttk.Frame(self)
        self.menu_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD)

        self.home_button = ttk.Button(self.menu_container, text="Home",
                                      command=lambda: root.switch_page(root._HomePage))
        self.home_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.entry_button = ttk.Button(self.menu_container, text="New Entry",
                                       command=lambda: root.switch_page(root._AddEntryPage))

        self.entry_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.draft_button = ttk.Button(self.menu_container, text="Drafts",
                                       command=lambda: root.switch_page(ViewDraftsPage))
        self.draft_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.quit_button = ttk.Button(self.menu_container, text="Quit",
                                      command=lambda: root.destroy())
        self.quit_button.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

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
            self.draft_li, root, {'Date': '2018-09-10'})
        self.test_entry.pack(side=tk.TOP,
                             padx=SMALL_PAD, pady=SMALL_PAD
                             )

        self.test_entry_1 = SingleEntry(
            self.draft_li, root, {'Date': '2018-09-10'})
        self.test_entry_1.pack(side=tk.TOP,
                               padx=SMALL_PAD, pady=SMALL_PAD
                               )
