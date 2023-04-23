from robot_fi_tool.msg import faultmsg
import robot_fi_module


fi = robot_fi_module()
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