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
                font=LABEL_FONT)
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
                font=LABEL_FONT)
            self.desc_title_lab.pack(side=tk.LEFT, anchor='nw',
                                     pady=SMALL_PAD)

        self.desc_row = ttk.Frame(self.container)
        self.desc_row.pack()

        self.desc_lab = DisplayOnlyText(self.desc_row)
        self.desc_lab.pack(side=tk.LEFT, fill=tk.X)

        """
        Status
        """
        font_col = INCOMP_COLOR
        if self.plan.Status == "Completed":
            font_col = COMP_COLOR
        elif self.plan.Status == "Scrapped":
            font_col = SCRAP_COLOR

        if not self.standalone:
            self.desc_lab.insert(tk.INSERT, self.plan.Status+"\t")
            self.desc_lab.tag_add("status", "1.0", "1." +
                                  str(len(self.plan.Status)))
            self.desc_lab.tag_config(
                "status", foreground=font_col, font=ANNOTATE_FONT)

        self.desc_lab.insert('end', self.plan.Description)
        self.desc_lab.configure(state='disabled')

        if self.standalone:
            self.status_row = ttk.Frame(self.container)
            self.status_row.pack(side=tk.TOP, fill=tk.X)

            self.status_title_lab = ttk.Label(
                self.status_row,
                text="Status: ",
                font=LABEL_FONT)
            self.status_title_lab.pack(side=tk.LEFT, anchor='nw',
                                       pady=SMALL_PAD)

            self.status_lab = tk.Label(
                self.status_row,
                text=self.plan.Status,
                font=ANNOTATE_FONT)
            self.status_lab.pack(side=tk.LEFT,  fill=tk.Y, anchor="nw",
                                 padx=SMALL_PAD,  pady=SMALL_PAD)

            self.status_lab.config(fg=font_col)
        """
        Steps
        """

        if self.plan.Num_Steps > 0:
            steps = match_steps(self.plan)
            if self.standalone:
                self.steps_title_row = ttk.Frame(self.container)
                self.steps_title_row.pack(side=tk.TOP, fill=tk.X)
                steps_lab = ttk.Label(self.steps_title_row, text="Steps: ",
                                      font=LABEL_FONT)
                steps_lab.pack(fill=tk.X,
                               pady=SMALL_PAD)

            steps_container = ttk.Frame(self.container)
            steps_container.pack(padx=SMALL_PAD)

            for step in steps.itertuples():
                step_row = ttk.Frame(steps_container)
                step_row.pack(side=tk.TOP)
                step_desc = DisplayOnlyText(step_row)

                if step.Status == "Completed":
                    step_desc.insert(tk.INSERT, "v ")
                    step_desc.tag_add("status", "1.0", "1.1")
                    step_desc.tag_config(
                        "status", foreground=COMP_COLOR, font=ANNOTATE_FONT)
                else:
                    step_desc.insert(tk.INSERT, "• ")
                    step_desc.tag_add("status", "1.0", "1.1")
                    step_desc.tag_config(
                        "status", foreground=INCOMP_COLOR, font=ANNOTATE_FONT)

                step_desc.insert("end", step.Description)
                step_desc.configure(state='disabled')
                step_desc.pack(side=tk.LEFT)

        if self.standalone:
            pencil_icon = PhotoImage(file="Icon/pencil.png").subsample(4, 4)
            trash_icon = PhotoImage(file="Icon/trash.png").subsample(4, 4)

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
                                            image=trash_icon)
            self.delete_button.image = trash_icon
            self.delete_button.pack(side=tk.LEFT)

    def toggle_edit_mode(self):
        self.container.destroy()
        self.container = ttk.Frame(self)
        self.container.pack(padx=SMALL_PAD, pady=SMALL_PAD)

        self.date_row = ttk.Frame(self.container)
        self.date_row.pack(side=tk.TOP, fill=tk.X,
                           padx=SMALL_PAD, pady=SMALL_PAD)

        self.date_lab = ttk.Label(
            self.date_row,
            text="Date Created: ",
            font=LABEL_FONT)
        self.date_lab.pack(side=tk.LEFT, anchor='nw')

        self.date_lab = ttk.Label(
            self.date_row,
            text=self.plan.Date_created.strftime("%Y-%m-%d"))
        self.date_lab.pack(side=tk.LEFT, anchor='nw')

        submit_icon = PhotoImage(file="Icon/enter.png").subsample(4, 4)
        trash_icon = PhotoImage(file="Icon/trash.png").subsample(4, 4)

        """
        Description
        """
        self.desc_title_row = ttk.Frame(self.container)
        self.desc_title_row.pack(fill=tk.X)
        self.desc_title_lab = ttk.Label(
            self.desc_title_row,
            text="Description: ",
            font=LABEL_FONT)
        self.desc_title_lab.pack(side=tk.LEFT, anchor='nw',
                                 padx=SMALL_PAD, pady=SMALL_PAD)

        self.desc_row = ttk.Frame(self.container)
        self.desc_row.pack(fill=tk.X)

        self.plan_entry = ttk.Entry(self.desc_row)
        self.plan_entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X,
                             padx=SMALL_PAD, pady=SMALL_PAD)

        self.plan_entry.insert('end', self.plan.Description)

        """
        Status
        """
        self.status_row = ttk.Frame(self.container)
        self.status_row.pack(side=tk.TOP, fill=tk.X)

        self.status_title_lab = ttk.Label(
            self.status_row,
            text="Status: ",
            font=LABEL_FONT)
        self.status_title_lab.pack(side=tk.LEFT, anchor='nw',
                                   pady=SMALL_PAD)

        self.status_menu = ttk.Combobox(self.status_row,
                                        values=PLAN_STATUSES,
                                        justify=tk.CENTER, width=10)
        self.status_menu.current([0])
        self.status_menu.state(statespec=('!disabled', 'readonly'))
        self.status_menu.pack(side=tk.LEFT)

        """
        Steps
        """
        self.steps_title_row = ttk.Frame(self.container)
        self.steps_title_row.pack(side=tk.TOP, fill=tk.X,
                                  padx=SMALL_PAD, pady=SMALL_PAD)

        steps_lab = ttk.Label(self.steps_title_row, text="Steps: ",
                              font=LABEL_FONT)
        steps_lab.pack(fill=tk.X)

        steps_container = ttk.Frame(self.container)
        steps_container.pack(side=tk.TOP, padx=SMALL_PAD, pady=SMALL_PAD)

        new_steps_li = []

        if self.plan.Num_Steps > 0:
            steps = match_steps(self.plan)
            for step in steps.itertuples():
                self.add_step_item(
                    steps_container, new_steps_li, prev_step=step)
        else:
            self.add_step_item(
                steps_container, new_steps_li, prev_step=None)

        """
        Buttons
        """
        self.options_row = ttk.Frame(self.container)
        self.options_row.pack(side=tk.TOP,
                              padx=SMALL_PAD, pady=SMALL_PAD)

        self.edit_button = ttk.Button(self.options_row,
                                      text="Edit",
                                      image=submit_icon,
                                      command=lambda: self.toggle_view_mode())
        self.edit_button.image = submit_icon
        self.edit_button.pack(side=tk.LEFT)

        self.delete_button = ttk.Button(self.options_row,
                                        text="Delete",
                                        image=trash_icon)
        self.delete_button.image = trash_icon
        self.delete_button.pack(side=tk.LEFT)

    def add_step_item(self, steps_container, steps_li, prev_step=None):
        new_step_row = ttk.Frame(steps_container)
        new_step_row.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X)

        check_var = tk.StringVar()
        new_step_checkb = ttk.Checkbutton(
            new_step_row, variable=check_var,
            onvalue="Completed", offvalue="Incomplete")

        new_step_checkb.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

        new_step_box = ttk.Entry(new_step_row)
        new_step_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        steps_li.append(new_step_box)

        if prev_step is not None:
            check_var.set(prev_step.Status)
            new_step_box.insert('end', prev_step.Description)

        """Add Button"""

        new_button_add_new = ttk.Button(
            new_step_row, text="+",
            command=lambda: self.add_step_item(steps_container, steps_li, prev_step=None))
        new_button_add_new.pack(side=tk.LEFT)
        new_button_add_new.config(width=SMALL_BUTTON_WIDTH)

        """Delete Button"""
        new_delete_button = ttk.Button(
            new_step_row, text="-",
            command=lambda: self.delete_step_item(self, steps_container, new_step_row, steps_li))
        new_delete_button.pack(side=tk.LEFT)
        new_delete_button.config(width=SMALL_BUTTON_WIDTH)

    def delete_step_item(self, steps_container, step_to_del, step_li):
        if len(step_li) == 0:
            pass

        if len(step_li) > 1:
            parent_name = step_to_del.winfo_parent()
            parent = step_to_del._nametowidget(parent_name)
            parent.destroy()
            step_li.remove(step_to_del)

        if len(step_li) == 0:
            self.add_step_item(steps_container, step_li, prev_input=None)
