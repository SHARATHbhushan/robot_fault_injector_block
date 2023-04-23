#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import numpy as np
from std_msgs.msg import Bool
from std_msgs.msg import Int32
from robot_fi_tool.msg import faultmsg
from subprocess import call
from subprocess import Popen  
import subprocess
from std_srvs.srv import Empty

'''
desired_state : 
  1-hover_pose
  2-pick_pose_down
  3-pick
  4-pick_pose_up
  5-hover_place_pose
  6-place_pose_down
  7-open_Hand
  8-place_pose_up
  9-init_pose
'''
'''
desire_joint 
  1 - panda_joint1
  2 - panda_joint2
  3 - panda_joint3
  4 - panda_joint4
  5 - panda_joint5
  6 - panda_joint6
  7 - panda_joint7
  8 - panda_finger_joint1
  9 - panda_finger_joint2
''' 
'''
desired_fault
  1 - noise
  2 - stuck_at
  3 - package_drop
  4 - offset
'''


class firos:


    def __init__(self):
        #noise = np.random.normal(10,1,1)
        #print(noise)
        
        #pause_physics_client=rospy.ServiceProxy('/gazebo/pause_physics',Empty)

        #ros init subscribers and publishers
        self.goal_state_subscriber = rospy.Subscriber("goal_flag", Bool, self.goal_flag_callback)
        self.goal_state_subscriber = rospy.Subscriber("goal_msg", Bool, self.goal_callback)
        self.joint_state_publisher = rospy.Publisher("joint_states", JointState, queue_size=10)
        self.fault_status = rospy.Publisher("fault_status", Bool, queue_size=10)
        self.joint_state_fake_subscriber = rospy.Subscriber("joint_states_fake", JointState, self.callback)
        self.state_subscriber = rospy.Subscriber("pose_state", Int32,self.state_callback)
        self.fault_msg_subscriber = rospy.Subscriber("fault_msg", faultmsg, self.fault_callback)
        self.publish_time = rospy.Publisher("time_to_inject", Int32, queue_size=10)
        self.real_time_fi = rospy.Subscriber("real_time_fi", Bool, self.real_time_fi_callback)
        self.faul_msg_status_pub = rospy.Publisher("fault_flag", Bool,  queue_size=10)
        self.fault_flag_pub = rospy.Publisher("goal_flag", Bool, queue_size=10)
        self.planning_subscription = rospy.Subscriber("planning", Bool, self.planning_callback)
        self.fault_msg_publisher = rospy.Publisher("fault_msg", faultmsg, queue_size=10)

        #setting up initial falgs
        self.goal = False
        self.fault_status.publish(False)
        self.package_drop_flag = False  
        self.package_drop_state = False
        self.real_time_fi_flag = False
        self.faul_msg_status_pub.publish(False)
        self.planning_flag = False


        #setting up initial values
        self.fault_val = 0
        self.state = 0
        self.desired_time = 0
        self.desired_time_label = 0
        self.desired_offset = 0
        self.proc = None
        self.joint_val_list = []
        self.fault_val_list = []
        

        #getting parameters from launch file
        self.desired_joint = 0
        self.desired_fault = rospy.get_param("/default_fault")
        self.desired_joint = rospy.get_param("/default_joint")
        self.desired_state = rospy.get_param("/default_state")
        self.desired_time = rospy.get_param("/default_time")
        self.desired_time_label = rospy.get_param("/default_time_label")
        self.desired_mean = rospy.get_param("/default_mean")
        self.desired_sd = rospy.get_param("/default_sd")
        self.desired_drop_rate = rospy.get_param("/default_drop_rate")
        self.desired_offset = rospy.get_param("/default_offset")

        #theses values are used for random fault injection
        self.min_mean = rospy.get_param("/min_mean")
        self.max_mean = rospy.get_param("/max_mean")
        self.min_drop_rate = rospy.get_param("/min_drop_rate")
        self.max_drop_rate = rospy.get_param("/max_drop_rate")
        self.min_sd = rospy.get_param("/min_sd")
        self.max_sd = rospy.get_param("/max_sd")
        self.min_offset = rospy.get_param("/min_offset")
        self.max_offset = rospy.get_param("/max_offset")
        self.max_time = rospy.get_param("max_time")



    def fault_callback(self,fault_msg):
        self.desired_state = fault_msg.pose
        self.desired_joint = fault_msg.joint
        self.desired_fault = fault_msg.fault
        self.desired_time = fault_msg.time
        self.desired_time_label = fault_msg.time_label
        self.desired_offset = fault_msg.offset
        self.desired_mean = round(fault_msg.mean,2)
        self.desired_sd = round(fault_msg.sd,2)
        self.desired_drop_rate = fault_msg.drop_rate
        self.fault_val_list = []
        self.desired_drop_rate = int(self.desired_drop_rate)
        #self.publish_time.publish(self.desired_time)
        self.fault_status.publish(True)

    def planning_callback(self,data):
        self.planning_flag = data.data

    def state_callback(self,state):
        self.state = state.data
        self.fault_val_list = []
        self.fault_status.publish(False)
        

    def goal_callback(self,goal):   
        self.goal = goal.data

    def callback(self,data):       
        self.joint_data = data      
        self.list_joint_data = list(self.joint_data.position)  
        #print(data.position[1])
        self.joint = self.desired_joint
        if self.desired_fault == 0:
            self.fault_val = 0
        if self.desired_fault == 1:
            self.fault_val = np.random.normal(self.desired_mean,self.desired_sd,1)[0]
        if self.desired_fault == 2:
            self.fault_val_list.append(self.list_joint_data[self.joint])
        if self.desired_fault == 4:
            self.fault_val = self.desired_offset

        if self.goal == True:
            if self.state == self.desired_state:
                if self.desired_time_label == 2:
                    #print(self.list_joint_data)
                    self.fault_status.publish(True)
                    self.faul_msg_status_pub.publish(True)
                    if self.desired_fault == 2:
                        self.list_joint_data[self.joint] = self.fault_val_list[0]
                    elif self.desired_fault == 3:
                        #print("working")
                        if self.package_drop_state == False:
                            self.package_drop_flag = True
                    else:
                        self.list_joint_data[self.joint] = self.list_joint_data[self.joint] + self.fault_val
                    self.joint_data.position = tuple(self.list_joint_data)
                #self.goal = False
                elif self.desired_time_label == 3 and self.planning_flag == False:
                        self.fault_status.publish(True)
                        self.faul_msg_status_pub.publish(True)
                        if self.desired_fault == 2:
                            self.list_joint_data[self.joint] = self.fault_val_list[0]
                        elif self.desired_fault == 3:
                            #print("working")
                            if self.package_drop_state == False:
                                self.package_drop_flag = True
                        else:
                            self.list_joint_data[self.joint] = self.list_joint_data[self.joint] + self.fault_val
                        self.joint_data.position = tuple(self.list_joint_data)
                    

        if self.real_time_fi_flag == True:
            if self.desired_fault == 3:
                if self.package_drop_state == False:
                    self.package_drop_flag = True
            
            else:
                #print(self.list_joint_data)
                self.fault_status.publish(True)
                self.faul_msg_status_pub.publish(True)
                if self.desired_fault == 2:
                    self.list_joint_data[self.joint] = self.fault_val_list[0]
                elif self.desired_fault == 3:
                    self.package_drop_flag = True
                else:
                    self.list_joint_data[self.joint] = self.list_joint_data[self.joint] + self.fault_val
                
                #print(self.list_joint_data[self.joint])
                
                #print("noise error injected")
                self.joint_data.position = tuple(self.list_joint_data)
                #self.joint_data.position[1] = error_data
                #self.joint_state_publisher.publish(self.joint_data)
                #self.joint_state_publisher.publish(data)
                #self.real_time_fi = False

        if self.package_drop_flag == True:
            pass
        else:
            self.joint_state_publisher.publish(self.joint_data)
        self.package_drop_flag == False
        self.fault_status.publish(False)
        self.faul_msg_status_pub.publish(False)

    def real_time_fi_callback(self,real_time_fi):
        if real_time_fi.data == True:
            self.real_time_fi_flag = True
        else:
            self.real_time_fi_flag = False





    def goal_flag_callback(self,goal_state):
        self.goal_state = goal_state.data
        #print(self.goal_state)
        if self.goal_state == True:
            if self.desired_fault == 3:
                self.fault_status.publish(True)
                print("works")
                cmd = ["rosrun", "topic_tools", "drop" ,"joint_states_fake", "1", str(self.desired_drop_rate), "joint_states"]
                self.proc = subprocess.Popen(cmd)
        else:
            self.fault_status.publish(False)
            if self.proc:
                if self.desired_fault == 3:
                    self.proc.kill()
                    self.package_drop_flag = False
                    self.package_drop_state = True
                    self.proc = None
        self.package_drop_state = False
        self.fault_status.publish(False)

    def publish_fault_msg(self,fault_msg):
        self.fault_msg = fault_msg
        self.fault_msg_publisher.publish(self.fault_msg)


if __name__ == '__main__':
    rospy.init_node('FIB')
    firos()
    rospy.spin()