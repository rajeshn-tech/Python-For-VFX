"""
Project : Render Report Generator

Purpose:
This file is used for learning, testing,
and experimenting with code before moving
the final version to main.py.
"""

import pandas as pd

# Read Excel File
df = pd.read_excel("sample_input.xlsx")

# Display Complete Data
print(df)

# Display Column Names
print("\nColumns\n")
print(df.columns)

# Display First Five Rows
print("\nFirst Five Rows\n")
print(df.head())

# Display DataFrame Information
print("\nInformation\n")
df.info()

def find_column_name(df, *possible_names):
    pass

find_column_name(df, "Status", "status", "STATUS")
