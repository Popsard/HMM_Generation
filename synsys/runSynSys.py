#!/usr/bin/python


from utils import *
from SyntheticEventDataGenerator import *
import pandas as pd
import numpy as np
import sys

def runDataGenerator(filename, numhmmstatesactivity, numhmmstatessensors, timeinterval, timestampmodeltype, main_event):

    #timeinterval = 6
    # This SyntheticEventGenerator object is in charge of generating acitivity and sensor event sequences
    syndatagenerator = SyntheticEventGenerator(filename, numhmmstatesactivity, numhmmstatessensors, timeinterval, timestampmodeltype, main_event)
    synthetic_df = syndatagenerator.run()
    
    #Suppression of the unused columns and processing of generated data
    
    index_num = []
    for i in range(1, len(synthetic_df)):
        row = synthetic_df.loc[i]
        if(pd.isnull(row["timestamp"])):
            index_num.append(i)
    synthetic_df.drop(index_num , inplace=True)
   
    synthetic_df = synthetic_df[["timestamp", "sensor_name", "sensor_state", "activity_name"]]

    synthetic_df.to_csv(r'data_generated.csv', index = False)
    
    print("Data Generated !")

"""
    #assemble the final synthetic data and print
    for i in range(1, len(synthetic_df)):
        row = synthetic_df.loc[i]
        if(not pd.isnull(row["timestamp"])):
            print(str(row["timestamp"]) + "," + row["sensor_name"] + "," + row["sensor_state"] + "," + row["activity_name"])
"""



#"/Users/jess/Desktop/HHdata/converted/Translated/DateRange/hh111week1"
if __name__ == "__main__":
    args = sys.argv
    filename = args[1]
    numhmmstatesactivity = int(args[2])
    numhmmstatessensors = int(args[3])
    timeinterval = int(args[4])
    timestampmodeltype = int(args[5])
    main_event = str(args[6])

    runDataGenerator(filename, numhmmstatesactivity, numhmmstatessensors, timeinterval, timestampmodeltype, main_event)


