import pandas as pd
import numpy as np
import sqlite3

DB_FILE = "Data_personal/Grat_Database.db"

ENTRY_TBL = "Entries"

PLAN_TBL = "Plans"

STEPS_TBL = "Steps"


def connect_db():
    conn = sqlite3.connect(DB_FILE)
    return conn


def convert_stl(str):
    return str[1:-1].split(',') if str is not None else []


def read_all_entries():
    conn = connect_db()
    df = pd.read_sql("SELECT * from " + ENTRY_TBL,
                     conn,
                     index_col="Entry_ID",
                     parse_dates=["Date"])

    for col in ["Gratitude", "Goals", "Plans"]:
        df[col] = df[col].apply(lambda x: convert_stl(x))

    conn.close()
    return df


def read_all_plans():
    conn = connect_db()
    plan_df = pd.read_sql("SELECT * from " + ENTRY_TBL,
                          conn,
                          index_col="Entry_ID",
                          parse_dates=["Date_created", "Date_completed"])
    step_df = pd.read_sql("SELECT * from " + ENTRY_TBL,
                          conn,
                          index_col="Entry_ID",
                          parse_dates=["Date_completed"])
    conn.close()
    return plan_df, step_df


def filter_entries(sql_cmd):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(sql_cmd)
    result = cursor.fetchall()
    conn.close()
    return result


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


if __name__ == "__main__":
    df = read_all_entries()
    print(df.dtypes)

    plans, steps = read_all_plans()
    print(plans.dtypes)
    print(steps.dtypes)
