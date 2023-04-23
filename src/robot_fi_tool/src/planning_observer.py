import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import numpy as np
from std_msgs.msg import Bool
from robot_fi_tool.msg import faultmsg
import rosbag
from rosgraph_msgs.msg import Log
from moveit_msgs.msg import MoveGroupActionFeedback
#subscribe to rosout and monitor simulation faults?



class plan_observer:
    def __init__(self):
        #self.collision_sub = rospy.Subscriber("collsion_model", String, self.collision_callback)
        #self.fault_sub = rospy.Subscriber("fault_status", Bool, self.fault_callback)
        #self.fault_msg_sub = rospy.Subscriber("fault_msg", faultmsg, self.fault_msg_callback)
        #subscribe to rosout and monitor simulation faults?
        self.move_group_sub = rospy.Subscriber("/move_group/feedback", MoveGroupActionFeedback, self.move_group)
        self.rate = rospy.Rate(180)     
        self.planning_pub = rospy.Publisher("/planning", Bool, queue_size=10)
        self.flag = False
        self.status_list = []
        self.publisher()


    def move_group(self,data):
        #print(data.feedback.state)
        self.status = data.status.status
        self.feedback = str(data.feedback.state)
        #print(self.status)
        if self.status == 1:
            if self.feedback == "PLANNING":
                self.flag = True
        if self.status == 3:
            #print(data.msg)
            #print("planning finished")
            self.flag = False
            #panda_arm/panda_arm[RRTConnect]: Starting planning with 1 states already in datastructure

    def publisher(self):
        while not rospy.is_shutdown():
            self.planning_pub.publish(self.flag)
            rospy.sleep(0.01)

if __name__ == '__main__':
    rospy.init_node('plan_observer')
    plan_observer()
    rospy.spin()



