from CustomStyle import MOCK_ENTRY
import pandas as pd
import numpy as np
import sqlite3

DB_FILE = "Data_personal/GratitudeDatabase.db"

ENTRY_TBL = "Entries"

PLAN_TBL = "Plans"

STEPS_TBL = "Steps"


def convert_str_to_li(str):
    """
    Converts a string to a list. Strings must be in the the format [string 1,string 2,..]
    """
    if str is None:
        return []
    else:
        li = str[1:-1].split(",")
        for i in range(len(li)):
            li[i] = li[i].replace("\comma", ",")
        return li


def convert_li_to_str(li):
    """
    Converts a list of strings to a string. Resulting string is in the the format [string 1,string 2,..]
    Any commas are replaced with \comma
    """
    for i in range(len(li)):
        li[i] = li[i].replace(",", "\comma")
    str = "["+",".join(li)+"]"
    return str


def connect_db():
    conn = sqlite3.connect(DB_FILE)
    return conn


def read_all_entries():
    conn = connect_db()
    df = pd.read_sql("SELECT * from " + ENTRY_TBL,
                     conn,
                     # index_col="Entry_ID",
                     parse_dates=["Date"])

    for col in ["Gratitude", "Goals", "Plans"]:
        df[col] = df[col].apply(lambda x: convert_str_to_li(x))

    conn.close()
    return df


def read_all_plans():
    conn = connect_db()
    plan_df = pd.read_sql("SELECT * from " + PLAN_TBL,
                          conn,
                          parse_dates=["Date_created", "Date_completed"])
    step_df = pd.read_sql("SELECT * from " + STEPS_TBL,
                          conn,
                          parse_dates=["Date_completed"])
    conn.close()
    return plan_df, step_df


def filter_entries(sql_cmd):
    conn = connect_db()
    df = pd.read_sql(sql_cmd,
                     conn,
                     # index_col="Entry_ID",
                     parse_dates=["Date"])

    for col in ["Gratitude", "Goals", "Plans"]:
        df[col] = df[col].apply(lambda x: convert_str_to_li(x))

    conn.close()
    return df


def get_latest_log():
    sql_cmd = ''' SELECT * from ''' + ENTRY_TBL + '''
            WHERE Entry_Type = "Log"
            ORDER BY Entry_ID DESC LIMIT 1'''

    latest_entry = filter_entries(sql_cmd)

    return next(filter_entries(sql_cmd).itertuples())


def get_all_logs():
    sql_cmd = ''' SELECT * from ''' + ENTRY_TBL + '''
            WHERE Entry_Type = "Log"
            ORDER BY Entry_ID DESC LIMIT 5'''

    logs_df = filter_entries(sql_cmd)
    return logs_df


def get_all_drafts():
    sql_cmd = ''' SELECT * from ''' + ENTRY_TBL + '''
            WHERE Entry_Type = "Draft"
            ORDER BY Entry_ID DESC  LIMIT 5'''

    logs_df = filter_entries(sql_cmd)
    return logs_df


def add_entry(entry_obj, plan_obj, step_obj):
    conn = connect_db()
    cursor = conn.cursor()
    # Add Entry

    # Add any plans

    # Add any steps

    conn.close()


def update_entry(conn, sql_cmd):
    conn.cursor().execute(sql_cmd)
    conn.commit()


def match_plans(entry_df):
    if len(entry_df.Plans) == 0:
        return None
    conn = connect_db()
    sql = '''SELECT * from ''' + PLAN_TBL + '''
            WHERE Plan_ID IN ("''' + '","'.join(entry_df.Plans) + '''")'''
    plans = pd.read_sql(sql, conn)
    return plans


def match_steps(plan_df):
    if plan_df.Num_Steps == 0:
        return None
    conn = connect_db()
    sql = '''SELECT * from ''' + STEPS_TBL + '''
            WHERE Plan_ID = "''' + plan_df.Plan_ID + '''"'''
    steps = pd.read_sql(sql, conn)
    return steps


if __name__ == "__main__":
    # df = pd.read_csv("Data_personal/entries.csv")
    # for col in ["Gratitude", "Goals", "Plans"]:
    #     df[col] = df[col].apply(lambda x: convert_str_to_li(x))
    # print(df["Gratitude"])
    # all_entries.to_csv("entries.csv")

    li = ['Nature',  'The Library',  'The Bus driver']

    print(convert_str_to_li(str))
