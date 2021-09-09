from tkcalendar.dateentry import DateEntry
from Controller import get_all_logs
import tkinter as tk
from tkinter import PhotoImage, ttk
from CustomWidgets import ScrollableFrame, DisplayOnlyText
from CustomStyle import *

from Pages.NavMenu import NavMenu
from Pages.EntrySingleFrame import SingleEntry


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
        Filter Row
        """
        self.side_box = ttk.Frame(self)
        self.side_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH,)

        self.filter_row = ttk.Frame(self.side_box)
        self.filter_row.pack(side=tk.TOP, fill=tk.X,
                             pady=LARGE_PAD)

        ttk.Label(self.filter_row, text="From",
                  font=SMALL_LABEL_FONT).pack(side=tk.LEFT)
        self.from_date = DateEntry(self.filter_row, width=10)
        self.from_date.pack(side=tk.LEFT)

        ttk.Label(self.filter_row, text="To",
                  font=SMALL_LABEL_FONT).pack(side=tk.LEFT)
        self.to_date = DateEntry(self.filter_row, width=10)
        self.to_date.pack(side=tk.LEFT)

        SEARCH_ICON = PhotoImage(file="Icon/funnel.png").subsample(4, 4)
        self.search_button = ttk.Button(self.filter_row,
                                        text="Search",
                                        image=SEARCH_ICON)
        self.search_button.image = SEARCH_ICON
        self.search_button.pack(side=tk.LEFT)

        """
        Form Box
        """
        self.logs_container = ScrollableFrame(self.side_box)
        self.logs_container.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        self.logs_li = self.logs_container.scrollable_frame
        self.logs_li.config(style=CONTAINER_STYLE)

        """
        List of Entries
        """

        self.current_logs = get_all_logs()

        for log in self.current_logs.itertuples():
            test_entry = SingleEntry(
                self.logs_li, root, log)
            test_entry.pack(side=tk.TOP,
                            padx=SMALL_PAD, pady=SMALL_PAD
                            )
