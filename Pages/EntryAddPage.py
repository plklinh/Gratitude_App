import pandas as pd
from Controller import *

import tkinter as tk
from tkinter import ttk

from CustomWidgets import ScrollableText, ScrollableFrame
from CustomStyle import *


class AddEntryPage(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        """
        Menu Pane
        """
        self.menu_container = ttk.Frame(self)
        self.menu_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD)

        self.menu_label = ttk.Label(self.menu_container,
                                    text="Home", font=LABEL_FONT)
        self.menu_label.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.quit_button = ttk.Button(self.menu_container, text="Back",
                                      command=lambda: root.switch_page(root._HomePage))
        self.quit_button.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.log_button = ttk.Button(self.menu_container, text="Save",
                                     command=lambda: root.switch_page(root._HomePage))

        self.log_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.draft_button = ttk.Button(self.menu_container, text="Save as Draft",
                                       command=lambda: root.switch_page(root._HomePage))
        self.draft_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        """
        Form Box
        """
        self.form_container = ScrollableFrame(self)
        self.form_container.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)

        self.form = self.form_container.scrollable_frame

        """
        Gratitude Row
        """

        self.gratitude_row = ttk.Frame(self.form)
        self.gratitude_row.pack(side=tk.TOP, fill=tk.X, expand=tk.YES,
                                padx=LARGE_PAD, pady=LARGE_PAD)

        self.gratitude_lab = ttk.Label(
            self.gratitude_row, width=20,
            text="Things I'm grateful for: ",
            font=LABEL_FONT,
            anchor='nw')
        self.gratitude_lab.pack(side=tk.LEFT)

        self.gratitude_entry_container = ttk.Frame(self.gratitude_row)
        self.gratitude_entry_container.pack(expand=tk.YES, fill=tk.X,
                                            side=tk.LEFT)

        self.grat_entry_li = []

        self.add_input_item(self.gratitude_entry_container, self.grat_entry_li)

        """
        Goals Row
        """
        self.goals_row = ttk.Frame(self.form)
        self.goals_row.pack(expand=tk.YES,
                            side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.goals_lab = ttk.Label(
            self.goals_row, width=20,
            text="Goals: ",
            font=LABEL_FONT,
            anchor='nw')
        self.goals_lab.pack(side=tk.LEFT)

        self.goals_entry_container = ttk.Frame(self.goals_row)
        self.goals_entry_container.pack(
            side=tk.LEFT, expand=tk.YES, fill=tk.X)

        self.goals_entry_li = []
        self.add_input_item(self.goals_entry_container, self.goals_entry_li)

        """
        Plans Row
        """
        self.plans_row = ttk.Frame(self.form)
        self.plans_row.pack(expand=tk.YES,
                            side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.plans_lab = ttk.Label(
            self.plans_row, width=20,
            text="Plans: ",
            font=LABEL_FONT,
            anchor='nw')
        self.plans_lab.pack(side=tk.LEFT)

        # plans_entry = ttk.Entry(self.plans_row)
        # plans_entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

        self.plans_container = ttk.Frame(self.plans_row)
        self.plans_container.pack(
            side=tk.LEFT, expand=tk.YES, fill=tk.X)

        self.plans_entry_container = ttk.Frame(self.plans_container)
        self.plans_entry_container.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X)

        self.plans_entry_li = []
        self.add_plan_item(self.plans_entry_container, self.plans_entry_li)

        self.plans_button = ttk.Button(
            self.plans_container, text="Add Plan",
            command=lambda: self.add_plan_item(self.plans_entry_container, self.plans_entry_li))
        self.plans_button.pack(side=tk.TOP)

        """
        Affirmation Row
        """
        self.affirm_row = ttk.Frame(self.form)
        self.affirm_row.pack(expand=tk.YES,
                             side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.affirm_lab = ttk.Label(
            self.affirm_row, width=20,
            text="Affirmation: ",
            font=LABEL_FONT,
            anchor='nw')
        self.affirm_lab.pack(side=tk.LEFT)

        self.affirm_entry = ScrollableText(
            self.affirm_row, height=10, width=50)
        self.affirm_entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X,
                               ipadx=10, ipady=10)

        """
        Note Row
        """
        self.notes_row = ttk.Frame(self.form)
        self.notes_row.pack(expand=tk.YES,
                            side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.notes_lab = ttk.Label(
            self.notes_row, width=20,
            text="Additional Notes: ",
            font=LABEL_FONT,
            anchor='w')
        self.notes_lab.pack(side=tk.LEFT)

        self.notes_entry = ScrollableText(self.notes_row, height=10, width=50)

        self.notes_entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X,
                              ipadx=10, ipady=10)

    def add_input_item(self, entry_container, entry_li):
        new_entry_frame = ttk.Frame(entry_container)
        new_entry_frame.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X)

        """Entry Box"""
        new_entry_box = ttk.Entry(new_entry_frame)
        new_entry_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        entry_li.append(new_entry_box)

        """Add Button"""
        def add_function(): return self.add_input_item(entry_container, entry_li)
        new_button_add_new = ttk.Button(
            new_entry_frame, text="+",
            command=add_function)
        new_button_add_new.pack(side=tk.LEFT)
        new_button_add_new.config(width=SMALL_BUTTON_WIDTH)

        """Delete Button"""
        def delete_function(): return self.delete_item(
            new_entry_box, entry_li, entry_container)
        new_delete_button = ttk.Button(
            new_entry_frame, text="-", command=delete_function)
        new_delete_button.pack(side=tk.LEFT)
        new_delete_button.config(width=SMALL_BUTTON_WIDTH)

    def add_plan_item(self, plan_container, plan_li):
        new_plan_frame = ttk.Frame(plan_container)
        new_steps_li = []
        new_plan_frame.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)

        description_row = ttk.Frame(new_plan_frame)
        description_row.pack(expand=tk.YES, fill=tk.X)

        steps_row = ttk.Frame(new_plan_frame)
        steps_row.pack(fill=tk.X)

        empty_widget = ttk.Frame(steps_row)
        empty_widget.pack()

        """Description Entry Box"""
        new_plan_box = ttk.Entry(description_row)
        new_plan_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

        full_plan_entry = {"Plan": new_plan_box, "Steps": new_steps_li}
        plan_li.append(full_plan_entry)

        """Add Button"""
        new_button_add_new = ttk.Button(
            description_row, text="+ steps",
            command=lambda: self.add_step_item(steps_row, new_steps_li))
        new_button_add_new.pack(side=tk.LEFT)

        """Delete Button"""
        new_delete_button = ttk.Button(
            description_row, text="-",
            command=lambda: self.delete_item(full_plan_entry, plan_li,
                                             plan_container, item_type="plan"))
        new_delete_button.pack(side=tk.LEFT)
        new_delete_button.config(width=SMALL_BUTTON_WIDTH)

    def add_step_item(self, steps_container, steps_li):
        new_step_row = ttk.Frame(steps_container)
        new_step_row.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X)
        steps_li.append(new_step_row)

        check_var = tk.StringVar()
        new_step_checkb = ttk.Checkbutton(
            new_step_row, variable=check_var,
            onvalue="Completed", offvalue="Incomplete")

        new_step_checkb.pack(side=tk.LEFT)

        new_step_box = ttk.Entry(new_step_row)
        new_step_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        steps_li.append(new_step_box)

        """Add Button"""

        new_button_add_new = ttk.Button(
            new_step_row, text="+",
            command=lambda: self.add_step_item(steps_container, steps_li))
        new_button_add_new.pack(side=tk.LEFT)
        new_button_add_new.config(width=SMALL_BUTTON_WIDTH)

        """Delete Button"""
        new_delete_button = ttk.Button(
            new_step_row, text="-",
            command=lambda: self.delete_item(
                new_step_row, steps_li, steps_container, item_type="step")

        )
        new_delete_button.pack(side=tk.LEFT)
        new_delete_button.config(width=SMALL_BUTTON_WIDTH)

    def delete_item(self, entry_to_del, entry_li, container, item_type=None):

        if item_type == "step" and len(entry_li) >= 1:
            entry_to_del.destroy()
            entry_li.remove(entry_to_del)
        else:
            if item_type == "plan":
                full_entry = entry_to_del
                entry_to_del = entry_to_del["Plan"]
                entry_li.remove(full_entry)
            parent_name = entry_to_del.winfo_parent()
            parent = entry_to_del._nametowidget(parent_name)

            if item_type == "plan":
                grandparent_name = parent.winfo_parent()
                grandparent = parent._nametowidget(grandparent_name)
                grandparent.destroy()
            else:
                parent.destroy()
                entry_li.remove(entry_to_del)
        """
        Add one if none left
        """
        if len(entry_li) == 0 and item_type == "plan":
            self.add_plan_item(container, entry_li)
        elif len(entry_li) == 0 and item_type is None:
            self.add_input_item(container, entry_li)
