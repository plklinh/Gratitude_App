import pandas as pd
import sqlite3

# Establish Connections
conn = sqlite3.connect('Data_personal/Grat_Database.db')

# Import Entries
entries = pd.read_csv("Data_personal/entries_df.csv")
entries.to_sql("Entries", conn, if_exists='replace', index=False)

# Import Plans
plans = pd.read_csv("Data_personal/plans_df.csv")
plans.to_sql("Plans", conn, if_exists='replace', index=False)

# Import Steps
steps = pd.read_csv("Data_personal/steps_df.csv")
plans.to_sql("Steps", conn, if_exists='replace', index=False)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
