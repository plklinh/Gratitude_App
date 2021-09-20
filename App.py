"""
Icon Credit:
- Search:
<div>Icons made by <a href="https://www.flaticon.com/authors/kiranshastry" title="Kiranshastry">Kiranshastry</a>
from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

- Funnel:
<div>Icons made by <a href="" title="Kiranshastry">Kiranshastry</a>
from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

- Trash:
<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a>
from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

- Pencil:
<div>Icons made by <a href="https://www.flaticon.com/authors/those-icons" title="Those Icons">Those Icons</a>
from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

- Fullscreen:
<div>Icons made by <a href="https://www.flaticon.com/authors/vectors-market" 
title="Vectors Market">Vectors Market</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
"""

from Controller import *

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

from CustomWidgets import ScrollableFrame
from CustomStyle import *

from Pages.EntryAddPage import AddEntryPage
from Pages.EntrySingleFrame import SingleEntry, PlanFrame
from Pages.EntryEditPage import EditEntryPage
from Pages.EntriesViewPage import ViewEntriesPage
from Pages.NavMenu import NavMenu
from Pages.PlansPage import PlansPage
from Pages.PlanAddPage import AddPlanPage


class HomePage(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        latest_log = get_latest_log(test=TESTING)
        plans_df = get_latest_incomp_plans(test=TESTING)

        """
        Menu Pane
        """
        self.menu_container = NavMenu(self, root)
        self.menu_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD)

        """
        Latest Log Pane
        """
        self.logs_container = ttk.Frame(self)
        self.logs_container.pack(
            side=tk.LEFT, padx=(0, LARGE_PAD), pady=LARGE_PAD, expand=tk.YES, fill=tk.BOTH)

        self.logs_label = ttk.Label(self.logs_container,
                                    text="Latest Log", font=LARGE_LABEL_FONT)
        self.logs_label.pack()

        self.logs_scrollframe = ScrollableFrame(self.logs_container)
        self.logs_scrollframe.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=tk.BOTH)

        s = ttk.Style()
        s.configure('Frame1.TFrame', background=MAIN_BG)

        self.logs_scrollframe.scrollable_frame.config(style=CONTAINER_STYLE)

        """List of Logs"""

        self.test_entry = SingleEntry(
            self.logs_scrollframe.scrollable_frame, root,
            latest_log)
        self.test_entry.pack(side=tk.TOP,
                             padx=SMALL_PAD, pady=SMALL_PAD
                             )
        """
        Plans Pane
        """
        self.plans_container = ttk.Frame(self)
        self.plans_container.pack(
            side=tk.LEFT, padx=(0, LARGE_PAD), pady=LARGE_PAD, expand=tk.YES, fill=tk.BOTH)

        self.plans_label = ttk.Label(self.plans_container,
                                     text="Plans", font=LARGE_LABEL_FONT)
        self.plans_label.pack()

        """
        List of Plans
        """

        self.plans_scrollframe = ScrollableFrame(self.plans_container)

        self.plans_scrollframe.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=tk.BOTH)

        self.plans_scrollframe.scrollable_frame.config(style=CONTAINER_STYLE)

        for plan in plans_df.itertuples():
            plan_frame = PlanFrame(
                self.plans_scrollframe.scrollable_frame, plan, standalone=True)
            plan_frame.pack(side=tk.TOP,
                            padx=SMALL_PAD, pady=SMALL_PAD)


class GratitudeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(750, 500)
        style = ThemedStyle(self)
        style.set_theme("arc")

        s = ttk.Style()
        s.configure('Frame1.TFrame', background=MAIN_BG)
        s.configure('Combo1.TCombobox',
                    selectbackground="white",
                    selectforeground="black")
        s.configure('Menu1.TMenubutton',
                    justify=tk.CENTER,
                    anchor="center")

        self._page = None
        self._HomePage = HomePage
        self._AddEntryPage = AddEntryPage
        self._ViewLogsPage = ViewEntriesPage
        self._EditEntryPage = EditEntryPage
        self._AddPlanPage = AddPlanPage
        self._PlansPage = PlansPage
        self.switch_page(self._HomePage)

    def switch_page(self, Page, entry=None):
        if Page == self._EditEntryPage and entry is not None:
            new_page = EditEntryPage(self, entry)
        else:
            new_page = Page(self)
        if self._page is not None:
            self._page.destroy()
        self._page = new_page
        self._page.pack(padx=LARGE_PAD, pady=LARGE_PAD,
                        expand=tk.YES, fill=tk.BOTH)


app = GratitudeApp()
app.mainloop()
