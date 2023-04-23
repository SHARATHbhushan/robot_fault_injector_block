# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from qwt import QwtPlot
import rospy
from robot_fi_tool.msg import faultmsg
import time
import sys
import os
from sensor_msgs.msg import JointState
from PyQt5.QtGui import QPixmap
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from random import randint
from std_msgs.msg import Bool
class Ui_Test_window(object):

    def __init__(self):
        self.fault_list = [" ","noise", "stuck_at", "package_drop", "offset"]
        self.joint_list = [" ", "panda_joint1", "panda_joint2", "panda_joint3", "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7", "panda_finger_joint1", "panda_finger_joint2"]
        self.state_list = [" ", "hover_pose", "pick_pose_down", "pick", "pick_pose_up", "hover_place_pose", "place_pose_down", "open_Hand", "place_pose_up", "init_pose"]
        self.time_label_list = [" ", "Real_time", "planning_time", "Execution_time"]
        self.fault_publisher = rospy.Publisher("fault_msg", faultmsg, queue_size=10)
        self.joint_state_fake_subscriber = rospy.Subscriber("joint_states_fake", JointState, self.callback)
        self.joint_state_fake_subscriber = rospy.Subscriber("joint_states", JointState, self.joint_callback)
        self.pose_callback_s = rospy.Subscriber("pose_state", Bool, self.pose_callback)
        #self.fault_sub = rospy.Subscriber("joint_states", Bool, self.fault_callback)
        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]
        self.x2 = list(range(100))  # 100 time points
        self.y2 = [randint(0,100) for _ in range(100)]
        self.i = 1
        self.offset = 0
        self.time_label_val = 0
        self.time_val = 0
        self.state_val = 0
        self.joint_val = 0
        self.fault_val = 0
        self.mean_val = 0
        self.sd_val = 0
        self.drop_rate_val = 0   
        self.state_val = 0 
        
    def pose_callback(self, msg):
        self.state_val = msg.data
        

    def setupUi(self, Test_window):
        Test_window.setObjectName("Test_window")
        Test_window.resize(1040, 682)
        self.centralwidget = QtWidgets.QWidget(Test_window)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 80, 281, 21))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 67, 17))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 170, 281, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 620, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.publish_fault)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 260, 281, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 400, 281, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 320, 91, 21))
        self.label_4.setObjectName("label_4")
        #self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        #self.progressBar.setGeometry(QtCore.QRect(120, 620, 118, 23))
        #self.progressBar.setProperty("value", 0)
        #self.progressBar.setObjectName("progressBar")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(140, 320, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setValue(5)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)
		
        #layout.addWidget(self.sl)
        self.horizontalSlider.valueChanged.connect(self.valuechange)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 340, 16, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 340, 16, 21))
        self.label_6.setObjectName("label_6")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(180, 450, 48, 26))
        self.spinBox.setObjectName("spinBox") 
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 450, 158, 21))
        self.label_7.setObjectName("label_7")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 70, 401, 251))
        self.widget.setObjectName("widget")

        self.plot = pg.plot()
        self.plot.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.plot.plot(self.x, self.y, pen=pen)
        layout = QGridLayout()
        self.widget.setLayout(layout)
        layout.addWidget(self.plot, 0, 1, 3, 1)

        
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(350, 360, 401, 271))
        self.widget_2.setObjectName("widget_2")

        self.plot_2 = pg.plot()
        self.plot_2.setBackground('w')
        pen_2 = pg.mkPen(color=(255, 0, 0))
        self.data_line_2 =  self.plot_2.plot(self.x2, self.y2, pen=pen_2)
        layout_2 = QGridLayout()
        self.widget_2.setLayout(layout_2)
        layout_2.addWidget(self.plot_2, 0, 1, 3, 1)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(60)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(780, 40, 231, 591))
        self.graphicsView.setObjectName("graphicsView")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 340, 41, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(510, 50, 121, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(500, 340, 181, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 370, 81, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 490, 67, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 530, 67, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 560, 81, 17))
        self.label_14.setObjectName("label_14")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 490, 69, 26))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(110, 520, 69, 26))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 560, 48, 26))
        self.spinBox_2.setObjectName("spinBox_2")
        Test_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Test_window)
        self.statusbar.setObjectName("statusbar")
        Test_window.setStatusBar(self.statusbar)


        



        self.retranslateUi(Test_window)
        QtCore.QMetaObject.connectSlotsByName(Test_window)

    def retranslateUi(self, Test_window):
        _translate = QtCore.QCoreApplication.translate
        Test_window.setWindowTitle(_translate("Test_window", "Robot_Fault_Injection_Module"))
        self.label.setText(_translate("Test_window", "Fault type"))
        self.label_2.setText(_translate("Test_window", "Joint"))
        self.label_3.setText(_translate("Test_window", "Robot State"))
        self.pushButton.setText(_translate("Test_window", "Inject Fault"))
        self.label_4.setText(_translate("Test_window", "Offset Value"))
        self.label_5.setText(_translate("Test_window", "1"))
        self.label_6.setText(_translate("Test_window", "10"))
        self.label_7.setText(_translate("Test_window", "Time to inject fault in s"))
        self.label_8.setText(_translate("Test_window", "Value"))
        self.label_9.setText(_translate("Test_window", "Real Sensor Data"))
        self.label_10.setText(_translate("Test_window", "Fault Injected Sensor Data"))
        self.label_11.setText(_translate("Test_window", "Time Label"))
        self.comboBox.addItems(self.fault_list)
        self.comboBox.activated[str].connect(self.select_noise)
        self.comboBox_2.addItems(self.joint_list)
        self.comboBox_2.activated[str].connect(self.select_joint)
        self.comboBox_3.addItems(self.state_list)
        self.comboBox_3.activated[str].connect(self.select_state)
        self.comboBox_4.addItems(self.time_label_list)
        self.comboBox_4.activated[str].connect(self.select_time_label)  
        self.spinBox.valueChanged.connect(self.set_time)
        self.spinBox_2.valueChanged.connect(self.set_drop_rate)
        self.doubleSpinBox.valueChanged.connect(self.set_mean)
        self.doubleSpinBox_2.valueChanged.connect(self.set_sd)
        self.label_12.setText(_translate("Test_window", "Mean"))
        self.label_13.setText(_translate("Test_window", "SD"))
        self.label_14.setText(_translate("Test_window", "Drop Rate"))
        image_path = "/home/acefly/Pictures/panda_2.jpg"
        if os.path.isfile(image_path):
                scene = QtWidgets.QGraphicsScene()
                pixmap = QPixmap(image_path)
                item = QtWidgets.QGraphicsPixmapItem(pixmap)
                scene.addItem(item)
                self.graphicsView.setScene(scene)

    

    def valuechange(self):
        self.offset = self.horizontalSlider.value()
        #print(self.offset)

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

    def select_time_label(self, time_label_text):
        self.time_label_val = self.time_label_list.index(time_label_text)
        print("time_label: ", self.time_label_val)
        if self.time_label_val == 1:
            self.comboBox_3.setCurrentIndex(self.state_val)

    def set_time(self):
        self.time_val = self.spinBox.value()
        print("time: ", self.time_val)

    def set_drop_rate(self):
        self.drop_rate_val = self.spinBox_2.value()
        print("drop rate: ", self.drop_rate_val)

    def set_mean(self):
        self.mean_val = self.doubleSpinBox.value()
        print("mean : ", self.mean_val)

    def set_sd(self):
        self.sd_val = self.doubleSpinBox_2.value()
        print("sd : ", self.sd_val)


    def publish_fault(self):
        print("clicked")
        msg = faultmsg() 
        msg.fault = int(self.fault_val)
        msg.joint = int(self.joint_val-1)
        msg.pose = int(self.state_val)
        msg.offset = int(self.offset)
        msg.time = int(self.time_val)
        msg.time_label = int(self.time_label_val)
        msg.mean = float(self.mean_val)
        msg.sd = float(self.sd_val)
        msg.drop_rate = int(self.drop_rate_val)
        self.fault_publisher.publish(msg)
        

    def callback(self, data):
        self.joint_data = data
        self.list_joint_data = list(self.joint_data.position)
        self.x = self.x[1:] 
        t = rospy.Time.from_sec(time.time())
        seconds = round(t.to_sec(),2) 
        self.x.append(seconds)  
        self.y = self.y[1:]  
        self.y.append(self.list_joint_data[int(self.joint_val)-1]) 
         

    def joint_callback(self, data):
        self.joint_data_2 = data
        self.list_joint_data_2 = list(self.joint_data_2.position)
        self.x2 = self.x2[1:] 
        t2 = rospy.Time.from_sec(time.time())
        seconds_2 = round(t2.to_sec(),2) 
        self.x2.append(seconds_2)  
        self.y2 = self.y2[1:]  
        self.y2.append(self.list_joint_data_2[int(self.joint_val)-1]) 
         

    def update_plot_data(self):

        #self.x = self.x[1:]  # Remove the first y element.
        #self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        #self.y = self.y[1:]  # Remove the first
        #self.y.append( randint(0,100))  # Add a new random value.
        self.data_line.setData(self.x, self.y)
        self.data_line_2.setData(self.x2, self.y2)

    


if __name__ == "__main__":
    rospy.init_node('FIB_GUI_v2')
    app = QtWidgets.QApplication(sys.argv)
    Test_window = QtWidgets.QMainWindow()
    ui = Ui_Test_window()
    ui.setupUi(Test_window)

    Test_window.show()
    sys.exit(app.exec_())
    rospy.spin()

