from os import read
from typing import NamedTuple
from Models.Entry import Entry, EntryType
import pandas as pd
import numpy as np


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


ENTRY_FILE = "Data/entries_df.csv"

PLAN_FILE = "Data/plans_df.csv"

STEPS_FILE = "Data/steps_df.csv"


def convert_stl(str):
    return str[1:-1].split(',') if str is not pd.NA else []


def read_entries():
    df = pd.read_csv(ENTRY_FILE,
                     index_col=[0], dtype={
                         "Entry_Type": 'string',
                         "Affirmation": 'string',
                         "Additional_Notes": 'string'},
                     converters={'Gratitude': lambda x: convert_stl(x),
                                 'Goal': lambda x: convert_stl(x),
                                 'Plan': lambda x: convert_stl(x),
                                 },
                     parse_dates=["Date"])
    return df


def read_plans():
    plan_df = pd.read_csv(PLAN_FILE, parse_dates=["Date_created"])
    step_df = pd.read_csv(STEPS_FILE)
    return plan_df, step_df


def add_entry(new_entry_df):
    new_entry_df.to_csv('entries_df.csv', mode='a', header=False, index=False)


def get_entry_type(data, type_code):
    entry_type = ""
    if type_code == "l":
        entry_type = "Log"
    else:
        entry_type = "Draft"
    return data[data["Entry_Type"] == entry_type]


def print_logs(log):
    printed_log = ""

    printed_log += color.BOLD + "Date: " + color.END + log["Date"] + "\n"
    printed_log += color.BOLD + "Gratitude: \n " + color.END
    printed_log += "\n".join(log["Gratitude"].split(";"))

    printed_log += color.BOLD + "\nGoal: \n " + color.END
    printed_log += "\n".join(log["Goal"].split(";"))

    printed_log += color.BOLD + "\nPlan: \n " + color.END
    printed_log += "\n".join(log["Plan"].split(";"))

    printed_log += color.BOLD + "\nAffirmation: \n" + color.END
    printed_log += "\n".join(log["Affirmation"].split(";"))

    if log["Additional_Notes"] is not np.NaN:
        printed_log += color.BOLD + "\nAdditional Notes: \n " + color.END
        printed_log += log["Additional_Notes"]
    return printed_log


if __name__ == "__main__":
    entries = read_entries()
