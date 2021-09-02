import pandas as pd
import tkinter as tk
from tkinter import PhotoImage, ttk

from CustomWidgets import ScrollableFrame, DisplayOnlyText
from CustomStyle import *

from Controller import *


class SingleEntry(ttk.Frame):
    """
    A fame to show an entry in display-only mode

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
    toggle_display_mode()
        Toggles between full and partial view

    confirm_delete()
        Creates a pop up window to confirm deletion
    """

    def __init__(self, parent, root, entry, mode="full", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        pencil_icon = PhotoImage(file="Icon/pencil.png").subsample(4, 4)
        trash_icon = PhotoImage(file="Icon/trash.png").subsample(4, 4)
        eye_icon = PhotoImage(file="Icon/eye.png").subsample(4, 4)

        """
        Date
        """
        if entry['Entry_Type'] == "Draft":
            self.draft_row = ttk.Frame(self)
            self.draft_row.pack(padx=SMALL_PAD, pady=SMALL_PAD)
            self.draft_lab = ttk.Label(
                self.draft_row,
                text="Draft",
                font=LABEL_FONT)
            self.draft_lab.pack()

        self.date_row = ttk.Frame(self)
        self.date_row.pack(side=tk.TOP, fill=tk.X,
                           padx=SMALL_PAD, pady=SMALL_PAD)

        self.date_lab = ttk.Label(
            self.date_row,
            text="Date: ",
            font=LABEL_FONT)
        self.date_lab.pack(side=tk.LEFT, anchor='nw')

        self.date_lab = ttk.Label(
            self.date_row,
            text=entry['Date'].strftime("%Y-%m-%d"))
        self.date_lab.pack(side=tk.LEFT, anchor='nw')

        """
        Gratitude
        """
        self.gratitude_lab = ttk.Label(
            self, width=20,
            text="Things I'm grateful for:",
            font=LABEL_FONT,
            anchor='nw')
        self.gratitude_lab.pack(side=tk.TOP, anchor='nw',
                                padx=SMALL_PAD, pady=SMALL_PAD)

        self.gratitude_entry = DisplayOnlyText(
            self)
        self.gratitude_entry.pack(
            side=tk.TOP, expand=True, fill=tk.X,
            padx=SMALL_PAD, pady=SMALL_PAD)

        self.gratitude_entry.configure(state='normal')

        for i in range(len(entry["Gratitude"])):
            txt = '• '+entry["Gratitude"][i] + "\n"
            if i == len(entry["Gratitude"])-1:
                txt = '• '+entry["Gratitude"][i]
            self.gratitude_entry.insert(
                'end', txt)

        self.gratitude_entry.configure(state='disabled')

        """
        Goals
        """

        self.goals_lab = ttk.Label(
            self, width=20,
            text="Goals: ",
            font=LABEL_FONT,
            anchor='nw')
        self.goals_lab.pack(side=tk.TOP, anchor='nw',
                            padx=SMALL_PAD, pady=SMALL_PAD)

        self.goals_entry = DisplayOnlyText(
            self, height=len(entry["Goals"]))
        self.goals_entry.pack(
            side=tk.TOP, expand=True, fill=tk.X,
            padx=SMALL_PAD, pady=SMALL_PAD)

        self.goals_entry.configure(state='normal')

        for i in range(len(entry["Goals"])):
            txt = '• '+entry["Goals"][i] + "\n"
            if i == len(entry["Goals"])-1:
                txt = '• '+entry["Goals"][i]
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
            font=LABEL_FONT,
            anchor='nw')
        plans_lab.pack(side=tk.TOP, anchor='nw',
                       padx=SMALL_PAD, pady=SMALL_PAD)

        plans_container = ttk.Frame(self)
        plans_container.pack(side=tk.TOP, fill=tk.X, anchor='nw')

        plans_df = match_plans(entry)

        for plan in plans_df.itertuples():
            plan_row = PlanFrame(plans_container, plan)
            plan_row.pack(fill=tk.X, padx=SMALL_PAD, pady=SMALL_PAD)

        """
        Affirmation Row
        """

        self.affirm_lab = ttk.Label(
            self, width=20,
            text="Affirmation: ",
            font=LABEL_FONT,
            anchor='nw')
        self.affirm_lab.pack(side=tk.TOP, anchor='nw',
                             padx=SMALL_PAD, pady=SMALL_PAD)

        self.affirm_entry = DisplayOnlyText(self)

        self.affirm_entry.pack(
            side=tk.TOP, anchor='nw',
            padx=SMALL_PAD, pady=SMALL_PAD)

        self.affirm_entry.insert(
            'end', entry["Affirmation"])

        self.affirm_entry.configure(state='disabled')

        """
        Note
        """
        if entry["Additional_Notes"] is not None:
            self.notes_lab = ttk.Label(
                self, width=20,
                text="Additional Notes: ",
                font=LABEL_FONT,
                anchor='w')
            self.notes_lab.pack(side=tk.TOP, anchor='nw',
                                padx=SMALL_PAD, pady=SMALL_PAD)

            self.notes_entry = DisplayOnlyText(self, height=2)

            self.notes_entry.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, anchor='nw',
                                  padx=SMALL_PAD, pady=SMALL_PAD)
        """
        Button Options
        """
        self.options_row = ttk.Frame(self)
        self.options_row.pack(side=tk.TOP,
                              padx=SMALL_PAD, pady=SMALL_PAD)

        if mode == "partial":
            self.full_view_button = ttk.Button(
                self.options_row, text="Full View",
                image=eye_icon)
            self.full_view_button.image = eye_icon
            self.full_view_button.pack(side=tk.LEFT)

        self.edit_button = ttk.Button(self.options_row,
                                      text="Edit",
                                      image=pencil_icon,
                                      command=lambda: root.switch_page(root._EditEntryPage, entry=entry))
        self.edit_button.image = pencil_icon
        self.edit_button.pack(side=tk.LEFT)

        self.delete_button = ttk.Button(self.options_row,
                                        text="Delete",
                                        image=trash_icon)
        self.delete_button.image = trash_icon
        self.delete_button.pack(side=tk.LEFT)

    def toggle_display_mode(self):
        pass

    def confirm_delete(self):
        pass


class PlanFrame(ttk.Frame):

    def __init__(self, parent, plan, mode="full", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.desc_row = ttk.Frame(self)
        self.desc_row.pack(fill=tk.X)

        self.desc_lab = ttk.Label(self.desc_row, text=plan.Description)
        self.desc_lab.pack(side=tk.LEFT, anchor="nw")

        self.status_lab = tk.Label(
            self.desc_row, text=plan.Status, font=ANNOTATE_FONT)
        self.status_lab.pack(side=tk.LEFT, padx=SMALL_PAD, anchor="nw")

        font_col = INCOMP_COLOR
        if plan.Status == "Completed":
            font_col = COMP_COLOR
        elif plan.Status == "Scrapped":
            font_col = SCRAP_COLOR

        self.status_lab.config(fg=font_col)
        """
        Steps
        """
        if mode == "full":
            steps = match_steps(plan)
            if steps is not None:
                steps_container = ttk.Frame(self)
                steps_container.pack(pady=SMALL_PAD)
                steps_container.pack()
                for step in steps.itertuples():
                    step_row = ttk.Frame(steps_container)
                    step_row.pack(side=tk.TOP)
                    if step.Status == "Completed":
                        step_stat = tk.Label(
                            step_row, text="v", font=ANNOTATE_FONT)
                        step_stat.config(fg=COMP_COLOR)
                        step_stat.pack(side=tk.LEFT)
                    else:
                        step_stat = tk.Label(
                            step_row, text=" ", font=ANNOTATE_FONT)
                        step_stat.pack(side=tk.LEFT)
                    step_desc = DisplayOnlyText(step_row)
                    step_desc.insert("end", step.Description)
                    step_desc.configure(state='disabled')
                    step_desc.pack(side=tk.LEFT)
