from CustomStyle import TESTING
import datetime
import pandas as pd
import numpy as np
import sqlite3

DB_FILE = "Data_personal/GratitudeDatabase.db"

TEST_DB = "Data/TestDatabase.db"

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


def connect_db(test=False):
    db = DB_FILE
    if test:
        db = TEST_DB
    conn = sqlite3.connect(db, isolation_level=None)
    return conn


""" Entry Methods """


def read_all_entries(test=False):
    conn = connect_db(test=test)
    df = pd.read_sql("SELECT * from " + ENTRY_TBL,
                     conn,
                     parse_dates=["Date"])

    for col in ["Gratitude", "Goals", "Plans"]:
        df[col] = df[col].apply(lambda x: convert_str_to_li(x))

    conn.close()
    return df


def filter_entries(sql_cmd, test=False):
    conn = connect_db(test=test)
    df = pd.read_sql(sql_cmd,
                     conn,
                     parse_dates=["Date"])

    for col in ["Gratitude", "Goals", "Plans"]:
        df[col] = df[col].apply(lambda x: convert_str_to_li(x))

    df = df.fillna(value="")

    conn.close()
    return df


def get_latest_log(test=False):
    sql_cmd = ''' SELECT * from ''' + ENTRY_TBL + '''
            WHERE Entry_Type = "Log"
            ORDER BY Entry_ID DESC LIMIT 1'''

    latest_entry = filter_entries(sql_cmd, test=test)

    return next(latest_entry.itertuples())


def get_all_logs(test=False):
    sql_cmd = ''' SELECT * from ''' + ENTRY_TBL + '''
            WHERE Entry_Type = "Log"
            ORDER BY Entry_ID DESC LIMIT 5'''

    logs_df = filter_entries(sql_cmd, test=test)
    return logs_df


def get_all_drafts(test=False):
    sql_cmd = ''' SELECT * from ''' + ENTRY_TBL + '''
            WHERE Entry_Type = "Draft"
            ORDER BY Entry_ID DESC  LIMIT 5'''

    logs_df = filter_entries(sql_cmd, test=test)
    return logs_df


def update_entry(conn, sql_cmd, test=False):
    conn.cursor().execute(sql_cmd)
    conn.commit()


""" Plan Methods """


def get_all_logged_plans(test=False):
    conn = connect_db(test=test)
    plan_df = pd.read_sql("SELECT * from " + PLAN_TBL + """
                          WHERE Plan_Type = "Log"
                          ORDER BY Plan_ID""",
                          conn,
                          parse_dates=["Date_created", "Date_completed"])
    conn.close()
    return plan_df


def get_all_draft_plans(test=False):
    conn = connect_db(test=test)
    plan_df = pd.read_sql("SELECT * from " + PLAN_TBL + """
                          WHERE Plan_Type = "Draft"
                          ORDER BY Plan_ID""",
                          conn,
                          parse_dates=["Date_created", "Date_completed"])
    conn.close()
    return plan_df


def get_latest_incomp_plans(test=False):
    sql_cmd = ''' SELECT * from ''' + PLAN_TBL + '''
            WHERE Status = "Incomplete" AND Plan_Type = "Log"
            ORDER BY Plan_ID DESC LIMIT 5'''

    conn = connect_db(test=test)
    df = pd.read_sql(sql_cmd,
                     conn,
                     parse_dates=["Date_created", "Date_completed"])
    df = df.fillna(value="")

    conn.close()
    return df


def get_draft_plans(test=False):
    sql_cmd = ''' SELECT * from ''' + PLAN_TBL + '''
            WHERE Status = "Incomplete" AND Plan_Type = "Log"
            ORDER BY Plan_ID DESC LIMIT 5'''

    conn = connect_db(test=test)
    df = pd.read_sql(sql_cmd,
                     conn,
                     parse_dates=["Date_created", "Date_completed"])
    df = df.fillna(value="")

    conn.close()
    return df


def match_plans(entry_df, test=False):
    if len(entry_df.Plans) == 0:
        return None
    conn = connect_db(test=test)
    sql = '''SELECT * from ''' + PLAN_TBL + '''
            WHERE Plan_ID IN ("''' + '","'.join(entry_df.Plans) + '''")'''
    plans = pd.read_sql(sql, conn)
    plans = plans.fillna(value="")
    conn.close()
    return plans


def match_steps(plan_df, test=False):
    if plan_df.Num_Steps == 0:
        return None
    conn = connect_db(test=test)
    sql = '''SELECT * from ''' + STEPS_TBL + '''
            WHERE Plan_ID = "''' + plan_df.Plan_ID + '''"'''
    steps = pd.read_sql(sql, conn)
    steps = steps.fillna(value="")
    return steps


"""Add Methods"""


def add_new_entry(entry_type, gratitude, goals, plans, affirmation, additional_notes, test=False):

    conn = connect_db(test=test)

    cursor = conn.cursor()

    date_created = datetime.date.today()

    # Add any plans
    plans_ids = []
    plans_df = []

    if len(plans) != 0:
        sql = '''SELECT Plan_ID from ''' + PLAN_TBL + '''
            WHERE Plan_ID LIKE "P''' + date_created.strftime("%y%m%d") + '''%"'''

        same_day_plan_ids = pd.read_sql(sql, conn)

        num_same_day = len(same_day_plan_ids)

        sql = '''INSERT INTO ''' + PLAN_TBL + ''' (Plan_ID,Date_created,Plan_Type,Description, Num_Steps,Status,Priority,Date_completed)
                VALUES '''

        for plan in plans:
            plan_df = add_new_plan(plan_type=plan["Plan_Type"],
                                   desc=plan["Description"],
                                   status=plan["Status"],
                                   priority=plan["Priority"],
                                   steps=plan["Steps"],
                                   prev_conn=conn,
                                   num_same_day=num_same_day,
                                   test=test)
            num_same_day += 1
            plans_df.append(plan_df)
            plans_ids.append(plan_df["Plan_ID"][0])

        plans_df = pd.concat(plans_df)

        plans_df.to_sql(name=PLAN_TBL,
                        con=conn,
                        schema="TestDatabase.db",
                        if_exists="append",
                        index=False,
                        method="multi")

    # Add Entry

    sql = '''SELECT Entry_ID from ''' + ENTRY_TBL + '''
            WHERE Entry_ID LIKE "E''' + date_created.strftime("%y%m%d") + '''%"'''

    same_day_entry_ids = pd.read_sql(sql, conn)

    entry_id = "E"+date_created.strftime("%y%m%d")

    num_same_day = len(same_day_entry_ids)

    if num_same_day > 9:
        entry_id = entry_id+str(num_same_day)
    else:
        entry_id = entry_id+"0"+str(num_same_day)

    entry_df = pd.DataFrame(data={"Entry_ID": [entry_id],
                                  "Date": [date_created],
                                  "Entry_Type": [entry_type],
                                  "Gratitude": [convert_li_to_str(gratitude)],
                                  "Goals": [convert_li_to_str(goals)],
                                  "Plans": [convert_li_to_str(plans_ids)],
                                  "Affirmation": [affirmation],
                                  "Additional_Notes": [additional_notes]
                                  })
    print(entry_df)

    entry_df.to_sql(ENTRY_TBL,
                    conn,
                    if_exists="append",
                    index=False)

    conn.commit()

    conn.close()


def add_new_plan(plan_type, desc, status, priority, steps, prev_conn=None, num_same_day=0, test=False):

    # Add plan
    date_created = datetime.date.today()

    if prev_conn is None:
        conn = connect_db(test=test)
        sql = '''SELECT Plan_ID from ''' + PLAN_TBL + '''
            WHERE Date_created="''' + date_created.strftime("%Y-%m-%d") + '''"'''

        same_day_plan_ids = pd.read_sql(sql, conn)

        num_same_day = len(same_day_plan_ids)

    else:
        conn = prev_conn

    plan_id = "P"+date_created.strftime("%y%m%d")

    if num_same_day > 9:
        plan_id = plan_id+str(num_same_day)
    else:
        plan_id = plan_id+"0"+str(num_same_day)

    num_steps = len(steps)

    plan_df = pd.DataFrame(data={"Plan_ID": [plan_id],
                                 "Date_created": [date_created],
                                 "Plan_Type": [plan_type],
                                 "Description": [desc],
                                 "Num_Steps": [num_steps],
                                 "Status": [status],
                                 "Priority": [priority],
                                 "Date_completed": [date_created if status == "Completed" else None]
                                 })

    for step in steps:
        step["Plan_ID"] = plan_id
        step["Date_completed"] = date_created if step["Status"] == "Completed" else None

    pd.DataFrame(steps).to_sql(STEPS_TBL,
                               conn,
                               if_exists="append",
                               index=False)

    if prev_conn is None:
        plan_df.to_sql(PLAN_TBL,
                       conn,
                       if_exists="append",
                       index=False)
        conn.close()
        return None
    else:
        return plan_df


if __name__ == "__main__":

    print(get_latest_log(test=TESTING))

    sql_cmd = ''' SELECT * from ''' + STEPS_TBL

    conn = connect_db(test=TESTING)
    df = pd.read_sql(sql_cmd,
                     conn,
                     parse_dates=["Date_created", "Date_completed"])
    df = df.fillna(value="")
    print(df)

    print(get_latest_incomp_plans(test=TESTING))
    pass
