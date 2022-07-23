import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE_PATH : str = "sample_usage_data.csv"

def make_schedule(size : int = 288):
    usage_data : pd.DataFrame = pd.read_csv(DATA_FILE_PATH)
    line_list  : dict         = {"State":[], "Time":[]}

    for index, row in usage_data.iteritems():
        if row[1] == "On" : line_list["State"].append(1)
        else              : line_list["State"].append(0)

        line_list["Time"].append(int(index.replace("Unnamed: ", ""))*5)

    line_list_df = pd.DataFrame(data=line_list)
    line  : dict = {"State":[], "Time":[]}
    
    for i in range(size):
        line["State"].append(line_list_df[line_list_df['Time'] == i*5]["State"].mean())
        line["Time"] .append(i*5)

    line : pd.DataFrame = pd.DataFrame(data=line)
    print(type(line["State"]))
    line["State"] = line["State"].rolling(window=).mean()#moving averaege so the device dosent "flicker"(one part on, one part off, one part on...)
    
    
    return line

if __name__ == "__main__":
    m = make_schedule()
    m.plot.scatter(x="Time", y="State")
    plt.show()