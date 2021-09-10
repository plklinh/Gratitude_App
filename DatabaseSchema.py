import pandas as pd
import sqlite3

conn = sqlite3.connect('Data_personal/GratitudeDatabase.db')

cursor = conn.cursor()

conn.execute("DROP TABLE IF EXISTS Entries")
conn.execute("DROP TABLE IF EXISTS Plans")
conn.execute("DROP TABLE IF EXISTS Steps")

sql = ''' CREATE TABLE IF NOT EXISTS Entries (
   Entry_ID PRIMARY KEY NOT NULL,
   Date TIMESTAMP NOT NULL,
   Entry_Type NOT NULL,
   Gratitude,
   Goals,
   Plans,
   Affirmation,
   Additional_Notes
)'''


cursor.execute(sql)

sql = ''' CREATE TABLE IF NOT EXISTS Entries (
   Entry_ID PRIMARY KEY NOT NULL,
   Date NOT NULL,
   Entry_Type NOT NULL,
   Gratitude,
   Goals,
   Plans,
   Affirmation,
   Additional_Notes
)'''


cursor.execute(sql)

sql = ''' CREATE TABLE IF NOT EXISTS Plans (
   Plan_ID PRIMARY KEY NOT NULL,
   Date_created NOT NULL,
   Plan_Type NOT NULL,
   Description,
   Num_Steps INTEGER,
   Status,
   Priority,
   Date_completed
)'''

cursor.execute(sql)


sql = ''' CREATE TABLE IF NOT EXISTS Steps (
   Plan_ID NOT NULL,
   Description,
   Status,
   Date_completed
)'''

cursor = conn.cursor()
cursor.execute(sql)

# Import Entries
entries = pd.read_csv("Data_personal/entries_df.csv")
entries.to_sql("Entries", conn, if_exists='append', index=False)

# Import Plans
plans = pd.read_csv("Data_personal/plans_df.csv")
plans.to_sql("Plans", conn, if_exists='append', index=False)

# Import Steps
steps = pd.read_csv("Data_personal/steps_df.csv")
steps.to_sql("Steps", conn, if_exists='append', index=False)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()

"""
TEST DATABASE
"""

conn = sqlite3.connect('Data/TestDatabase.db')

cursor = conn.cursor()

sql = ''' CREATE TABLE IF NOT EXISTS Entries (
   Entry_ID PRIMARY KEY NOT NULL,
   Date TIMESTAMP NOT NULL,
   Entry_Type NOT NULL,
   Gratitude,
   Goals,
   Plans,
   Affirmation,
   Additional_Notes
)'''


cursor.execute(sql)

sql = ''' CREATE TABLE IF NOT EXISTS Entries (
   Entry_ID PRIMARY KEY NOT NULL,
   Date NOT NULL,
   Entry_Type NOT NULL,
   Gratitude,
   Goals,
   Plans,
   Affirmation,
   Additional_Notes
)'''


cursor.execute(sql)

sql = ''' CREATE TABLE IF NOT EXISTS Plans (
   Plan_ID PRIMARY KEY NOT NULL,
   Date_created NOT NULL,
   Plan_Type NOT NULL,
   Description,
   Num_Steps INTEGER,
   Status,
   Priority,
   Date_completed
)'''

cursor.execute(sql)


sql = ''' CREATE TABLE IF NOT EXISTS Steps (
   Plan_ID NOT NULL,
   Description,
   Status,
   Date_completed
)'''

cursor = conn.cursor()
cursor.execute(sql)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
