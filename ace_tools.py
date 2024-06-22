# ace_tools.py
import pandas as pd

def display_dataframe_to_user(name, dataframe):
    print(f"{name} DataFrame:")
    print(dataframe.head())
