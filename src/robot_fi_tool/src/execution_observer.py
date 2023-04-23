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
        self.planning_pub = rospy.Publisher("/execution", Bool, queue_size=10)
        self.flag = False
        self.publisher()



    def rosout_callback(self,data):
        #print(data)
        key = "SimpleSetup: Path simplification took"
        
        if data.name == "/move_group":
            #print(data.msg)
            if key in data.msg or data.msg == "Execution request received":
                self.flag = True
                #print("execution started")
            if data.msg == "Execution completed: SUCCEEDED" or data.msg == "Completed trajectory execution with status SUCCEEDED ...":
                #print("execution finished")
                self.flag = False
            #Completed trajectory execution with status SUCCEEDED ...
    def publisher(self):
        while not rospy.is_shutdown():
            self.planning_pub.publish(self.flag)
            rospy.sleep(0.0000001)

    

if __name__ == '__main__':
    rospy.init_node('exec_observer')
    exec_observer()
    rospy.spin()



