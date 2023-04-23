#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
from sensor_msgs.msg import JointState
from robot_fi_tool.msg import faultmsg
class goal_listener:
    def __init__(self):
        rospy.Subscriber("goal_state", Bool, self.callback)
        #rospy.Subscriber("joint_states", JointState, self.publisher)
        self.pub = rospy.Publisher('goal_msg', Bool, queue_size=10)
        self.pub2 = rospy.Publisher('goal_flag', Bool, queue_size=10)
        rospy.Subscriber("fault_msg", faultmsg, self.fault_callback)
        self.pub3 = rospy.Publisher('real_time_fi', Bool,queue_size=10)
        self.rate = rospy.Rate(30) # 10hz
        self.flag = False
        self.desired_time_label = -1
        self.desired_time = 0
        self.real_time_exec = 0
        self.real_time_val_s = 0
        self.real_endTime = 0
        self.plan_time_exec = 0
        self.plan_time_val = 0
        self.plan_endTime = 0
        self.exec_time_exec = 0
        self.exec_time_val = 0
        self.exec_endTime = 0
        self.desired_time_offset = 0.5
        

    def fault_callback(self,data):
        self.desired_time_label = data.time_label
        self.desired_time = data.time
        self.desired_time_offset = round(data.time_offset,2)
        print(self.desired_time_offset)
        self.real_time_exec = rospy.Time.now()
        self.real_time_val = rospy.Duration(self.desired_time) 
        self.real_endTime = self.real_time_exec + self.real_time_val
        self.goal_msg = Bool()
        self.goal_state = Bool()
        if self.desired_time_label == 1:
                    #print("state 0")
                    print("real_time_injection")
                    self.goal_state = True
                    self.pub2.publish(self.goal_state)
                    #print("start: ", self.real_time_exec, "sec : ", self.real_time_val, "end: ", self.real_endTime)
                    while rospy.Time.now() < self.real_endTime:
                        self.goal_msg.data = True
                        #print("state 1")
                        self.pub3.publish(self.goal_msg)
                        rospy.sleep(0.1)
                    self.goal_state = False
                    self.pub2.publish(self.goal_state)
                    self.goal_msg.data = False
                    self.pub3.publish(self.goal_msg)

        
    def callback(self,data):
        #print(data.data)
        if data.data == False:
            self.flag = False
        if data.data == True:
            self.flag = True
        self.real_time_exec_s = rospy.Time.now()
        self.real_time_val_s = rospy.Duration(self.desired_time) 
        self.real_endTime = self.real_time_exec_s + self.real_time_val_s
        self.plan_time_exec_s = rospy.Time.now()
        self.plan_time_val_s = rospy.Duration(5 - self.desired_time)
        self.plan_endTime = self.plan_time_exec_s + self.plan_time_val_s

        #self.publisher(data.data,self.flag)
        

        #def publisher(self,data):
        self.goal_msg = Bool()
        self.goal_msg_val = Bool()
        if data:    
            if self.flag == True:
                #print(True)

                #self.flag = False

                if self.desired_time_label == 2:
                    #print("state 2")
                    #print("start: ", self.plan_time_exec, "sec : ", self.plan_time_val, "end: ", self.plan_endTime)
                    while rospy.Time.now() < self.plan_endTime:
                        #print("state 2.1")
                        self.goal_msg.data = False
                        self.pub.publish(self.goal_msg)
                        rospy.sleep(0.1)
                    time_offset = rospy.Time.now()
                    planning_offset = rospy.Duration(self.desired_time_offset)
                    self.goal_msg_val = True
                    self.pub2.publish(self.goal_msg_val)
                    while rospy.Time.now() < self.real_time_val_s+time_offset+planning_offset:
                        #print("state 2.2")
                        self.goal_msg.data = True
                        self.pub.publish(self.goal_msg)
                        rospy.sleep(0.1)
                    self.goal_msg_val = False
                    self.pub2.publish(self.goal_msg_val)
                self.goal_msg.data = False
                self.pub.publish(self.goal_msg)
                self.flag = False

                if self.desired_time_label == 3:
                    #print("state 3")
                    self.exec_time_exec = rospy.Time.now()
                    self.exec_time_val = rospy.Duration(5)
                    self.exec_endTime = self.exec_time_exec + self.exec_time_val
                    while rospy.Time.now() < self.exec_endTime:
                        #print("state 3.1")
                        self.goal_msg.data = False
                        self.pub.publish(self.goal_msg)
                        rospy.sleep(0.1)
                    time_offset = rospy.Time.now()
                    self.goal_msg_val = True
                    self.pub2.publish(self.goal_msg_val)
                    while rospy.Time.now() < self.real_time_val_s+time_offset:
                        #print("state 3.2")
                        self.goal_msg.data = True
                        self.pub.publish(self.goal_msg)
                        rospy.sleep(0.1)
                    self.goal_msg_val = False
                    self.pub2.publish(self.goal_msg_val)
                self.goal_msg.data = False
                self.pub.publish(self.goal_msg)
                self.flag = False
                
            else:
                self.goal_msg.data = False
                self.pub.publish(self.goal_msg)
                #self.rate.sleep()
                #if self.flag == True:
                #    break


if __name__ == '__main__':
    rospy.init_node('listener')
    goal_listener()
    rospy.spin()