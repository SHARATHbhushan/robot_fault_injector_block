# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Test_window(object):
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
        self.pushButton.setGeometry(QtCore.QRect(130, 520, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 260, 281, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 320, 91, 21))
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 620, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(140, 320, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 340, 16, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 340, 16, 21))
        self.label_6.setObjectName("label_6")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(180, 400, 118, 26))
        self.timeEdit.setObjectName("timeEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 400, 141, 21))
        self.label_7.setObjectName("label_7")
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 70, 401, 251))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(350, 360, 401, 271))
        self.widget_2.setObjectName("widget_2")
        Test_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Test_window)
        self.statusbar.setObjectName("statusbar")
        Test_window.setStatusBar(self.statusbar)

        self.retranslateUi(Test_window)
        QtCore.QMetaObject.connectSlotsByName(Test_window)

    def retranslateUi(self, Test_window):
        _translate = QtCore.QCoreApplication.translate
        Test_window.setWindowTitle(_translate("Test_window", "MainWindow"))
        self.label.setText(_translate("Test_window", "Topic"))
        self.label_2.setText(_translate("Test_window", "Fault type"))
        self.label_3.setText(_translate("Test_window", "Robot State"))
        self.pushButton.setText(_translate("Test_window", "Inject Fault"))
        self.label_4.setText(_translate("Test_window", "Offset Value"))
        self.label_5.setText(_translate("Test_window", "1"))
        self.label_6.setText(_translate("Test_window", "10"))
        self.label_7.setText(_translate("Test_window", "Time to inject fault"))
        self.label_8.setText(_translate("Test_window", "Value"))
        self.label_9.setText(_translate("Test_window", "Real Sensor Data"))
        self.label_10.setText(_translate("Test_window", "Fault Injected Sensor Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Test_window = QtWidgets.QMainWindow()
    ui = Ui_Test_window()
    ui.setupUi(Test_window)
    Test_window.show()
    sys.exit(app.exec_())
