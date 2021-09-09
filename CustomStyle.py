import pandas as pd

LARGE_LABEL_FONT = ('TkDefaultFont', 15, 'bold')
SMALL_LABEL_FONT = ('TkDefaultFont', 13, 'bold')

SMALL_FONT = ('TkDefaultFont', 12)
ANNOTATE_FONT = ('TkDefaultFont', 10, 'bold')

SMALL_BUTTON_WIDTH = 1
BIG_BUTTON_WIDTH = 10

SMALL_PAD = 5
LARGE_PAD = 10

MAIN_BG = '#ececec'
HIGHLIGHT_BG = "#5294e2"  # Baby blue
MID_BG = "#5c616c"  # dark blue grey
TEXT_BG = "#f2f4f5"  # mid grey

PLAN_STATUSES = ["Incomplete", "Completed", "Scrapped"]

COMP_COLOR = "#00B884"  # Green
INCOMP_COLOR = "#DF2935"  # Red
SCRAP_COLOR = "#0A2E36"  # Blackish green

PRIORITY_LVL = ["High", "Medium", "Low", ""]

HIGHP_COLOR = "#C53F2D"  # Red
MEDP_COLOR = "#F28705"  # Orange
LOWP_COLOR = "#EBC62A"  # Yellow


CONTAINER_STYLE = "Frame1.TFrame"

COMBOBOX_STYLE = 'Combo1.TCombobox'

MENUBUTTON_STYLE = 'Menu1.TMenubutton'

MOCK_ENTRY = {"Entry_ID": "E21080300",
              "Date": pd.to_datetime("2021-08-03"),
              "Entry_Type": "Log",
              "Gratitude": ['My mum for packing antibiotics', 'Google', 'Funny Youtubers'],
              "Goals": ['Be committed and start project '],
              "Plans": ['P21080302', 'P21080500'],
              "Affirmation": "I am making progress with the app",
              "Additional_Notes": None}

MOCK_DRAFT = {"Entry_ID": 'E21082300',
              "Date": pd.to_datetime("2021-08-03"),
              "Entry_Type": "Draft",
              "Gratitude": ['My mum for packing antibiotics', 'Funny Youtubers'],
              "Goals": ['Be committed and start project '],
              "Plans": ['P21082300'],
              "Affirmation": "Not Spiral",
              "Additional_Notes": None}
