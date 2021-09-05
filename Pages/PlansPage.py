from Controller import *

import tkinter as tk
from tkinter import PhotoImage, ttk
from tkcalendar import DateEntry

from CustomWidgets import ScrollableFrame
from CustomStyle import *

from Pages.NavMenu import NavMenu
from Pages.PlanSingleFrame import PlanFrame


class PlansPage(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        """
        Menu Pane
        """
        self.menu_container = NavMenu(self, root)
        self.menu_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD)

        """
        Plan filters
        """
        self.side_box = ttk.Frame(self)
        self.side_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH,)

        self.filter_row = ttk.Frame(self.side_box)
        self.filter_row.pack(side=tk.TOP, fill=tk.X,
                             pady=LARGE_PAD)

        self.status_filter_lab = ttk.Label(self.filter_row,
                                           text="Status", font=LABEL_FONT)
        self.status_filter_lab.pack(side=tk.LEFT)

        self.status_filter_menu = ttk.Combobox(
            self.filter_row,
            values=PLAN_STATUSES,
            justify=tk.CENTER, width=10, exportselection=0)
        self.status_filter_menu.current([0])
        self.status_filter_menu.state(statespec=('!disabled', 'readonly'))
        self.status_filter_menu.pack(side=tk.LEFT)

        ttk.Label(self.filter_row, text="From",
                  font=LABEL_FONT).pack(side=tk.LEFT)
        self.from_date = DateEntry(self.filter_row, width=10)
        self.from_date.pack(side=tk.LEFT)

        ttk.Label(self.filter_row, text="To",
                  font=LABEL_FONT).pack(side=tk.LEFT)
        self.to_date = DateEntry(self.filter_row, width=10)
        self.to_date.pack(side=tk.LEFT)

        SEARCH_ICON = PhotoImage(file="Icon/search.png").subsample(4, 4)
        self.search_button = ttk.Button(self.filter_row,
                                        text="Search",
                                        image=SEARCH_ICON)
        self.search_button.image = SEARCH_ICON
        self.search_button.pack(side=tk.LEFT)

        """
        List of Plans
        """

        plans_df, _ = read_all_plans()

        plans_df = plans_df.iloc[6:10]

        self.plans_scrollframe = ScrollableFrame(self.side_box)

        self.plans_scrollframe.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=tk.BOTH)

        self.plans_scrollframe.scrollable_frame.config(style="Frame1.TFrame")

        for plan in plans_df.itertuples():
            plan_frame = PlanFrame(
                self.plans_scrollframe.scrollable_frame, plan, standalone=True)
            plan_frame.pack(side=tk.TOP,
                            padx=SMALL_PAD, pady=SMALL_PAD)
