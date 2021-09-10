from os import stat
import pandas as pd
from Controller import *

import tkinter as tk
from tkinter import PhotoImage, ttk

from CustomWidgets import ScrollableText, ScrollableFrame
from CustomStyle import *


class AddPlanPage(ttk.Frame):
    """
    A page to add a new entry

    ...

    Attributes
    ----------
    root : tk.Tk
        the root Tk application

    Methods
    -------
    add_input_item(entry_container, entry_li)
        Adds a new input row with entry box, plus and minus button

    add_plan_item(plan_container, plan_li)
        Adds a new input row for a plan with an entry box for plan description, add step button and delete button

    add_step_item(self.steps_container, steps_li)
        Adds a new input row for a step with checkbox for step status, entry box for step description, plus and minus button

    delete_item(entry_to_del, entry_li, container, item_type=None)
        Removes input row from interface and tracking list
    """

    def __init__(self, root, *args, **kwargs):
        """
        Parameters
        ----------
        root : tk.Tk
            the root Tk application
        *args : optional
            extra arguments for parent constructor
        **kwargs : optional
            extra keyword arguments for parent constructor
        """

        super().__init__(root, *args, **kwargs)

        """
        Menu Pane
        """
        self.menu_container = ttk.Frame(self)
        self.menu_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD)

        self.quit_button = ttk.Button(self.menu_container, text="Back",
                                      command=lambda: root.switch_page(root._HomePage))
        self.quit_button.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.log_button = ttk.Button(self.menu_container, text="Save",
                                     command=lambda: self.submit_entry())

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

        self.form.pack(expand=tk.YES,
                       padx=SMALL_PAD, pady=SMALL_PAD)
        """
        Description
        """
        self.desc_title_row = ttk.Frame(self.form)
        self.desc_title_row.pack(fill=tk.X, pady=SMALL_PAD)
        self.desc_title_lab = ttk.Label(
            self.desc_title_row,
            text="Description: ",
            font=SMALL_LABEL_FONT)
        self.desc_title_lab.pack(side=tk.LEFT, anchor='nw')

        self.desc_row = ttk.Frame(self.form)
        self.desc_row.pack(fill=tk.X)

        self.description_entry = ttk.Entry(self.desc_row)
        self.description_entry.pack(side=tk.LEFT,
                                    expand=tk.YES, fill=tk.X,
                                    padx=SMALL_PAD, pady=SMALL_PAD)

        """
        Status
        """
        self.status_row = ttk.Frame(self.form)
        self.status_row.pack(side=tk.TOP, fill=tk.X, pady=SMALL_PAD)

        self.status_title_lab = ttk.Label(
            self.status_row,
            text="Status:\t",
            font=SMALL_LABEL_FONT)
        self.status_title_lab.pack(side=tk.LEFT, anchor='nw',
                                   pady=SMALL_PAD)
        self.status_var = tk.StringVar()
        self.status_menu = ttk.Combobox(self.status_row,
                                        textvariable=self.status_var,
                                        values=PLAN_STATUSES,
                                        style=COMBOBOX_STYLE,
                                        state="readonly",
                                        justify=tk.CENTER, width=10)
        self.status_menu.pack(side=tk.LEFT)

        """
        Priority
        """
        self.priority_row = ttk.Frame(self.form)
        self.priority_row.pack(side=tk.TOP, fill=tk.X, pady=SMALL_PAD)

        self.priority_title_lab = ttk.Label(
            self.priority_row,
            text="Priority:\t",
            font=SMALL_LABEL_FONT)
        self.priority_title_lab.pack(side=tk.LEFT, anchor='nw',
                                     pady=SMALL_PAD)
        self.priority_var = tk.StringVar()
        self.priority_menu = ttk.Combobox(self.priority_row,
                                          textvariable=self.priority_var,
                                          values=PRIORITY_LVL,
                                          style=COMBOBOX_STYLE,
                                          state="readonly",
                                          justify=tk.CENTER, width=10)
        self.priority_menu.pack(side=tk.LEFT)

        """
        Steps
        """
        self.steps_title_row = ttk.Frame(self.form)
        self.steps_title_row.pack(side=tk.TOP, fill=tk.X,
                                  pady=SMALL_PAD)

        self.steps_lab = ttk.Label(self.steps_title_row, text="Steps: ",
                                   font=SMALL_LABEL_FONT)
        self.steps_lab.pack(fill=tk.X)

        self.steps_container = ttk.Frame(self.form)
        self.steps_container.pack(side=tk.TOP, fill=tk.X,
                                  padx=SMALL_PAD, pady=SMALL_PAD)

        self.steps_li = []

        self.add_step_button = ttk.Button(
            self.steps_container, text="Add Step",
            command=lambda: self.add_step_item())
        self.add_step_button.pack(side=tk.TOP)

    def add_step_item(self):
        if len(self.steps_li) == 0:
            self.add_step_button.destroy()

        new_step_row = ttk.Frame(self.steps_container)
        new_step_row.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X)

        check_var = tk.StringVar()
        new_step_checkb = ttk.Checkbutton(
            new_step_row, variable=check_var,
            onvalue="Completed", offvalue="Incomplete")

        new_step_checkb.pack(side=tk.LEFT)

        new_step_box = ttk.Entry(new_step_row)
        new_step_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

        full_step_entry = {"Description": new_step_box, "Status": check_var}
        self.steps_li.append(full_step_entry)

        """Add Button"""

        new_button_add_new = ttk.Button(
            new_step_row, text="+",
            command=lambda: self.add_step_item())
        new_button_add_new.pack(side=tk.LEFT)
        new_button_add_new.config(width=SMALL_BUTTON_WIDTH)

        """Delete Button"""
        new_delete_button = ttk.Button(
            new_step_row, text="-",
            command=lambda: self.delete_step_item(full_step_entry))
        new_delete_button.pack(side=tk.LEFT)
        new_delete_button.config(width=SMALL_BUTTON_WIDTH)

    def delete_step_item(self,  step_to_del):

        if len(self.steps_li):
            parent_name = step_to_del["Description"].winfo_parent()
            parent = step_to_del["Description"]._nametowidget(parent_name)
            parent.destroy()
            self.steps_li.remove(step_to_del)

        if len(self.steps_li) == 0:
            self.add_step_button = ttk.Button(
                self.steps_container, text="Add Step",
                command=lambda: self.add_step_item())
            self.add_step_button.pack(side=tk.TOP)

    def submit_plan(self, plan_type="Log"):
        plan = {}
        plan["Description"] = self.description_entry.get()
        plan["Status"] = self.status_var
        plan["Priority"] = self.priority_var
        plan["Steps"] = []

        for step_entry in self.steps_li:
            step_txt = step_entry["Description"].get()
            if step_txt == "":
                pass
            else:
                full_step = {"Status": step_entry["Status"].get(),
                             "Description": step_txt}
                plan["Steps"].append(full_step)
        self.toggle_view_mode()
