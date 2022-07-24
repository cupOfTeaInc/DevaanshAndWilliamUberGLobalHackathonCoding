import pandas as pd
import json

DATA_FILE_PATH     : str = "sample_usage_data.csv" # if getting data from Home Assistant via data_collection.py, name would be usage_data.csv
SCHEDULE_FILE_PATH : str = "schedule.json"
usage_data : pd.DataFrame = pd.read_csv(DATA_FILE_PATH)

def make_schedule(device : str, size : int = 288): # Makes schedule for specified device size is the amount of intervals in the dau. There are 288 5-min intervals in a day
    line_list  : dict         = {"State":[], "Time":[]}

    for index, row in usage_data.iteritems(): # cpmverts "on" and "off" to 1 and 0.
        if row[0] == device: # only make schedule for specified device
            if row[1] == "On" : line_list["State"].append(1)
            else              : line_list["State"].append(0)

            line_list["Time"].append(int(index.replace("Unnamed: ", ""))*5) # Filters out 1st column; Unnamed: is removed from 1st column

    line_list_df = pd.DataFrame(data=line_list) # Converts the line_list, which is a dict to a pandas df.
    line  : dict = {"State":[], "Time":[]}
    
    for i in range(size):
        line["State"].append(line_list_df[line_list_df['Time'] == i*5]["State"].mean()) # Averages all values at same point in time
        line["Time"] .append(i*5)

    line : pd.DataFrame = pd.DataFrame(data=line)
    print(type(line["State"]))
    line["State"] = line["State"].rolling(window=8, min_periods=0).mean() # moving average so the device doesn't "flicker"(one part on, one part off, one part on...)
    line["State"] = line["State"].round() # turns line into state at given time 1 being on and 0 being off

    return line # Returns the line which is a pandas df

def make_schedule_for_all(): # Makes schedule for all devices
    ret : dict = {}
    print(usage_data)
    for device_name in set(usage_data.iloc[0][1:]):
        print(device_name)
        m = make_schedule(device_name)
        output : list = []
        for point in m["State"]:
            output.append(int(point))

        ret[device_name] = output
    
    json.dump(ret, open(SCHEDULE_FILE_PATH, "w")) # Output to JSON file

    return ret

if __name__ == "__main__":
    make_schedule_for_all()