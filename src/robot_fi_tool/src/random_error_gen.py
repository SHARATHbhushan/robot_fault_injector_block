import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import numpy as np
from std_msgs.msg import Bool
from std_msgs.msg import Int32
from robot_fi_tool.msg import faultmsg
import random

class firos_rand:


    def __init__(self):
        #noise = np.random.normal(10,1,1)
        #print(noise)
        self.fault_list = [" ","noise", "stuck_at", "package_drop", "offset"]
        self.joint_list = [" ", "panda_joint1", "panda_joint2", "panda_joint3", "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7", "panda_finger_joint1", "panda_finger_joint2"]
        self.state_list = [" ", "hover_pose", "pick_pose_down", "pick_pose_down", "pick", "pick_pose_up", "hover_place_pose", "place_pose_down", "open_Hand", "place_pose_up", "init_pose"]
        self.goal_state_subscriber = rospy.Subscriber("goal_msg", Bool, self.goal_callback)
        self.goal_state_subscriber = rospy.Subscriber("iterations", Int32, self.iter_callback)
        self.random_fault_publisher = rospy.Publisher("fault_msg", faultmsg, queue_size=10)
        self.state_subscriber = rospy.Subscriber("pose_state", Int32,self.state_callback)

        self.min_mean = rospy.get_param("/min_mean")
        self.max_mean = rospy.get_param("/max_mean")
        self.min_drop_rate = rospy.get_param("/min_drop_rate")
        self.max_drop_rate = rospy.get_param("/max_drop_rate")
        self.min_sd = rospy.get_param("/min_sd")
        self.max_sd = rospy.get_param("/max_sd")
        self.min_offset = rospy.get_param("/min_offset")
        self.max_offset = rospy.get_param("/max_offset")
        self.max_time = rospy.get_param("/max_time")
        self.max_joints = rospy.get_param("/max_joints")
        self.max_faults = rospy.get_param("/max_faults")
        self.max_states = rospy.get_param("/max_states")
        self.max_time_labels = rospy.get_param("/max_time_labels")
        self.max_time = rospy.get_param("/max_time")
        self.max_time_offset = rospy.get_param("/max_time_offset")
        self.min_time_offset = rospy.get_param("/min_time_offset")
        

        self.desired_fault = rospy.get_param("/default_fault")
        self.desired_joint = rospy.get_param("/default_joint")
        self.desired_state = rospy.get_param("/default_state")
        self.desired_time = rospy.get_param("/default_time")
        self.desired_time_label = rospy.get_param("/default_time_label")
        self.desired_mean = rospy.get_param("/default_mean")
        self.desired_sd = rospy.get_param("/default_sd")
        self.desired_drop_rate = rospy.get_param("/default_drop_rate")
        self.desired_offset = rospy.get_param("/default_offset")
        self.desired_time_offset = rospy.get_param("/default_time_offset")

        self.goal = False
        self.desired_state = 0
        self.desired_joint = 0
        self.desired_fault = 0
        self.desired_time_label = 0
        self.desired_offset = 0
        self.desired_time = 0


        self.iter = 0
        self.state = 0
        self.iter_msg = False



    def state_callback(self,state):
        self.state = state.data
        

    def goal_callback(self,goal):   
        self.goal = goal.data
        #print(rand_msg.fault)
        #print(rand_msg.joint)
        #print(rand_msg.pose)
        
    def iter_callback(self,data):
        self.iter = data.data
        self.iter_msg = True
        self.rand_time = random.randint(1,5)
        self.real_time_exec = rospy.Time.now()
        self.real_time_val = rospy.Duration(self.rand_time) 
        rospy.sleep(self.real_time_val)
        print("injecting")
        self.timer_callback()

        
                
    def timer_callback(self):
        if self.iter_msg == True:
            rand_msg = faultmsg()
            self.desired_joint = random.randint(0, self.max_joints)
            self.desired_state = random.randint(1, self.max_states)
            self.desired_fault = random.randint(1, self.max_faults)
            self.desired_drop_rate = random.randint(self.min_drop_rate,self.max_drop_rate)
            self.desired_mean = round(random.uniform(self.min_mean,self.max_mean),2)
            self.desired_sd = round(random.uniform(self.min_sd,self.max_sd),2)
            self.desired_time_label = random.randint(2, self.max_time_labels) #disable for real and execution time fault injection
            #self.desired_time_label = 1
            self.desired_offset = random.randint(self.min_offset,self.max_offset)
            self.desired_time = random.randint(1, self.max_time)
            self.desired_time_offset = round(random.uniform(self.min_time_offset, self.max_time_offset),2)

            rand_msg.mean = round(self.desired_mean,2)
            rand_msg.sd = round(self.desired_sd,2)
            rand_msg.drop_rate = self.desired_drop_rate
            rand_msg.time = self.desired_time
            rand_msg.time_label = self.desired_time_label
            rand_msg.offset = self.desired_offset
            rand_msg.fault = self.desired_fault
            rand_msg.joint = self.desired_joint
            rand_msg.pose = self.desired_state
            rand_msg.time_offset = round(self.desired_time_offset,2)
            print(self.fault_list[self.desired_fault] + " Fault is being injected at state " + self.state_list[self.desired_state] + " in joint " + self.joint_list[self.desired_joint])
            print("fault : ", self.desired_fault)
            print("joint : ", self.desired_joint)
            print("state : ", self.desired_state)
            print("time : ", self.desired_time)
            print("time_label : ", self.desired_time_label)
            print("offset : ", self.desired_offset)
            print("drop_rate : ", self.desired_drop_rate)
            print("mean : ", self.desired_mean)
            print("sd : ", self.desired_sd)
            
            self.random_fault_publisher.publish(rand_msg)
        self.iter_msg = False
        
if __name__ == '__main__':
    rospy.init_node('random_fault_gen')
    firos_rand()
    rospy.spin()