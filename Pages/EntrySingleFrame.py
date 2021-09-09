from Controller import *

import tkinter as tk
from tkinter import PhotoImage, ttk

from CustomWidgets import DisplayOnlyText
from CustomStyle import *
from Pages.PlanSingleFrame import PlanFrame


class SingleEntry(ttk.Frame):
    """
    A frame to show an entry in display-only mode

    ...

    Attributes
    ----------
    parent : tk.Frame
        the container of the Frame
    root : tk.Tk
        the root Tk application
    entry : pandas.DataFrame
        the data to be displayed
    mode : str
        whether to show steps in plans ("full") or not ("partial") (default full)

    Methods
    -------
    confirm_delete()
        Creates a pop up window to confirm deletion
    """

    def __init__(self, parent, root, entry, mode="full", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        PENCIL_ICON = PhotoImage(file="Icon/pencil.png").subsample(4, 4)
        TRASH_ICON = PhotoImage(file="Icon/trash.png").subsample(4, 4)
        #EYE_ICON = PhotoImage(file="Icon/eye.png").subsample(4, 4)

        """
        Date
        """
        if entry.Entry_Type == "Draft":
            self.draft_row = ttk.Frame(self)
            self.draft_row.pack(padx=SMALL_PAD, pady=SMALL_PAD)
            self.draft_lab = ttk.Label(
                self.draft_row,
                text="Draft",
                font=SMALL_LABEL_FONT)
            self.draft_lab.pack()

        self.date_row = ttk.Frame(self)
        self.date_row.pack(side=tk.TOP, fill=tk.X,
                           padx=SMALL_PAD, pady=SMALL_PAD)

        self.date_lab = ttk.Label(
            self.date_row,
            text="Date: ",
            font=SMALL_LABEL_FONT)
        self.date_lab.pack(side=tk.LEFT, anchor='nw')

        self.date_lab = ttk.Label(
            self.date_row,
            text=entry.Date.strftime("%Y-%m-%d"))
        self.date_lab.pack(side=tk.LEFT, anchor='nw')

        """
        Gratitude
        """
        self.gratitude_lab = ttk.Label(
            self, width=20,
            text="Things I'm grateful for:",
            font=SMALL_LABEL_FONT,
            anchor='nw')
        self.gratitude_lab.pack(side=tk.TOP, anchor='nw',
                                padx=SMALL_PAD, pady=SMALL_PAD)

        if len(entry.Gratitude) > 0:
            self.gratitude_entry = DisplayOnlyText(
                self)
            self.gratitude_entry.pack(
                side=tk.TOP, expand=True, fill=tk.X,
                padx=LARGE_PAD, pady=SMALL_PAD)

            self.gratitude_entry.configure(state='normal')

            for i in range(len(entry.Gratitude)):
                txt = '•    '+entry.Gratitude[i] + "\n"
                if i == len(entry.Gratitude)-1:
                    txt = '•    '+entry.Gratitude[i]
                self.gratitude_entry.insert(
                    'end', txt)

            self.gratitude_entry.configure(state='disabled')

        """
        Goals
        """

        self.goals_lab = ttk.Label(
            self, width=20,
            text="Goals: ",
            font=SMALL_LABEL_FONT,
            anchor='nw')
        self.goals_lab.pack(side=tk.TOP, anchor='nw',
                            padx=SMALL_PAD, pady=SMALL_PAD)

        if len(entry.Goals) > 0:
            self.goals_entry = DisplayOnlyText(
                self, height=len(entry.Goals))
            self.goals_entry.pack(
                side=tk.TOP, expand=True, fill=tk.X,
                padx=LARGE_PAD, pady=SMALL_PAD)

            self.goals_entry.configure(state='normal')

            for i in range(len(entry.Goals)):
                txt = '•    '+entry.Goals[i] + "\n"
                if i == len(entry.Goals)-1:
                    txt = '•    '+entry.Goals[i]
                self.goals_entry.insert(
                    'end', txt)

            self.goals_entry.configure(state='disabled')

        """
        Plans Row
        """
        plans_lab = ttk.Label(
            self,
            width=20,
            text="Plans: ",
            font=SMALL_LABEL_FONT,
            anchor='nw')
        plans_lab.pack(side=tk.TOP, anchor='nw',
                       padx=SMALL_PAD, pady=SMALL_PAD)

        plans_container = ttk.Frame(self)
        plans_container.pack(side=tk.TOP, fill=tk.X, anchor='nw')

        plans_df = match_plans(entry)

        if plans_df is not None:
            for plan in plans_df.itertuples():
                plan_row = PlanFrame(plans_container, plan)
                plan_row.pack(pady=(0, SMALL_PAD))

        """
        Affirmation Row
        """

        self.affirm_lab = ttk.Label(
            self, width=20,
            text="Affirmation: ",
            font=SMALL_LABEL_FONT,
            anchor='nw')
        self.affirm_lab.pack(side=tk.TOP, anchor='nw',
                             padx=SMALL_PAD, pady=SMALL_PAD)

        if entry.Affirmation is not None:
            self.affirm_entry = DisplayOnlyText(self)
            self.affirm_entry.insert(
                'end', entry.Affirmation)
            self.affirm_entry.configure(state='disabled')

        """
        Note
        """
        if entry.Additional_Notes is not None:
            self.notes_lab = ttk.Label(
                self, width=20,
                text="Additional Notes: ",
                font=SMALL_LABEL_FONT,
                anchor='w')
            self.notes_lab.pack(side=tk.TOP, anchor='nw',
                                padx=SMALL_PAD, pady=SMALL_PAD)

            self.notes_entry = DisplayOnlyText(self, height=2)

            self.notes_entry.insert('end', entry.Additional_Notes)

            self.notes_entry.configure(state='disabled')

            self.notes_entry.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, anchor='nw',
                                  padx=LARGE_PAD, pady=SMALL_PAD)
        """
        Button Options
        """
        self.options_row = ttk.Frame(self)
        self.options_row.pack(side=tk.TOP,
                              padx=SMALL_PAD, pady=SMALL_PAD)

        self.edit_button = ttk.Button(self.options_row,
                                      text="Edit",
                                      image=PENCIL_ICON,
                                      command=lambda: root.switch_page(root._EditEntryPage, entry=entry))
        self.edit_button.image = PENCIL_ICON
        self.edit_button.pack(side=tk.LEFT)

        self.delete_button = ttk.Button(self.options_row,
                                        text="Delete",
                                        image=TRASH_ICON)
        self.delete_button.image = TRASH_ICON
        self.delete_button.pack(side=tk.LEFT)

    def confirm_delete(self):
        pass
