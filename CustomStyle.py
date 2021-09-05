import pandas as pd

LABEL_FONT = ('TkDefaultFont', 12, 'bold')
SMALL_FONT = ('TkDefaultFont', 10, 'bold')
ANNOTATE_FONT = ('TkDefaultFont', 9, 'bold')

SMALL_BUTTON_WIDTH = 1
BIG_BUTTON_WIDTH = 10

SMALL_PAD = 5
LARGE_PAD = 10

COMP_COLOR = "#8CA53B"
INCOMP_COLOR = "#F72C25"
SCRAP_COLOR = "#2D1E2F"

MAIN_BG = '#ececec'
HIGHLIGHT_BG = "#5294e2"  # Baby blue
MID_BG = "#5c616c"  # dark blue grey
TEXT_BG = "#f2f4f5"  # mid grey

PLAN_STATUSES = ["Incomplete", "Completed", "Scrapped"]

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
