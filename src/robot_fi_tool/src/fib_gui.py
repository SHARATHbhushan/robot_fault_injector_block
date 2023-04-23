from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from robot_fi_tool.msg import faultmsg
import time
import sys



class Ui_Test_window(object):
    def __init__(self):
        self.fault_list = [" ","noise", "stuck_at", "package_drop", "offset"]
        self.joint_list = [" ", "panda_joint1", "panda_joint2", "panda_joint3", "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7", "panda_finger_joint1", "panda_finger_joint2"]
        self.state_list = [" ", "hover_pose", "pick_pose_down", "pick_pose_down", "pick", "pick_pose_up", "hover_place_pose", "place_pose_down", "open_Hand", "place_pose_up", "init_pose"]
        self.fault_publisher = rospy.Publisher("fault_msg", faultmsg, queue_size=10)


    def setupUi(self, Test_window):
        Test_window.setObjectName("Test_window")
        Test_window.resize(352, 441)
        self.centralwidget = QtWidgets.QWidget(Test_window)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 80, 281, 21))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 78, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 67, 17))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 170, 281, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 280, 281, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 380, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.publish_fault)
        Test_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Test_window)
        self.statusbar.setObjectName("statusbar")
        Test_window.setStatusBar(self.statusbar)

        self.retranslateUi(Test_window)
        QtCore.QMetaObject.connectSlotsByName(Test_window)

    def retranslateUi(self, Test_window):
        _translate = QtCore.QCoreApplication.translate
        Test_window.setWindowTitle(_translate("Test_window", "Fault Injector module for panda robot"))
        self.label.setText(_translate("Test_window", "Noise Type"))
        self.label_2.setText(_translate("Test_window", "Joint"))
        self.label_3.setText(_translate("Test_window", "Robot State"))
        self.pushButton.setText(_translate("Test_window", "Inject Fault"))
        self.comboBox.addItems(self.fault_list)
        self.comboBox.activated[str].connect(self.select_noise)
        self.comboBox_2.addItems(self.joint_list)
        self.comboBox_2.activated[str].connect(self.select_joint)
        self.comboBox_3.addItems(self.state_list)
        self.comboBox_3.activated[str].connect(self.select_state)

    def select_noise(self, text):
        #print("hello you selected : ", text)
        self.fault_val = self.fault_list.index(text)
        print("noise: ", self.fault_val)

    def select_joint(self, joint_text):
        self.joint_val = self.joint_list.index(joint_text)
        print("joint: ", self.joint_val)

    def select_state(self, state_text):
        self.state_val = self.state_list.index(state_text)
        print("state: ", self.state_val)

    def publish_fault(self):
        print("clicked")
        msg = faultmsg() 
        msg.fault = self.fault_val
        msg.joint = int(self.joint_val)-1
        msg.pose = self.state_val
        self.fault_publisher.publish(msg)




if __name__ == "__main__":

    rospy.init_node('FIB_GUI')
    
    app = QtWidgets.QApplication(sys.argv)
    Test_window = QtWidgets.QMainWindow()
    ui = Ui_Test_window()
    ui.setupUi(Test_window)
    
    Test_window.show()
    sys.exit(app.exec_())
    rospy.spin()
