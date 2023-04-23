import csv
import pandas as pd
import ast
import matplotlib.pyplot as plt
import datetime
import numpy as np

df = pd.read_csv("/home/acefly/robot_fib/plot_v2/faulty_joint_states_2023-03-20-00-06-17-joint_states.csv")
from datetime import datetime, timedelta
# input and output file paths
input_file = "/home/acefly/robot_fib/plot_v2/faulty_joint_states_2023-03-20-00-06-17-joint_states.csv"
output_file = 'output.csv'

# columns that contain tuple values
tuple_columns = ['.position']

time = ["time"]
names_list2 = []

names_list2.append(time)

names_list = df[".name"].values[0]

names_list_3 = ast.literal_eval(names_list)


with open(input_file, 'r') as csv_file, open(output_file, 'w', newline='') as output_csv_file:
    reader = csv.DictReader(csv_file)
    writer = csv.writer(output_csv_file)

    # write header row to output CSV file
    header = names_list_3
    writer.writerow(header)

    # loop through rows in input CSV file
    for row in reader:
        # extract tuple values from selected columns
        tuple_values = []
        for col in tuple_columns:
            if row[col].startswith('(') and row[col].endswith(')'):
                tuple_values.extend(list(eval(row[col])))
            else:
                tuple_values.extend(['', ''])

        # write ID and tuple values to output CSV file
        writer.writerow(tuple_values)


df_out = pd.read_csv("/home/acefly/robot_fib/output.csv")

df_out.insert(0,'time', df["time"] )


df_out["time"] = pd.to_datetime(df["time"]).astype(str)

df_out[['Date', 'time_series']] = df_out["time"].str.split(" ", expand = True)



df_out['time_series'] = pd.to_datetime(df_out['time_series'].astype(str))


df_plannig_flg = pd.read_csv("/home/acefly/robot_fib/plot_v2/planning_flag_2023-03-20-00-06-41-planning.csv")

df_out["planning"] = df_plannig_flg[".data"]

plt.plot(df_out['time_series'], df_out['panda_joint3'])

df_out.set_index('time_series', inplace=True)


for idx, row in df_out.iterrows():
    if row['planning']:
        plt.axvspan(idx, idx+pd.Timedelta(minutes=1), alpha=0.3, color='green')

#plt.xticks(pd.date_range(start=df_out['time_series'].min(), end=df_out['time_series'].max(), freq='Min'))
plt.show()
print(df_out)
df_out.to_csv("test.csv")
