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

folder = "/home/acefly/robot_fib/data_v3/"




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




faults_dataframe = pd.DataFrame()

for i in range(0, 1):

    with AnyReader([Path(folder+fault_joint_states_list[i])]) as reader:
        faults_dataframe = faults_dataframe.append(get_dataframe(reader, '/sensor_msg', ['fault', 'joint', 'pose', 'offset', 'time', 'time_label', 'drop_rate', 'mean', 'sd']), ignore_index=False)
        

p = faults_dataframe.index.values
faults_dataframe.insert( 0, column="time_stamp",value = p)



faults_dataframe = faults_dataframe.reset_index()
faults_dataframe = faults_dataframe.drop('index', axis=1)
print(faults_dataframe)



#faults_dataframe.to_csv("/home/acefly/robot_fib/data_v3/faults/faults.csv")



