"""
Icon Credit:
<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> 
from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
"""

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

from CustomWidgets import ScrollableFrame, DisplayOnlyText
from CustomStyle import *

from EntryAddPage import AddEntryPage
from EntrySingleFrame import SingleEntry
from DraftsViewPage import ViewDraftsPage
from EntryEditPage import EditEntryPage


class HomePage(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        """
        Menu Pane
        """
        self.menu_container = ttk.Frame(self)
        self.menu_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD)

        # self.menu_label = ttk.Label(self.menu_container,
        #                             text="Menu", font=LABEL_FONT)
        # self.menu_label.pack(
        #     pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.home_button = ttk.Button(self.menu_container, text="Home",
                                      command=lambda: root.switch_page(root._HomePage))
        self.home_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.entry_button = ttk.Button(self.menu_container, text="New Entry")

        self.entry_button = ttk.Button(self.menu_container, text="New Entry",
                                       command=lambda: root.switch_page(AddEntryPage))

        self.entry_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.draft_button = ttk.Button(self.menu_container, text="Drafts",
                                       command=lambda: root.switch_page(ViewDraftsPage))
        self.draft_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.quit_button = ttk.Button(self.menu_container, text="Quit",
                                      command=lambda: root.destroy())
        self.quit_button.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        """
        Logs Pane
        """
        self.logs_container = ttk.Frame(self)
        self.logs_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD, expand=tk.YES, fill=tk.BOTH)

        self.logs_label = ttk.Label(self.logs_container,
                                    text="Previous Entries", font=LABEL_FONT)
        self.logs_label.pack()

        self.logs_scrollframe = ScrollableFrame(self.logs_container)
        self.logs_scrollframe.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=tk.BOTH)

        # Initialize style
        s = ttk.Style()
        # Create style used by default for all Frames
        s.configure('Frame1.TFrame', background=MAIN_BG)

        self.logs_scrollframe.scrollable_frame.config(style="Frame1.TFrame")

        """List of Logs"""

        self.test_entry = SingleEntry(
            self.logs_scrollframe.scrollable_frame, root,
            {'Date': '2018-09-10'},
            mode="partial")
        self.test_entry.pack(side=tk.TOP,
                             padx=SMALL_PAD, pady=SMALL_PAD
                             )

        self.test_entry_1 = SingleEntry(
            self.logs_scrollframe.scrollable_frame, root,
            {'Date': '2018-09-10'},
            mode="partial")
        self.test_entry_1.pack(side=tk.TOP,
                               padx=SMALL_PAD, pady=SMALL_PAD
                               )

        """
        Plans Pane
        """
        self.plans_container = ttk.Frame(self)
        self.plans_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD, expand=tk.YES, fill=tk.BOTH)

        self.plans_label = ttk.Label(self.plans_container,
                                     text="Plans", font=LABEL_FONT)
        self.plans_label.pack()

        self.plans_scrollframe = ScrollableFrame(self.plans_container)

        self.plans_scrollframe.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=tk.BOTH)


class GratitudeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(700, 500)
        style = ThemedStyle(self)
        style.set_theme("arc")
        self._page = None
        self._HomePage = HomePage
        self._AddEntryPage = AddEntryPage
        self._ViewDraftsPage = ViewDraftsPage
        self._EditEntryPage = EditEntryPage
        self.switch_page(self._HomePage)

    def switch_page(self, Page):
        new_page = Page(self)
        if self._page is not None:
            self._page.destroy()
        self._page = new_page
        self._page.pack(padx=LARGE_PAD, pady=LARGE_PAD,
                        expand=tk.YES, fill=tk.BOTH)


app = GratitudeApp()
app.mainloop()
