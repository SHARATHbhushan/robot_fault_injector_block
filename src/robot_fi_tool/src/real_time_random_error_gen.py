import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import numpy as np
from std_msgs.msg import Bool
from std_msgs.msg import Int32
from robot_fi_tool.msg import faultmsg
import random

from datetime import timedelta  

class firos_rand:


    def __init__(self):
        #noise = np.random.normal(10,1,1)
        #print(noise)
        self.fault_list = [" ","noise", "stuck_at", "package_drop", "offset"]
        self.joint_list = [" ", "panda_joint1", "panda_joint2", "panda_joint3", "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7", "panda_finger_joint1", "panda_finger_joint2"]
        self.state_list = [" ", "hover_pose", "pick_pose_down", "pick_pose_down", "pick", "pick_pose_up", "hover_place_pose", "place_pose_down", "open_Hand", "place_pose_up", "init_pose"]

        self.random_fault_publisher = rospy.Publisher("fault_msg", faultmsg, queue_size=10)
        self.reset_world = rospy.Publisher("reset_world", Bool, queue_size=10)
        self.pose_state = rospy.Subscriber("pose_state", Int32, self.pose_state_callback)
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

        self.desired_fault = rospy.get_param("/default_fault")
        self.desired_joint = rospy.get_param("/default_joint")
        self.desired_state = rospy.get_param("/default_state")
        self.desired_time = rospy.get_param("/default_time")
        self.desired_time_label = rospy.get_param("/default_time_label")
        self.desired_mean = rospy.get_param("/default_mean")
        self.desired_sd = rospy.get_param("/default_sd")
        self.desired_drop_rate = rospy.get_param("/default_drop_rate")
        self.desired_offset = rospy.get_param("/default_offset")

        self.goal = False
        # self.desired_state = 0
        # self.desired_joint = 0
        # self.desired_fault = 0
        # self.desired_time_label = 0
        # self.desired_offset = 0
        # self.desired_time = 0

        self.timer_flag = 0
        self.iter = 0
        self.state = 0
        self.iter_msg = False
        self.rand_time_list = []     
        self.start_timer()
        self.pose_state = 0

    def pose_state_callback(self, msg):
        self.pose_state = msg.data
        
    def start_timer(self):
        rng = np.random.default_rng()
        self.rand_time = rng.choice(range(590), size=7, replace=False)
        self.rand_time.tolist()
        self.rand_time = np.append(self.rand_time,600)
        self.rand_time.sort()
        self.start_time = rospy.Time.now()
        self.iter_callback()




    def iter_callback(self):
        self.iter_msg = True
        # sim time : 9.5 mins
        print(self.rand_time)
        print(self.start_time)
        self.rand_time_val = self.rand_time[self.timer_flag]
        self.real_time_exec = rospy.Time.now()
        self.real_time_val = self.start_time + rospy.Duration(self.rand_time_val)
        print("actual_time: ", self.real_time_exec)
        print("desired_time: ", self.real_time_val)
        while rospy.Time.now() < self.real_time_val:
            #print("sleeping")   
            rospy.sleep(1)

        print("injecting")
        self.timer_flag = self.timer_flag + 1
        self.timer_callback()
           

        
                
    def timer_callback(self):
        if self.iter_msg == True:
            rand_msg = faultmsg()
            self.desired_joint = random.randint(0, self.max_joints)
            self.desired_state = random.randint(1, self.max_states)
            self.desired_fault = random.randint(1, self.max_faults)
            self.desired_drop_rate = random.randint(self.min_drop_rate,self.max_drop_rate)
            self.desired_mean = random.randint(self.min_mean,self.max_mean)
            self.desired_sd = random.randint(self.min_sd,self.max_sd)
            #self.desired_time_label = random.randint(2, self.max_time_labels) #disable for real and execution time fault injection
            self.desired_time_label = 1
            self.desired_offset = random.randint(self.min_offset,self.max_offset)
            self.desired_time = random.randint(1, self.max_time)

            rand_msg.mean = self.desired_mean
            rand_msg.sd = self.desired_sd
            rand_msg.drop_rate = self.desired_drop_rate
            rand_msg.time = self.desired_time
            rand_msg.time_label = self.desired_time_label
            rand_msg.offset = self.desired_offset
            rand_msg.fault = self.desired_fault
            rand_msg.joint = self.desired_joint
            rand_msg.pose = self.pose_state
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
        rospy.sleep(5)
        print(self.timer_flag)
        if self.timer_flag <= 6:
            self.iter_callback()
        if self.timer_flag == 7:
            self.reset_flag = Bool()
            self.reset_flag.data = True
            self.reset_world.publish(self.reset_flag)
            self.timer_flag = 0
            self.start_timer()



            
        
if __name__ == '__main__':
    rospy.init_node('real_time_random_fault_gen')
    firos_rand()
    rospy.spin()