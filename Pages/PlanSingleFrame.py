from Controller import *

import tkinter as tk
from tkinter import PhotoImage, ttk

from CustomWidgets import DisplayOnlyText
from CustomStyle import *


class PlanFrame(ttk.Frame):
    """
    A frame to show a plan in display-only mode

    ...

    Attributes
    ----------
    parent : tk.Frame
        the container of the Frame
    plan : pandas.DataFrame named tuple
        the data to be displayed
    standalone: boolean
        whether the plan is shown as part of an entry or by itself (default False)

    Methods
    -------
    toggle_edit_mode()
        Toggles between display and edit view

    confirm_delete()
        Creates a pop up window to confirm deletion
    """

    def __init__(self, parent, plan, standalone=False, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.plan = plan

        self.standalone = standalone

        self.container = None
        self.toggle_view_mode()

    def toggle_view_mode(self):
        if self.container is not None:
            self.container.destroy()
        self.container = ttk.Frame(self)
        self.container.pack(padx=SMALL_PAD, pady=SMALL_PAD)
        """
        Date + Description
        """
        if self.standalone:
            self.date_row = ttk.Frame(self.container)
            self.date_row.pack(side=tk.TOP, fill=tk.X)

            self.date_lab = ttk.Label(
                self.date_row,
                text="Date Created: ",
                font=SMALL_LABEL_FONT)
            self.date_lab.pack(side=tk.LEFT, anchor='nw')

            self.date_lab = ttk.Label(
                self.date_row,
                text=self.plan.Date_created.strftime("%Y-%m-%d"))
            self.date_lab.pack(side=tk.LEFT, anchor='nw')

            self.desc_title_row = ttk.Frame(self.container)
            self.desc_title_row.pack(fill=tk.X)
            self.desc_title_lab = ttk.Label(
                self.desc_title_row,
                text="Description: ",
                font=SMALL_LABEL_FONT)
            self.desc_title_lab.pack(side=tk.LEFT, anchor='nw',
                                     pady=SMALL_PAD)

        self.desc_row = ttk.Frame(self.container)
        self.desc_row.pack()

        self.desc_lab = DisplayOnlyText(self.desc_row)
        self.desc_lab.pack(side=tk.LEFT, fill=tk.X)

        """
        Status
        """
        status_font_col = INCOMP_COLOR
        if self.plan.Status == "Completed":
            status_font_col = COMP_COLOR
        elif self.plan.Status == "Scrapped":
            status_font_col = SCRAP_COLOR

        if not self.standalone:
            self.desc_lab.insert(tk.INSERT, self.plan.Status+"  ")
            self.desc_lab.tag_add("status", "1.0", "1." +
                                  str(len(self.plan.Status) + 2))
            self.desc_lab.tag_config(
                "status", foreground=status_font_col, font=ANNOTATE_FONT)

        """
        Priority
        """

        priority_font_col = MEDP_COLOR
        if self.plan.Priority == "High":
            priority_font_col = HIGHP_COLOR
        elif self.plan.Priority == "Low":
            priority_font_col = LOWP_COLOR

        if not self.standalone:
            self.desc_lab.insert(tk.INSERT, self.plan.Priority + "  ")
            self.desc_lab.tag_add("priority", "1." + str(len(self.plan.Status) + 2),
                                  "1." + str(len(self.plan.Status) + 2 + len(self.plan.Priority)
                                             ))
            self.desc_lab.tag_config(
                "priority", foreground=priority_font_col, font=ANNOTATE_FONT)

        self.desc_lab.insert('end', self.plan.Description)
        self.desc_lab.configure(state='disabled')

        if self.standalone:

            """
            Status + Priority in Standalone mode
            """
            self.status_row = ttk.Frame(self.container)
            self.status_row.pack(side=tk.TOP, fill=tk.X)

            """Status"""
            self.status_title_lab = ttk.Label(
                self.status_row,
                text="Status:\t",
                font=SMALL_LABEL_FONT)
            self.status_title_lab.pack(side=tk.LEFT, anchor='nw',
                                       pady=SMALL_PAD)

            self.status_lab = tk.Label(
                self.status_row,
                text=self.plan.Status,
                font=ANNOTATE_FONT)
            self.status_lab.pack(side=tk.LEFT,  fill=tk.Y, anchor="nw",
                                 padx=SMALL_PAD,  pady=SMALL_PAD)

            self.status_lab.config(fg=status_font_col)

            if self.plan.Priority != "":
                self.priority_row = ttk.Frame(self.container)
                self.priority_row.pack(side=tk.TOP, fill=tk.X)

                self.priority_title_lab = ttk.Label(
                    self.priority_row,
                    text="Priority:\t",
                    font=SMALL_LABEL_FONT)
                self.priority_title_lab.pack(side=tk.LEFT, anchor='nw',
                                             pady=SMALL_PAD)

                self.priority_lab = tk.Label(
                    self.priority_row,
                    text=self.plan.Priority,
                    font=ANNOTATE_FONT)
                self.priority_lab.pack(side=tk.LEFT,  fill=tk.Y, anchor="nw",
                                       padx=SMALL_PAD,  pady=SMALL_PAD)

                self.priority_lab.config(fg=priority_font_col)
        """
        Steps
        """

        if self.plan.Num_Steps > 0:
            steps = match_steps(self.plan, test=TESTING)
            if self.standalone:
                self.steps_title_row = ttk.Frame(self.container)
                self.steps_title_row.pack(side=tk.TOP, fill=tk.X)
                self.steps_lab = ttk.Label(self.steps_title_row, text="Steps: ",
                                           font=SMALL_LABEL_FONT)
                self.steps_lab.pack(fill=tk.X,
                                    pady=SMALL_PAD)

            self.steps_container = ttk.Frame(self.container)
            self.steps_container.pack(padx=SMALL_PAD)

            for step in steps.itertuples():
                step_row = ttk.Frame(self.steps_container)
                step_row.pack(side=tk.TOP)
                step_desc = DisplayOnlyText(step_row)

                if step.Status == "Completed":
                    step_desc.insert(tk.INSERT, "v    ")
                    step_desc.tag_add("status", "1.0", "1.1")
                    step_desc.tag_config(
                        "status", foreground=COMP_COLOR, font=ANNOTATE_FONT)
                else:
                    step_desc.insert(tk.INSERT, "•    ")
                    step_desc.tag_add("status", "1.0", "1.1")
                    step_desc.tag_config(
                        "status", foreground=INCOMP_COLOR, font=ANNOTATE_FONT)

                step_desc.insert("end", step.Description)
                step_desc.configure(state='disabled')
                step_desc.pack(side=tk.LEFT)

        if self.standalone:
            pencil_icon = PhotoImage(file="Icon/pencil.png").subsample(4, 4)
            TRASH_ICON = PhotoImage(file="Icon/trash.png").subsample(4, 4)

            self.options_row = ttk.Frame(self.container)
            self.options_row.pack(side=tk.TOP,
                                  padx=SMALL_PAD, pady=SMALL_PAD)

            self.edit_button = ttk.Button(self.options_row,
                                          text="Edit",
                                          image=pencil_icon,
                                          command=lambda: self.toggle_edit_mode())
            self.edit_button.image = pencil_icon
            self.edit_button.pack(side=tk.LEFT)

            self.delete_button = ttk.Button(self.options_row,
                                            text="Delete",
                                            image=TRASH_ICON,
                                            command=lambda: self.confirm_delete())
            self.delete_button.image = TRASH_ICON
            self.delete_button.pack(side=tk.LEFT)

    def toggle_edit_mode(self):

        self.container.destroy()
        self.container = ttk.Frame(self)
        self.container.pack(expand=tk.YES, fill=tk.X,
                            padx=SMALL_PAD, pady=SMALL_PAD)

        SUBMIT_ICON = PhotoImage(file="Icon/enter.png").subsample(4, 4)
        TRASH_ICON = PhotoImage(file="Icon/trash.png").subsample(4, 4)

        """Date"""

        self.date_row = ttk.Frame(self.container)
        self.date_row.pack(side=tk.TOP, fill=tk.X, pady=SMALL_PAD)

        self.date_lab = ttk.Label(
            self.date_row,
            text="Date Created:   ",
            font=SMALL_LABEL_FONT)
        self.date_lab.pack(side=tk.LEFT, anchor='nw')

        self.date_lab = ttk.Label(
            self.date_row,
            text=self.plan.Date_created.strftime("%Y-%m-%d"))
        self.date_lab.pack(side=tk.LEFT, anchor='nw')

        """Draft"""

        self.draft_row = ttk.Frame(self.container)
        self.draft_row.pack(side=tk.TOP, fill=tk.X, pady=SMALL_PAD)

        self.draft_title_lab = ttk.Label(
            self.draft_row,
            text="Draft:\t",
            font=SMALL_LABEL_FONT)
        self.draft_title_lab.pack(side=tk.LEFT, anchor='nw',
                                  pady=SMALL_PAD)
        self.draft_check_var = tk.StringVar()
        self.draft_check_button = ttk.Checkbutton(
            self.draft_row, variable=self.draft_check_var,
            onvalue="Draft", offvalue="Log")

        self.draft_check_button.pack(side=tk.LEFT)

        self.draft_check_var.set(self.plan.Plan_Type)

        """
        Description
        """
        self.desc_title_row = ttk.Frame(self.container)
        self.desc_title_row.pack(fill=tk.X, pady=SMALL_PAD)
        self.desc_title_lab = ttk.Label(
            self.desc_title_row,
            text="Description: ",
            font=SMALL_LABEL_FONT)
        self.desc_title_lab.pack(side=tk.LEFT, anchor='nw')

        self.desc_row = ttk.Frame(self.container)
        self.desc_row.pack(fill=tk.X)

        self.description_entry = ttk.Entry(self.desc_row)
        self.description_entry.pack(side=tk.LEFT,
                                    expand=tk.YES, fill=tk.X,
                                    padx=SMALL_PAD, pady=SMALL_PAD)

        self.description_entry.insert('end', self.plan.Description)

        """
        Status
        """
        self.status_row = ttk.Frame(self.container)
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
        self.status_var.set(self.plan.Status)
        self.status_menu.pack(side=tk.LEFT)

        """
        Priority
        """
        self.priority_row = ttk.Frame(self.container)
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
        self.priority_var.set(self.plan.Priority)
        self.priority_menu.pack(side=tk.LEFT)

        """
        Steps
        """
        self.steps_title_row = ttk.Frame(self.container)
        self.steps_title_row.pack(side=tk.TOP, fill=tk.X,
                                  pady=SMALL_PAD)

        self.steps_lab = ttk.Label(self.steps_title_row, text="Steps: ",
                                   font=SMALL_LABEL_FONT)
        self.steps_lab.pack(fill=tk.X)

        self.steps_container = ttk.Frame(self.container)
        self.steps_container.pack(side=tk.TOP, fill=tk.X,
                                  padx=SMALL_PAD, pady=SMALL_PAD)

        self.steps_li = []

        self.add_step_button = None

        if self.plan.Num_Steps > 0:
            steps = match_steps(self.plan, test=TESTING)
            for step in steps.itertuples():
                self.add_step_item(prev_step=step)
        else:
            self.add_step_button = ttk.Button(
                self.steps_container, text="Add Step",
                command=lambda: self.add_step_item(prev_step=None))
            self.add_step_button.pack(side=tk.TOP)

        """
        Buttons
        """
        self.options_row = ttk.Frame(self.container)
        self.options_row.pack(side=tk.TOP,
                              padx=SMALL_PAD, pady=SMALL_PAD)

        self.edit_button = ttk.Button(self.options_row,
                                      text="Edit",
                                      image=SUBMIT_ICON,
                                      command=lambda: self.update_prev_plan())
        self.edit_button.image = SUBMIT_ICON
        self.edit_button.pack(side=tk.LEFT)

        self.delete_button = ttk.Button(self.options_row,
                                        text="Delete",
                                        image=TRASH_ICON,
                                        command=lambda: self.confirm_delete())
        self.delete_button.image = TRASH_ICON
        self.delete_button.pack(side=tk.LEFT)

    def confirm_delete(self):
        self.destroy()

    def add_step_item(self, prev_step=None):
        if len(self.steps_li) == 0 and prev_step is None:
            self.add_step_button.destroy()

        new_step_row = ttk.Frame(self.steps_container)
        new_step_row.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X)

        check_var = tk.StringVar()
        new_step_checkb = ttk.Checkbutton(
            new_step_row, variable=check_var,
            onvalue="Completed", offvalue="Incomplete")

        new_step_checkb.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

        new_step_box = ttk.Entry(new_step_row)
        new_step_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

        full_step_entry = {"Description": new_step_box, "Status": check_var}
        self.steps_li.append(full_step_entry)

        if prev_step is not None:
            check_var.set(prev_step.Status)
            new_step_box.insert('end', prev_step.Description)

        """Add Button"""

        new_button_add_new = ttk.Button(
            new_step_row, text="+",
            command=lambda: self.add_step_item(prev_step=None))
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

    def update_prev_plan(self):
        plan = {}
        plan["Plan_ID"] = self.plan.Plan_ID
        plan["Plan_Type"] = self.draft_check_var.get()
        plan["Description"] = self.description_entry.get()
        plan["Status"] = self.status_var.get()
        plan["Priority"] = self.priority_var.get()
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
