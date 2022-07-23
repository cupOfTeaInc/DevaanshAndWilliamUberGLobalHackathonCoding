import pandas as pd
import random

DATA_FILE_PATH = "sample_usage_data.json"

sample_data = {}

for i in range(0, 288):
    sample_data[i] = {}
    sample_data[i]["device"] = "AC"
    sample_data[i]["action"] = random.choice(["On", "Off"])
    sample_data[i]["mins"] = i * 5

df = pd.DataFrame(data=sample_data)

with open(DATA_FILE_PATH, "w") as f:
    f.write(str(sample_data))

