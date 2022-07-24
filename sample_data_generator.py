import random
import pandas as pd

DATA_FILE_PATH : str = "sample_usage_data.csv"



def week_day():
    sample_data    : dict = {} # create dict to make dataframe w
    work_from_home : int  = random.choices([1, 0])[0]

    """
    This loop randomly generates sample data for one week (2016 = 7 days * 288 5-min intervals per day) 
    This is how we expect to query the data from our Core (Home Assistant for now) in the future. We will get data for every 5 minute interval 
    """

    for j in range(0, 120): # Midnight to early morning                    
        sample_data[str(j)]           = {} # create dict nested in sample_data so the keys we use below exist
        sample_data[str(j)]["Device"] = "AC"
        sample_data[str(j)]["State"]  = random.choices(["On", "Off"], weights=[0.7, 0.3])[0]
        sample_data[str(j)]["Time"]   = (j % 288) * 5

    for j in range(120, 1992): # Morning to night      
        sample_data[str(j)]           = {} # create dict nested in sample_data so the keys we use below exist
        sample_data[str(j)]["Device"] = "AC"
        sample_data[str(j)]["State"]  = random.choices(["On", "Off"], weights=[work_from_home, 1-work_from_home])[0]
        sample_data[str(j)]["Time"]   = (j % 288 ) * 5

    for j in range(1992, 2016): # Night to midnight     
        sample_data[str(j)]           = {} # create dict nested in sample_data so the keys we use below exist
        sample_data[str(j)]["Device"] = "AC"
        sample_data[str(j)]["State"]  = random.choices(["On", "Off"], weights=[0.8, 0.2])[0]
        sample_data[str(j)]["Time"]   = (j % 288 ) * 5

    return sample_data

def weekend():
    sample_data : dict = {} # create dict to make dataframe with

    # Same code as before, just for a weekend
    
    for j in range(0, 120):                  
        sample_data[str(j)]           = {} # create dict nested in sample_data so the keys we use below exist
        sample_data[str(j)]["Device"] = "AC"
        sample_data[str(j)]["State"]  = random.choices(["On", "Off"], weights=[0.7, 0.3])[0]
        sample_data[str(j)]["Time"]   = (j % 288 ) * 5

    for j in range(120, 1992):       
        sample_data[str(j)]           = {} # create dict nested in sample_data so the keys we use below exist
        sample_data[str(j)]["Device"] = "AC"
        sample_data[str(j)]["State"]  = random.choices(["On", "Off"], weights=[0.6, 0.4])[0]
        sample_data[str(j)]["Time"]   = (j % 288 ) * 5

    for j in range(1992, 2016):       
        sample_data[str(j)]           = {} # create dict nested in sample_data so the keys we use below exist
        sample_data[str(j)]["Device"] = "AC"
        sample_data[str(j)]["State"]  = random.choices(["On", "Off"], weights=[0.8, 0.2])[0]
        sample_data[str(j)]["Time"]   = (j % 288 ) * 5

    return sample_data

df = pd.DataFrame(data = weekend()) # create datafram from dict
df.to_csv(DATA_FILE_PATH) # saving data to use in schedule_maker.py
