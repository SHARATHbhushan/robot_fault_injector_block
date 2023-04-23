#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String, Int32
from sensor_msgs.msg import JointState
import numpy as np
from std_msgs.msg import Bool
from robot_fi_tool.msg import faultmsg
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import GetModelState
class firos:


    def __init__(self):
        #noise = np.random.normal(10,1,1)
        #print(noise)
        self.person = []
        self.platform = []
        self.tangram_1_x = []
        self.tangram_2_x = []
        self.tangram_3_x = []
        self.tangram_4_x = []
        self.tangram_5_x = []
        self.tangram_6_x = []
        self.tangram_7_x = []
        self.tangram_1_y = []
        self.tangram_2_y = []
        self.tangram_3_y = []
        self.tangram_4_y = []
        self.tangram_5_y = []
        self.tangram_6_y = []
        self.tangram_7_y = []
        self.tangram_1_z = []
        self.tangram_2_z = []
        self.tangram_3_z = []
        self.tangram_4_z = []
        self.tangram_5_z = []
        self.tangram_6_z = []
        self.tangram_7_z = []
        self.flat_back = []
        self.flat_right = []
        self.flat_front = []
        self.i = 0
        self.goal_state_subscriber = rospy.Subscriber("/gazebo/model_states", ModelStates, self.collision_callback)
        self.collision_pub = rospy.Publisher("/collision_model", Int32, queue_size=10)
        self.reset_collision = rospy.Subscriber("/pose_state", Int32,self.state_callback)
        self.fault_callback_sub = rospy.Subscriber("/fault_msg", faultmsg, self.fault_callback)
        self.fault_pub = rospy.Publisher("/fault_effect", faultmsg, queue_size=10)
        
        self.person_state = False
        self.platform_state = False
        self.tangram_1_state = False
        self.tangram_2_state = False
        self.tangram_3_state = False
        self.tangram_4_state = False
        self.tangram_5_state = False
        self.tangram_6_state = False
        self.tangram_7_state = False
        self.flat_back_state = False
        self.flat_right_state = False
        self.flat_front_state = False
        self.fault = 0
        self.fault_joint = 0
        self.time = 0
        self.time_label = 0
        self.offset = 0
        self.drop_rate = 0
        self.mean = 0
        self.sd = 0
        self.fault_state = 0
        self.fault_effect = 0
        self.exponent = 1000

    def state_callback(self, data):

        self.person_state = False
        self.platform_state = False
        self.tangram_1_state = False
        self.tangram_2_state = False
        self.tangram_3_state = False
        self.tangram_4_state = False
        self.tangram_5_state = False
        self.tangram_6_state = False
        self.tangram_7_state = False
        self.flat_back_state = False
        self.flat_right_state = False
        self.flat_front_state = False

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


    def collision_callback(self,data): 
        object_1 = data.name[1]
        object_2 = data.name[2]
        object_3 = data.name[3]
        object_4 = data.name[4]
        object_5 = data.name[5]
        object_6 = data.name[6]
        object_7 = data.name[7]
        object_8 = data.name[8]
        object_9 = data.name[9]
        object_10 = data.name[10]
        object_11 = data.name[11]
        object_12 = data.name[12]
        object_13 = data.name[13]
        #object_12 = data.name[12]
        #print(object_13)
        
        self.person.append(data.pose[13].position)
        self.platform.append(data.pose[1].position)
        self.flat_back.append(data.pose[9].position)
        self.flat_right.append(data.pose[11].position)
        self.flat_front.append(data.pose[10].position)
        self.tangram_1_x.append(data.twist[2].linear.x)
        self.tangram_2_x.append(data.twist[3].linear.x)
        self.tangram_3_x.append(data.twist[4].linear.x)
        self.tangram_4_x.append(data.twist[5].linear.x)
        self.tangram_5_x.append(data.twist[6].linear.x)
        self.tangram_6_x.append(data.twist[7].linear.x)
        self.tangram_7_x.append(data.twist[8].linear.x)
        self.tangram_1_y.append(data.twist[2].linear.y)
        self.tangram_2_y.append(data.twist[3].linear.y)
        self.tangram_3_y.append(data.twist[4].linear.y)
        self.tangram_4_y.append(data.twist[5].linear.y)
        self.tangram_5_y.append(data.twist[6].linear.y)
        self.tangram_6_y.append(data.twist[7].linear.y)
        self.tangram_7_y.append(data.twist[8].linear.y)
        self.tangram_1_z.append(data.twist[2].linear.z)
        self.tangram_2_z.append(data.twist[3].linear.z)
        self.tangram_3_z.append(data.twist[4].linear.z)
        self.tangram_4_z.append(data.twist[5].linear.z)
        self.tangram_5_z.append(data.twist[6].linear.z)
        self.tangram_6_z.append(data.twist[7].linear.z)
        self.tangram_7_z.append(data.twist[8].linear.z)

        """  
        collision_x_2 = data.pose[2].position.x
        collision_x_3 = data.pose[3].position.x
        collision_x_4 = data.pose[4].position.x
        collision_x_5 = data.pose[5].position.x
        collision_x_6 = data.pose[6].position.x
        collision_x_7 = data.pose[7].position.x
        collision_x_8 = data.pose[8].position.x
        collision_X_9 = data.pose[9].position.x 
        """
        self.exponent = 1000
        #print(float(self.tangram_1_y[self.i])*self.exponent)
        if abs(float(self.tangram_1_x[self.i])*self.exponent) > 500 or abs(float(self.tangram_1_y[self.i])*self.exponent) > 500 or abs(float(self.tangram_1_z[self.i])*self.exponent) > 5000:
            if self.tangram_1_state == False:
                print("tangram_1_x fall detected")
                msg = Int32()
                msg.data = 1
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 1
                self.fault_pub.publish(fault_msg)
                self.tangram_1_state = True
        
        if abs(float(self.tangram_2_x[self.i])*self.exponent) > 500 or abs(float(self.tangram_2_y[self.i])*self.exponent) > 500 or abs(float(self.tangram_2_z[self.i])*self.exponent) > 500:
            if self.tangram_2_state == False:
                print("tangram_2_x fall detected")
                msg = Int32()
                msg.data = 1
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 1
                self.fault_pub.publish(fault_msg)
                self.tangram_2_state = True
        
        if abs(float(self.tangram_3_x[self.i])*self.exponent) > 500 or abs(float(self.tangram_3_y[self.i])*self.exponent) > 500 or abs(float(self.tangram_3_z[self.i])*self.exponent) > 500:
            if self.tangram_3_state == False:
                print("tangram_3_x fall detected")
                msg = Int32()
                msg.data = 1
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 1
                self.fault_pub.publish(fault_msg)
                self.tangram_3_state = True
        
        if abs(float(self.tangram_4_x[self.i])*self.exponent) > 500 or abs(float(self.tangram_4_y[self.i])*self.exponent) > 500 or abs(float(self.tangram_4_z[self.i])*self.exponent) > 500:
            if self.tangram_4_state == False:
                print("tangram_4_x fall detected")
                msg = Int32()
                msg.data = 1
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 1
                self.fault_pub.publish(fault_msg)
                self.tangram_4_state = True

        if abs(float(self.tangram_5_x[self.i])*self.exponent) > 500 or abs(float(self.tangram_5_y[self.i])*self.exponent) > 500 or abs(float(self.tangram_5_z[self.i])*self.exponent) > 500:
            if self.tangram_5_state == False:
                print("tangram_5_x fall detected")
                msg = Int32()
                msg.data = 1
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 1
                self.fault_pub.publish(fault_msg)
                self.tangram_5_state = True

        if abs(float(self.tangram_6_x[self.i])*self.exponent) > 500 or abs(float(self.tangram_6_y[self.i])*self.exponent) > 500 or abs(float(self.tangram_6_z[self.i])*self.exponent) > 500:
            if self.tangram_6_state == False:
                print("tangram_6_x fall detected")
                msg = Int32()
                msg.data = 1
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 1
                self.fault_pub.publish(fault_msg)
                self.tangram_6_state = True
        
        if abs(float(self.tangram_7_x[self.i])*self.exponent) > 500 or abs(float(self.tangram_7_y[self.i])*self.exponent) > 500 or abs(float(self.tangram_7_z[self.i])*self.exponent) > 500:
            if self.tangram_7_state == False:
                print("tangram_7_x fall detected")
                msg = Int32()
                msg.data = 1
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 1
                self.fault_pub.publish(fault_msg)
                self.tangram_7_state = True
        
        #delta_x = self.person[self.i].x - self.person[self.i - 1].x
        #delta_y = self.person[self.i].y - self.person[self.i - 1].y
        #print("delta: ",delta_x,delta_y)
        
        if self.person[self.i] != self.person[self.i - 1]:
            if self.person_state == False:
                print("human collision detected")
                msg = Int32()
                msg.data = 2
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 2
                self.fault_pub.publish(fault_msg)
                self.person_state = True
        
        if self.platform[self.i] != self.platform[self.i - 1]:
            if self.platform_state == False:
                print("platform collision detected")
                msg = Int32()
                msg.data = 3
                self.collision_pub.publish(msg)
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
                #fault_msg.fault_effect = 3
                self.fault_pub.publish(fault_msg)
                self.platform_state = True

 
        if self.flat_back[self.i] != self.flat_back[self.i - 1]:
            if self.flat_back_state == False:
                print("flat_back collision detected")
                msg = Int32()
                msg.data = 4
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 3
                self.fault_pub.publish(fault_msg)
                self.flat_back_state = True

        if self.flat_right[self.i] != self.flat_right[self.i - 1]:
            if self.flat_right_state == False:
                print("flat_right collision detected")
                msg = Int32()
                msg.data = 5
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 4
                self.fault_pub.publish(fault_msg)
                self.flat_right_state = True

        if self.flat_front[self.i] != self.flat_front[self.i - 1]:
            if self.flat_front_state == False:
                print("flat_front collision detected")
                msg = Int32()
                msg.data = 6
                self.collision_pub.publish(msg)
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
                fault_msg.fault_effect = 5
                self.fault_pub.publish(fault_msg)
                self.flat_front_state = True



        self.i = self.i + 1
        



if __name__ == '__main__':
    rospy.init_node('gazebo_collision')
    firos()
    rospy.spin()





