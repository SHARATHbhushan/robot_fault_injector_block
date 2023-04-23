#! /usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import numpy as np
from std_msgs.msg import Bool
from std_msgs.msg import Int32
from robot_fi_tool.msg import faultmsg
import random
from std_srvs.srv import Empty


class reset_world_init:
    def __init__(self):
        self.wait = rospy.wait_for_service('/gazebo/reset_world')
        self.reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)
        self.wait2 = rospy.wait_for_service('/gazebo/reset_simulation')
        self.reset_simulation = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
        self.reset_world_sub = rospy.Subscriber("reset_world", Bool, self.reset_callback)

    
    def reset_callback(self, data):  
        print("works")
        rospy.sleep(5)
        self.reset_world()
        #self.reset_simulation()


if __name__ == '__main__':
    rospy.init_node('reset_world_init')
    reset_world_init()
    rospy.spin()
        


