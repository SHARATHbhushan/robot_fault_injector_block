from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Test_window(object):
    def setupUi(self, Test_window):
        Test_window.setObjectName("Test_window")
        Test_window.resize(352, 441)
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
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(20, 260, 118, 26))
        self.timeEdit.setObjectName("timeEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 380, 89, 25))
        self.pushButton.setObjectName("pushButton")
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
        self.label_3.setText(_translate("Test_window", "Fault Time"))
        self.pushButton.setText(_translate("Test_window", "Inject Fault"))
    def Onchanged(self, text):
        print("hello you selected : ", text)
        self.selected_event = text




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Test_window = QtWidgets.QMainWindow()
    ui = Ui_Test_window()
    ui.setupUi(Test_window)
    ui.comboBox.addItem("trajectory")
    ui.comboBox.addItem("joints")
    ui.comboBox.activated[str].connect(ui.Onchanged)
    Test_window.show()
    sys.exit(app.exec_())
