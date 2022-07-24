import sqlite3
from datetime import datetime, timedelta
import pandas as pd

DATA_FILE_PATH : str = "usage_data.csv"

def get_usage_data(device : str, nickname : str):
    conn = sqlite3.connect('.homeassistant/home-assistant_v2.db')

    c    = conn.cursor()

    c.execute(f"SELECT entity_id, state, last_updated FROM states WHERE entity_id = '{device}'")

    items             = c.fetchall()
    usage_data : dict = {}

    for i in range(len(items)):
        usage_data[str(i)] = {}
        usage_data[str(i)]["Device"] = nickname
        usage_data[str(i)]["State"]  = items[i][1]
        usage_data[str(i)]["Time"]   = items[i][2]

    for i in usage_data.items():
        tm = datetime.strptime(i[1]["Time"], '%Y-%m-%d %H:%M:%S.%f')
        tm = tm - timedelta(minutes=tm.minute % 5,
                                seconds=tm.second,
                                microseconds=tm.microsecond)

        usage_data[i[0]]["Time"] = ((tm.hour*60 + tm.minute)/5)
        
        if i[1]["State"] == "heat":  usage_data[i[0]]["State"] = "On"
        else                      :  usage_data[i[0]]["State"] = "Off"

    conn.close()

    df = pd.DataFrame(data = usage_data)

    return df.to_csv()

if __name__ == "__main__":
    get_usage_data()