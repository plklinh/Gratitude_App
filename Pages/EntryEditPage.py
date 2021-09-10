from Controller import *

import tkinter as tk
from tkinter import PhotoImage, ttk

from CustomWidgets import ScrollableText, ScrollableFrame
from CustomStyle import *


class EditEntryPage(ttk.Frame):
    def __init__(self, root, entry, *args, **kwargs):
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
                                     command=lambda: root.switch_page(root._HomePage))

        self.log_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.draft_button = ttk.Button(self.menu_container, text="Save as Draft",
                                       command=lambda: root.switch_page(root._HomePage))
        self.draft_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.delete_button = ttk.Button(self.menu_container, text="Delete",
                                        command=lambda: root.switch_page(root._HomePage))
        self.delete_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

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
            font=SMALL_LABEL_FONT,
            anchor='nw')
        self.gratitude_lab.pack(side=tk.LEFT)

        self.gratitude_entry_container = ttk.Frame(self.gratitude_row)
        self.gratitude_entry_container.pack(expand=tk.YES, fill=tk.X,
                                            side=tk.LEFT)

        self.grat_entry_li = []

        if len(entry.Gratitude) > 0:
            for grat in entry.Gratitude:
                self.add_input_item(self.gratitude_entry_container,
                                    self.grat_entry_li, prev_input=grat)
        else:
            self.add_input_item(self.gratitude_entry_container,
                                self.grat_entry_li)

        """
        Goals Row
        """
        self.goals_row = ttk.Frame(self.form)
        self.goals_row.pack(expand=tk.YES,
                            side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.goals_lab = ttk.Label(
            self.goals_row, width=20,
            text="Goals: ",
            font=SMALL_LABEL_FONT,
            anchor='nw')
        self.goals_lab.pack(side=tk.LEFT)

        self.goals_entry_container = ttk.Frame(self.goals_row)
        self.goals_entry_container.pack(
            side=tk.LEFT, expand=tk.YES, fill=tk.X)

        self.goals_entry_li = []

        if len(entry.Goals) > 0:
            for goal in entry.Goals:
                self.add_input_item(self.goals_entry_container,
                                    self.goals_entry_li, prev_input=goal)
        else:
            self.add_input_item(self.goals_entry_container,
                                self.goals_entry_li)

        """
        Plans Row
        """
        self.plans_row = ttk.Frame(self.form)
        self.plans_row.pack(expand=tk.YES,
                            side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.plans_lab = ttk.Label(
            self.plans_row, width=20,
            text="Plans: ",
            font=SMALL_LABEL_FONT,
            anchor='nw')
        self.plans_lab.pack(side=tk.LEFT)

        self.plans_container = ttk.Frame(self.plans_row)
        self.plans_container.pack(
            side=tk.LEFT, expand=tk.YES, fill=tk.X)

        self.plans_entry_container = ttk.Frame(self.plans_container)
        self.plans_entry_container.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X)

        # Empty Widget to resize container
        empty_widget = ttk.Frame(self.plans_entry_container)
        empty_widget.pack(side=tk.TOP)

        self.plans_entry_li = []

        if len(entry.Plans) > 0:
            plans_df = match_plans(entry)
            for plan in plans_df.itertuples():
                self.add_plan_item(
                    self.plans_entry_container, self.plans_entry_li, plan)
        else:
            self.add_plan_item(self.plans_entry_container, self.plans_entry_li)

        self.plans_button = ttk.Button(
            self.plans_container, text="+ plan",
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
            font=SMALL_LABEL_FONT,
            anchor='nw')
        self.affirm_lab.pack(side=tk.LEFT)

        self.affirm_entry = ScrollableText(
            self.affirm_row, height=10, width=50)
        self.affirm_entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X,
                               ipadx=10, ipady=10)

        if entry.Affirmation is not None:
            self.affirm_entry.insert("end", entry.Affirmation)

        """
        Note Row
        """
        self.notes_row = ttk.Frame(self.form)
        self.notes_row.pack(expand=tk.YES,
                            side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.notes_lab = ttk.Label(
            self.notes_row, width=20,
            text="Additional Notes: ",
            font=SMALL_LABEL_FONT,
            anchor='w')
        self.notes_lab.pack(side=tk.LEFT)

        self.notes_entry = ScrollableText(self.notes_row, height=10, width=50)

        self.notes_entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X,
                              ipadx=10, ipady=10)

        if entry.Additional_Notes is not None:
            self.notes_entry.insert("end", entry.Additional_Notes)

    def add_input_item(self, entry_container, entry_li,  prev_input=None):
        new_entry_frame = ttk.Frame(entry_container)
        new_entry_frame.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X)

        """Entry Box"""
        new_entry_box = ttk.Entry(new_entry_frame)
        new_entry_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        entry_li.append(new_entry_box)

        if prev_input is not None:
            new_entry_box.insert('end', prev_input)

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

    def add_plan_item(self, plan_container, plan_li, prev_plan=None):
        new_plan_frame = ttk.Frame(plan_container)
        new_steps_li = []
        new_plan_frame.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)

        """Description"""
        description_row = ttk.Frame(new_plan_frame)
        description_row.pack(expand=tk.YES, fill=tk.X)

        description_lab = ttk.Label(
            description_row,
            text="Description",
            font=ANNOTATE_FONT)

        description_lab.pack(side=tk.LEFT, anchor='nw',
                             pady=SMALL_PAD, padx=(0, SMALL_PAD))

        """Description Entry Box"""
        new_plan_box = ttk.Entry(description_row)
        new_plan_box.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

        """Delete Button"""
        TRASH_ICON = PhotoImage(file="Icon/trash.png").subsample(4, 4)

        new_delete_button = ttk.Button(
            description_row,
            text="Delete",
            image=TRASH_ICON,
            command=lambda: self.delete_item(full_plan_entry, plan_li,
                                             plan_container, item_type="plan"))
        new_delete_button.image = TRASH_ICON
        new_delete_button.pack(side=tk.LEFT)
        new_delete_button.config(width=SMALL_BUTTON_WIDTH)

        """
        Aux Row
        """
        aux_row = ttk.Frame(new_plan_frame)
        aux_row.pack(expand=tk.YES, fill=tk.X)
        """Status"""
        status_title_lab = ttk.Label(
            aux_row,
            text="Status\t",
            font=ANNOTATE_FONT)
        status_title_lab.pack(side=tk.LEFT, anchor='nw',
                              pady=SMALL_PAD, padx=(0, 0))

        status_menu = ttk.Combobox(aux_row,
                                   values=PLAN_STATUSES,
                                   style=COMBOBOX_STYLE,
                                   state="readonly",
                                   justify=tk.CENTER, width=10)
        status_menu.current([0])
        status_menu.pack(side=tk.LEFT)

        status_title_lab = ttk.Label(
            aux_row,
            text="\tPriority\t",
            font=ANNOTATE_FONT)
        status_title_lab.pack(side=tk.LEFT, anchor='nw',
                              pady=SMALL_PAD, padx=(0, SMALL_PAD))

        """Priority"""
        priority_menu = ttk.Combobox(aux_row,
                                     values=PRIORITY_LVL,
                                     style=COMBOBOX_STYLE,
                                     state="readonly",
                                     justify=tk.CENTER, width=10)
        priority_menu.pack(side=tk.LEFT)

        steps_row = ttk.Frame(new_plan_frame)
        steps_row.pack(fill=tk.X, pady=(0, SMALL_PAD))

        if prev_plan is not None:
            status_menu.current(PLAN_STATUSES.index(prev_plan.Status))
            priority_menu.current(PRIORITY_LVL.index(prev_plan.Priority))
            new_plan_box.insert('end', prev_plan.Description)
            if prev_plan.Num_Steps > 0:
                steps = match_steps(prev_plan)
                for step in steps.itertuples():
                    self.add_step_item(
                        steps_row, new_steps_li, prev_step=step)

        """
        Steps
        """
        steps_lab = ttk.Label(steps_row,
                              text="Steps\t",
                              font=ANNOTATE_FONT)
        steps_lab.pack(side=tk.LEFT, anchor='nw',
                       pady=SMALL_PAD, padx=(0, SMALL_PAD))

        add_step_button = ttk.Button(steps_row, text="+ step",
                                     command=lambda: self.add_step_item(steps_row, new_steps_li))
        add_step_button.pack(side=tk.TOP, pady=(SMALL_PAD, 0))

        """Draft"""
        draft_row = ttk.Frame(new_plan_frame)
        draft_row.pack(side=tk.TOP, expand=tk.YES, fill=tk.X,
                       pady=(0, SMALL_PAD))

        draft_title_lab = ttk.Label(
            draft_row,
            text="Draft\t",
            font=ANNOTATE_FONT)
        draft_title_lab.pack(side=tk.LEFT, anchor='nw',
                             pady=SMALL_PAD)
        draft_check_var = tk.StringVar()
        draft_check_button = ttk.Checkbutton(
            draft_row, variable=draft_check_var,
            onvalue="Draft", offvalue="Log")

        draft_check_button.pack(side=tk.LEFT, padx=(SMALL_PAD, 0))

        if prev_plan is not None:
            draft_check_var.set(prev_plan.Plan_Type)

        """Append full plan entry"""

        full_plan_entry = {"Description": new_plan_box, "Plan_Type": draft_check_button, "Status": status_menu,
                           "Priority": priority_menu, "Steps": new_steps_li}
        plan_li.append(full_plan_entry)

    def add_step_item(self, steps_container, steps_li, prev_step=None):
        if len(steps_li) == 0:
            add_step_button_name = steps_container.winfo_children()[1]
            add_step_button = steps_container._nametowidget(
                add_step_button_name)
            add_step_button.destroy()

        new_step_row = ttk.Frame(steps_container)
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
        steps_li.append(full_step_entry)

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
            command=lambda: self.delete_item(
                full_step_entry, steps_li, steps_container, item_type="step"))
        new_delete_button.pack(side=tk.LEFT)
        new_delete_button.config(width=SMALL_BUTTON_WIDTH)

    def delete_item(self, entry_to_del, entry_li, container, item_type=None):
        """Removes input row from interface and tracking list.

        Parameters
        ----------
        entry_to_del: ttk.Frame
            The input row to delete

        entry_li: list
            List of inputs that tracks the item to delete

        container: ttk.Frame
            The frame containing the item to delete

        item_type: str, optional
            The type of input item to delete, include generic - None , "plan" and "step" (default None)

        Raises
        ------

        """
        if item_type == "plan" or item_type == "step":
            full_entry = entry_to_del
            entry_to_del = entry_to_del["Description"]
            entry_li.remove(full_entry)

        parent_name = entry_to_del.winfo_parent()
        parent = entry_to_del._nametowidget(parent_name)

        if item_type == "plan":
            grandparent_name = parent.winfo_parent()
            grandparent = parent._nametowidget(grandparent_name)
            grandparent.destroy()
        elif item_type == "step":
            if len(entry_li) == 0:
                add_step_button = ttk.Button(container, text="+ step",
                                             command=lambda: self.add_step_item(container, entry_li))
                add_step_button.pack(side=tk.TOP)
            parent.destroy()
        elif item_type is None:
            parent.destroy()
            entry_li.remove(entry_to_del)
        """
        Add one if none left and the item type is a plan or generic input row
        """
        if len(entry_li) == 0 and item_type is None:
            self.add_input_item(container, entry_li)

    def submit_entry(self, entry_type="Log"):
        """Retrieves user's input and save output to database

        Parameters
        ----------
        entry_type: str, optional
            What type of entry to save as, include "Log" and "Draft" (default "Draft")

        Raises
        ------

        """
        # Gratitude List
        gratitude_li = []
        for grat_entry in self.grat_entry_li:
            grat_txt = grat_entry.get()
            if grat_txt != "":
                gratitude_li.append(grat_txt.replace(",", "\comma"))

        # Goals List
        goals_li = []

        for goal_entry in self.goals_entry_li:
            goal_txt = goal_entry.get()
            if goal_txt != "":
                goals_li.append(goal_txt.replace(",", "\comma"))

        """
        Plans List:  {"Description": description entry box,
                           "Priority": priority combo box, "Steps": list of step entry boxes }
                           
        Step list: {"Description": new_step_box, "Status": check_var}
        """
        plans_li = []

        for plan_entry in self.plans_entry_li:
            if plan_entry["Description"].get() == "" and len(plan_entry["Steps"]) == 0:
                pass
            else:
                plan = {}
                plan["Plan_Type"] = plan_entry["Plan_Type"].get()
                plan["Description"] = plan_entry["Description"].get().replace(
                    ",", "\comma")
                plan["Status"] = plan_entry["Status"].get()
                plan["Priority"] = plan_entry["Priority"].get()
                plan["Steps"] = []
                for step_entry in plan_entry["Steps"]:
                    step_txt = step_entry["Description"].get()
                    if step_txt == "":
                        pass
                    else:
                        full_step = {"Status": step_entry["Status"].get(),
                                     "Description": step_txt}
                        plan["Steps"].append(full_step)
                plans_li.append(plan)

        # Affirmation Entry
        affirmation = self.affirm_entry.get("1.0", 'end-1c')

        # Additional Comment Entry
        additional_notes = self.notes_entry.get("1.0", 'end-1c')

        add_new_entry(entry_type=entry_type,
                      gratitude=gratitude_li,
                      goals=goals_li,
                      plans=plans_li,
                      affirmation=affirmation,
                      additional_notes=additional_notes)

        self.root.switch_page(self.root._HomePage)
