import bagpy
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
import rosbag
from os import listdir
from rosbags.dataframe import get_dataframe
from rosbags.highlevel import AnyReader

from pathlib import Path

folder = "/home/acefly/robot_fib/data_v4/"



from os.path import isfile, join
onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]

collision_list = []
faults_list = []
fault_flag_list = []
fault_state_list = []
fault_joint_states_list = []
faulty_robot_states_list = []
real_joint_states_list = []
rosout_list = []
fault_effect_list = []

collision_key = "check_collision"
faults_key = "faults"
fault_flag_key = "fault_flag"
fault_state_key = "fault_state"
fault_joint_states_key = "faulty_joint_states"
faulty_robot_states_key = "faulty_robot_state"
real_joint_states_key = "real_joint_states"
rosout_key = "rosout"
fault_effect_key = "fault_effect"

collision_list = [x for x in onlyfiles if x.startswith(collision_key)]
faults_list = [x for x in onlyfiles if x.startswith(faults_key)]
fault_flag_list = [x for x in onlyfiles if x.startswith(fault_flag_key)]
fault_state_list = [x for x in onlyfiles if x.startswith(fault_state_key)]
fault_joint_states_list = [x for x in onlyfiles if x.startswith(fault_joint_states_key)]
faulty_robot_states_list = [x for x in onlyfiles if x.startswith(faulty_robot_states_key)]
real_joint_states_list = [x for x in onlyfiles if x.startswith(real_joint_states_key)]
rosout_list = [x for x in onlyfiles if x.startswith(rosout_key)]
fault_effect_list = [x for x in onlyfiles if x.startswith(fault_effect_key)]
print(fault_effect_list)
    
'''
collision_dataframe = pd.DataFrame()

for i in range(0, len(collision_list)):

    with AnyReader([Path(folder+collision_list[i])]) as reader:
        collision_dataframe = collision_dataframe.append(get_dataframe(reader, '/collision_model', ['data']), ignore_index=False)
        

p = collision_dataframe.index.values
collision_dataframe.insert( 0, column="time_stamp",value = p)



collision_dataframe = collision_dataframe.reset_index()
collision_dataframe = collision_dataframe.drop('index', axis=1)
collision_dataframe.to_csv("/home/acefly/robot_fib/data_v2/check_collision/check_collision.csv")


'''


faults_dataframe = pd.DataFrame()

for i in range(0, len(faults_list)):

    with AnyReader([Path(folder+faults_list[i])]) as reader:
        faults_dataframe = faults_dataframe.append(get_dataframe(reader, '/fault_msg', ['fault', 'joint', 'pose', 'offset', 'time', 'time_label', 'drop_rate', 'mean', 'sd']), ignore_index=False)
        

p = faults_dataframe.index.values
faults_dataframe.insert( 0, column="time_stamp",value = p)



faults_dataframe = faults_dataframe.reset_index()
faults_dataframe = faults_dataframe.drop('index', axis=1)
faults_dataframe.to_csv(folder + "faults/faults.csv")



'''
fault_flag_dataframe = pd.DataFrame()

for i in range(0, len(fault_flag_list)):

    with AnyReader([Path(folder+fault_flag_list[i])]) as reader:
        fault_flag_dataframe = fault_flag_dataframe.append(get_dataframe(reader, '/fault_flag', ['data']), ignore_index=False)
        

p = fault_flag_dataframe.index.values
fault_flag_dataframe.insert( 0, column="time_stamp",value = p)



fault_flag_dataframe = fault_flag_dataframe.reset_index()
fault_flag_dataframe = fault_flag_dataframe.drop('index', axis=1)
fault_flag_dataframe.to_csv("/home/acefly/robot_fib/data_v3/fault_flag/fault_flag.csv")

'''

###

'''
print(faulty_robot_states_list)

robot_states_dataframe = pd.DataFrame()

for i in range(0, len(faulty_robot_states_list)):

    with AnyReader([Path(folder+faulty_robot_states_list[i])]) as reader:
        robot_states_dataframe = robot_states_dataframe.append(get_dataframe(reader, '/pose_state', ['data']), ignore_index=False)
        

p = robot_states_dataframe.index.values
robot_states_dataframe.insert( 0, column="time_stamp",value = p)



robot_states_dataframe = robot_states_dataframe.reset_index()
robot_states_dataframe = robot_states_dataframe.drop('index', axis=1)
robot_states_dataframe.to_csv("/home/acefly/robot_fib/data_v2/faulty_robot_state/faulty_robot_state.csv")



print(robot_states_dataframe)

'''

###


fault_effect_dataframe = pd.DataFrame()

for i in range(0, len(fault_effect_list)):
    
    with AnyReader([Path(folder+fault_effect_list[i])]) as reader:
        try:
            fault_effect_dataframe = fault_effect_dataframe.append(get_dataframe(reader, '/fault_effect', ['fault', 'joint', 'pose', 'offset', 'time', 'time_label', 'drop_rate', 'mean', 'sd', 'fault_effect']), ignore_index=False)
        except:
            print("error")
            continue

p = fault_effect_dataframe.index.values
fault_effect_dataframe.insert( 0, column="time_stamp",value = p)



fault_effect_dataframe = fault_effect_dataframe.reset_index()
fault_effect_dataframe = fault_effect_dataframe.drop('index', axis=1)
fault_effect_dataframe.to_csv("/home/acefly/robot_fib/data_v4/fault_effect/fault_effect.csv")
val = fault_effect_dataframe.columns[[1,2,3,4,5,6,7,8,9,10]]
print(val)
fault_effect_dataframe.drop_duplicates(subset=fault_effect_dataframe.columns[[1,2,3,4,5,6,7,8,9,10]], keep=False, inplace=True)

fault_effect_dataframe["fault_effect"] = fault_effect_dataframe["fault_effect"].replace(to_replace=4,value=3)
fault_effect_dataframe["fault_effect"] = fault_effect_dataframe["fault_effect"].replace(to_replace=5,value=4)
fault_effect_dataframe["fault_effect"] = fault_effect_dataframe["fault_effect"].replace(to_replace=6,value=5)
fault_effect_dataframe["fault_effect"] = fault_effect_dataframe["fault_effect"].replace(to_replace=7,value=6)

fault_effect_dataframe.to_csv(folder + "fault_effect/fault_effect_no_repetation.csv")
print(fault_effect_dataframe)








###
'''
fault_flag_dataframe[fault_flag_dataframe['data']]



filtered_df = fault_flag_dataframe[fault_flag_dataframe['data'] == True]
filtered_df.to_csv("/home/acefly/robot_fib/data_v2/plot_data/fault_flag.csv")
print(filtered_df)


fault_time_stamp = []

'''
