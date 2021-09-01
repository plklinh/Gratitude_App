import tkinter as tk
from tkinter import PhotoImage, ttk
from ttkthemes import ThemedStyle
from EntryAddPage import AddEntryPage
from EntryEditPage import EditEntryPage
from CustomWidgets import ScrollableFrame, DisplayOnlyText
from CustomStyle import *


class SingleEntry(ttk.Frame):

    def __init__(self, parent, root, entry, mode="full", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        pencil_icon = PhotoImage(file="Icon/pencil.png").subsample(4, 4)
        trash_icon = PhotoImage(file="Icon/trash.png").subsample(4, 4)
        eye_icon = PhotoImage(file="Icon/eye.png").subsample(4, 4)

        """
        Date
        """
        self.date_row = ttk.Frame(self)
        self.date_row.pack(side=tk.TOP, fill=tk.X,
                           padx=SMALL_PAD, pady=SMALL_PAD)

        self.date_lab = ttk.Label(
            self.date_row,
            text="Time: ",
            font=LABEL_FONT)
        self.date_lab.pack(side=tk.LEFT, anchor='nw')

        self.date_lab = ttk.Label(
            self.date_row,
            text=entry['Date'])
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

        self.gratitude_entry = DisplayOnlyText(self, height=2)
        self.gratitude_entry.pack(
            side=tk.TOP, expand=True, fill=tk.X,
            padx=SMALL_PAD, pady=SMALL_PAD)

        self.gratitude_entry.configure(state='normal')
        self.gratitude_entry.insert(
            'end', '• Some Text(base)\nTraceback (most recent call last):')
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

        self.goals_entry = DisplayOnlyText(self, height=2)
        self.goals_entry.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X, anchor='nw',
            padx=SMALL_PAD, pady=SMALL_PAD)

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

        plans_entry = DisplayOnlyText(self, height=2)
        plans_entry.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, anchor='nw',
                         padx=SMALL_PAD, pady=SMALL_PAD)

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

        self.affirm_entry = DisplayOnlyText(self, height=2)

        self.affirm_entry.pack(
            side=tk.TOP, expand=tk.YES, fill=tk.X, anchor='nw',
            padx=SMALL_PAD, pady=SMALL_PAD)

        """
        Note
        """

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
                                      command=lambda: root.switch_page(EditEntryPage))
        self.edit_button.image = pencil_icon
        self.edit_button.pack(side=tk.LEFT)

        self.delete_button = ttk.Button(self.options_row,
                                        text="Delete",
                                        image=trash_icon)
        self.delete_button.image = trash_icon
        self.delete_button.pack(side=tk.LEFT)

    def FullView():
        win = tk.Toplevel()
        win.wm_title("Full Entry")

        l = tk.Label(win, text="Input")
        l.grid(row=0, column=0)

        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.grid(row=1, column=0)
