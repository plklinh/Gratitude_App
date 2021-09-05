import tkinter as tk
from tkinter import ttk
from CustomStyle import *


class NavMenu(ttk.Frame):
    def __init__(self, parent, root, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.home_button = ttk.Button(self, text="Home",
                                      command=lambda: root.switch_page(root._HomePage))
        self.home_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.entry_button = ttk.Button(self, text="New Entry",
                                       command=lambda: root.switch_page(root._AddEntryPage))

        self.entry_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.log_button = ttk.Button(self, text="Logs",
                                     command=lambda: root.switch_page(root._ViewLogsPage))
        self.log_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.plan_button = ttk.Button(self, text="Plans",
                                      command=lambda: root.switch_page(root._PlansPage))
        self.plan_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.draft_button = ttk.Button(self, text="Drafts",
                                       command=lambda: root.switch_page(root._ViewDraftsPage))
        self.draft_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.quit_button = ttk.Button(self, text="Quit",
                                      command=lambda: root.destroy())
        self.quit_button.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)
