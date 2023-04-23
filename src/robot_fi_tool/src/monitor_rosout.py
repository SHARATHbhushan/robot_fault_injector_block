import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import numpy as np
from std_msgs.msg import Bool
from robot_fi_tool.msg import faultmsg
import rosbag
from rosgraph_msgs.msg import Log

#subscribe to rosout and monitor simulation faults?



class exec_observer:
    def __init__(self):
        #self.collision_sub = rospy.Subscriber("collsion_model", String, self.collision_callback)
        #self.fault_sub = rospy.Subscriber("fault_status", Bool, self.fault_callback)
        #self.fault_msg_sub = rospy.Subscriber("fault_msg", faultmsg, self.fault_msg_callback)
        #subscribe to rosout and monitor simulation faults?
        self.rosout_sub = rospy.Subscriber("/rosout", Log, self.rosout_callback)
        self.rate = rospy.Rate(180)     
        self.fault_callback_sub = rospy.Subscriber("fault_msg", faultmsg, self.fault_callback)
        self.fault_pub = rospy.Publisher("/fault_effect", faultmsg, queue_size=10)
        self.fault = 0
        self.fault_joint = 0
        self.time = 0
        self.time_label = 0
        self.offset = 0
        self.drop_rate = 0
        self.mean = 0
        self.sd = 0
        self.fault_state = 0


    def fault_callback(self, data):
        self.fault = data.fault
        self.fault_joint = data.joint
        self.time = data.time
        self.time_label = data.time_label
        self.offset = data.offset
        self.drop_rate = data.drop_rate
        self.mean = data.mean
        self.sd = data.sd
        self.fault_state = data.pose



    def rosout_callback(self,data):
        #print(data)
        if data.name == "/own_pick_place_V4":
            #print(data.msg)
            if data.msg == "Failed to fetch current robot state":
                fault_msg = faultmsg()
                fault_msg.fault = self.fault
                fault_msg.joint = self.fault_joint
                fault_msg.time = self.time
                fault_msg.time_label = self.time_label
                fault_msg.offset = self.offset
                fault_msg.drop_rate = self.drop_rate
                fault_msg.mean = self.mean
                fault_msg.sd = self.sd
                fault_msg.pose = self.fault_state
                fault_msg.fault_effect = 7
                self.fault_pub.publish(fault_msg)
                


        


    

if __name__ == '__main__':
    rospy.init_node('exec_observer')
    exec_observer()
    rospy.spin()



