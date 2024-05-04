#!/usr/bin/env python3

import pandas as pd
from pandasql import sqldf

# Sample DataFrame
df = pd.read_csv('fitness_log.csv')
breakpoint()

# Define a function to execute SQL queries
def execute_query(query):
    return sqldf(query)

# Read-eval-print loop
while True:
    user_query = input("Enter your SQL query (or 'exit' to quit): ")
    
    if user_query.lower() == 'exit':
        print("Exiting...")
        break
    
    try:
        result_df = execute_query(user_query)
        print("Result:")
        print(result_df)
    except Exception as e:
        print("Error:", e)
