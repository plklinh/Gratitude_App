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
        Tab Control
        """
        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH,
                              padx=LARGE_PAD, pady=LARGE_PAD)

        self.logged_plans_side_box = ttk.Frame(self.tab_control)
        self.draft_plans_side_box = ttk.Frame(self.tab_control)

        self.tab_control.add(self.logged_plans_side_box, text="   Logs   ")
        self.tab_control.add(self.draft_plans_side_box, text="   Drafts   ")

        """
        LOGGED PLANS
        """
        plans_df = get_all_logged_plans()

        plans_df = plans_df.iloc[6:10]
        """
        Plan Filters
        """

        """
        Status filter
        """

        self.filter_row = ttk.Frame(self.logged_plans_side_box)
        self.filter_row.pack(side=tk.TOP, fill=tk.X,
                             pady=LARGE_PAD)

        self.status_filter_lab = ttk.Label(self.filter_row,
                                           text="Status  ", font=SMALL_LABEL_FONT)
        self.status_filter_lab.pack(side=tk.LEFT)

        self.status_var = tk.StringVar()

        self.status_filter_menu = ttk.Combobox(
            self.filter_row,
            textvariable=self.status_var,
            values=PLAN_STATUSES,
            state="readonly",
            style=COMBOBOX_STYLE,
            justify=tk.CENTER, width=10)
        self.status_filter_menu.pack(side=tk.LEFT, padx=(0, SMALL_PAD))

        """
        Priority Filter
        """
        self.priority_title_lab = ttk.Label(
            self.filter_row,
            text="Priority  ",
            font=SMALL_LABEL_FONT)
        self.priority_title_lab.pack(side=tk.LEFT)

        self.priority_var = tk.StringVar()
        self.priority_menu = ttk.Combobox(self.filter_row,
                                          textvariable=self.priority_var,
                                          values=PRIORITY_LVL,
                                          style=COMBOBOX_STYLE,
                                          state="readonly",
                                          justify=tk.CENTER, width=10)
        self.priority_menu.pack(side=tk.LEFT, padx=(0, SMALL_PAD))

        """
        Date Filter
        """

        ttk.Label(self.filter_row, text="From  ",
                  font=SMALL_LABEL_FONT).pack(side=tk.LEFT)
        self.from_date = DateEntry(self.filter_row, width=10)
        self.from_date.pack(side=tk.LEFT, padx=(0, SMALL_PAD))

        ttk.Label(self.filter_row, text="To  ",
                  font=SMALL_LABEL_FONT).pack(side=tk.LEFT)
        self.to_date = DateEntry(self.filter_row, width=10)
        self.to_date.pack(side=tk.LEFT, padx=(0, SMALL_PAD))

        SEARCH_ICON = PhotoImage(file="Icon/funnel.png").subsample(4, 4)
        self.search_button = ttk.Button(self.filter_row,
                                        text="Search",
                                        image=SEARCH_ICON)
        self.search_button.image = SEARCH_ICON
        self.search_button.pack(side=tk.LEFT)

        """
        List of Plans
        """

        self.plans_scrollframe = ScrollableFrame(self.logged_plans_side_box)

        self.plans_scrollframe.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=tk.BOTH)

        self.plans_scrollframe.scrollable_frame.config(style="Frame1.TFrame")

        for plan in plans_df.itertuples():
            plan_frame = PlanFrame(
                self.plans_scrollframe.scrollable_frame, plan, standalone=True)
            plan_frame.pack(side=tk.TOP,
                            padx=SMALL_PAD, pady=SMALL_PAD)

        """
        DRAFT PLANS
        """
        plans_df = get_all_draft_plans()

        """
        Plan filters
        """

        """
        Status filter
        """

        self.filter_row = ttk.Frame(self.draft_plans_side_box)
        self.filter_row.pack(side=tk.TOP, fill=tk.X,
                             pady=LARGE_PAD)

        self.status_filter_lab = ttk.Label(self.filter_row,
                                           text="Status  ", font=SMALL_LABEL_FONT)
        self.status_filter_lab.pack(side=tk.LEFT)

        self.status_var = tk.StringVar()

        self.status_filter_menu = ttk.Combobox(
            self.filter_row,
            textvariable=self.status_var,
            values=PLAN_STATUSES,
            state="readonly",
            style=COMBOBOX_STYLE,
            justify=tk.CENTER, width=10)
        self.status_filter_menu.pack(side=tk.LEFT, padx=(0, SMALL_PAD))

        """
        Priority Filter
        """
        self.priority_title_lab = ttk.Label(
            self.filter_row,
            text="Priority  ",
            font=SMALL_LABEL_FONT)
        self.priority_title_lab.pack(side=tk.LEFT)

        self.priority_var = tk.StringVar()
        self.priority_menu = ttk.Combobox(self.filter_row,
                                          textvariable=self.priority_var,
                                          values=PRIORITY_LVL,
                                          style=COMBOBOX_STYLE,
                                          state="readonly",
                                          justify=tk.CENTER, width=10)
        self.priority_menu.pack(side=tk.LEFT, padx=(0, SMALL_PAD))

        """
        Date Filter
        """

        ttk.Label(self.filter_row, text="From  ",
                  font=SMALL_LABEL_FONT).pack(side=tk.LEFT)
        self.from_date = DateEntry(self.filter_row, width=10)
        self.from_date.pack(side=tk.LEFT, padx=(0, SMALL_PAD))

        ttk.Label(self.filter_row, text="To  ",
                  font=SMALL_LABEL_FONT).pack(side=tk.LEFT)
        self.to_date = DateEntry(self.filter_row, width=10)
        self.to_date.pack(side=tk.LEFT, padx=(0, SMALL_PAD))

        SEARCH_ICON = PhotoImage(file="Icon/funnel.png").subsample(4, 4)
        self.search_button = ttk.Button(self.filter_row,
                                        text="Search",
                                        image=SEARCH_ICON)
        self.search_button.image = SEARCH_ICON
        self.search_button.pack(side=tk.LEFT)

        """
        List of Plans
        """

        self.plans_scrollframe = ScrollableFrame(self.draft_plans_side_box)

        self.plans_scrollframe.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=tk.BOTH)

        self.plans_scrollframe.scrollable_frame.config(style="Frame1.TFrame")

        for plan in plans_df.itertuples():
            plan_frame = PlanFrame(
                self.plans_scrollframe.scrollable_frame, plan, standalone=True)
            plan_frame.pack(side=tk.TOP,
                            padx=SMALL_PAD, pady=SMALL_PAD)
