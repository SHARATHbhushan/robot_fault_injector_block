from robot_fi_tool.msg import faultmsg
import rospy


class fi_module:
    def __init__(self):
        self.pub = rospy.Publisher('fault_msg', faultmsg, queue_size=10)
        
    def publish_fault_msg(self, fault_msg):
        self.pub.publish(fault_msg)


if __name__ == '__main__':
    rospy.init_node('fi_module')
    
    fi = fi_module()
    fault_msg = faultmsg()

    fault_msg.time_label = 1
    fault_msg.time = 5
    fault_msg.time_offset = 0.5
    fault_msg.drop_rate = 2
    fault_msg.mean = 0.5
    fault_msg.sd = 0.5
    fault_msg.offset = 0.5
    fault_msg.fault = 1
    fault_msg.joint = 1
    fault_msg.pose = 1

    fi.publish_fault_msg(fault_msg)
    rospy.spin()
