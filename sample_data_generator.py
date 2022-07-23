import random
import pandas as pd
DATA_FILE_PATH = "sample_usage_data.csv"

sample_data = {}

for j in range(0, 2016):
    sample_data[str(j)] = {}
    sample_data[str(j)]["Device"] = "AC"
    sample_data[str(j)]["State"] = random.choice(["On", "Off"])
    sample_data[str(j)]["Time"] = (j * 5)

df = pd.DataFrame(data = sample_data)
df.to_csv(DATA_FILE_PATH)
