import tkinter as tk
from tkinter import ttk
from tkinter.constants import BUTT
from CustomStyle import *


class NavMenu(ttk.Frame):
    def __init__(self, parent, root, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        """Home Button"""
        self.home_button = ttk.Button(self, text="Home",
                                      command=lambda: root.switch_page(
                                          root._HomePage))
        self.home_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        """Add New Button"""
        self.entry_button = ttk.Menubutton(
            self, text="Add", style=MENUBUTTON_STYLE, direction="right")

        self.entry_button.menu = tk.Menu(self.entry_button, tearoff=0)

        self.entry_button['menu'] = self.entry_button.menu

        self.entry_button.menu.add_command(
            label="Entry", command=lambda: root.switch_page(root._AddEntryPage))

        self.entry_button.menu.add_command(
            label="Plan", command=lambda: root.switch_page(root._AddPlanPage))

        self.entry_button.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=tk.X)

        """View Previous Logs Button"""
        self.log_button = ttk.Button(self, text="Entries",
                                     command=lambda: root.switch_page(
                                         root._ViewLogsPage))
        self.log_button.pack(pady=SMALL_PAD,
                             padx=SMALL_PAD, expand=tk.YES)

        """View Previous Plans Button"""
        self.plan_button = ttk.Button(self, text="Plans",
                                      command=lambda: root.switch_page(
                                          root._PlansPage))
        self.plan_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        """Quit Button"""
        self.quit_button = ttk.Button(self, text="Quit",
                                      command=lambda: root.destroy())
        self.quit_button.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)
