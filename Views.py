"""
Icon Credit:
<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> 
from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
"""

import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter.constants import BOTH, S, TRUE
from ttkthemes import ThemedStyle
from AddEntryPage import AddEntryPage
from CustomWidgets import ScrollableFrame, DisplayOnlyText


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


LABEL_FONT = ('TkDefaultFont', 13, 'bold')
SMALL_FONT = ('TkDefaultFont', 9, 'bold')
SMALL_BUTTON_WIDTH = 1
BIG_BUTTON_WIDTH = 10

SMALL_PAD = 5
LARGE_PAD = 10


class SingleEntry(ttk.Frame):

    def __init__(self, parent, root, entry, *args, **kwargs):
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


class HomePage(ttk.Frame):
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

        self.entry_button = ttk.Button(self.menu_container, text="New Entry",
                                       command=lambda: root.switch_page(AddEntryPage))

        self.entry_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.draft_button = ttk.Button(self.menu_container, text="Drafts",
                                       command=lambda: root.switch_page(ViewDraftsPage))
        self.draft_button.pack(pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        self.quit_button = ttk.Button(self.menu_container, text="Quit",
                                      command=lambda: root.destroy())
        self.quit_button.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES)

        """
        Logs Pane
        """
        self.logs_container = ttk.Frame(self)
        self.logs_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD, expand=tk.YES, fill=BOTH)

        self.logs_label = ttk.Label(self.logs_container,
                                    text="Previous Entries", font=LABEL_FONT)
        self.logs_label.pack()

        self.logs_scrollframe = ScrollableFrame(self.logs_container)
        self.logs_scrollframe.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=tk.BOTH)

        # Initialize style
        s = ttk.Style()
        # Create style used by default for all Frames
        s.configure('Frame1.TFrame', background='#ececec')

        self.logs_scrollframe.scrollable_frame.config(style="Frame1.TFrame")

        """List of Logs"""

        self.test_entry = SingleEntry(
            self.logs_scrollframe.scrollable_frame, root, {'Date': '2018-09-10'})
        self.test_entry.pack(side=tk.TOP,
                             padx=SMALL_PAD, pady=SMALL_PAD
                             )

        self.test_entry_1 = SingleEntry(
            self.logs_scrollframe.scrollable_frame, root, {'Date': '2018-09-10'})
        self.test_entry_1.pack(side=tk.TOP,
                               padx=SMALL_PAD, pady=SMALL_PAD
                               )

        """
        Plans Pane
        """
        self.plans_container = ttk.Frame(self)
        self.plans_container.pack(
            side=tk.LEFT, padx=LARGE_PAD, pady=LARGE_PAD, expand=tk.YES, fill=BOTH)

        self.plans_label = ttk.Label(self.plans_container,
                                     text="Plans", font=LABEL_FONT)
        self.plans_label.pack()

        self.plans_scrollframe = ScrollableFrame(self.plans_container)

        self.plans_scrollframe.pack(
            pady=SMALL_PAD, padx=SMALL_PAD, expand=tk.YES, fill=BOTH)


class ViewDraftsPage(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)


class EditEntryPage(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)


class GratitudeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(700, 500)
        style = ThemedStyle(self)
        style.set_theme("arc")
        self._page = None
        self._HomePage = HomePage
        self.switch_page(self._HomePage)

    def switch_page(self, Page):
        new_page = Page(self)
        if self._page is not None:
            self._page.destroy()
        self._page = new_page
        self._page.pack(padx=LARGE_PAD, pady=LARGE_PAD,
                        expand=tk.YES, fill=tk.BOTH)


app = GratitudeApp()
app.mainloop()
