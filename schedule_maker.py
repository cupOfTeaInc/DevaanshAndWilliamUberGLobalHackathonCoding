import pandas as pd
import json

DATA_FILE_PATH = "sample_usage_data.csv"

df = pd.read_csv(DATA_FILE_PATH)

print(df)