# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DELL\Desktop\finalGUI\DesignedWelWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from DesignedHomeWin import Ui_HomeMainWindow

class Ui_DesignedWelWindow(object):

    def openMainWin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeMainWindow()
        self.ui.setupUi(self.window)
        DesignedWelWindow.hide()
        self.window.show()


    
    def setupUi(self, DesignedWelWindow):
        DesignedWelWindow.setObjectName("DesignedWelWindow")
        DesignedWelWindow.resize(762, 326)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imcon/senti2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DesignedWelWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DesignedWelWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_Heading = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Heading.setGeometry(QtCore.QRect(160, 60, 541, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(26)
        self.lbl_Heading.setFont(font)
        self.lbl_Heading.setObjectName("lbl_Heading")
        self.lbl_HeadIcon = QtWidgets.QLabel(self.centralwidget)
        self.lbl_HeadIcon.setGeometry(QtCore.QRect(40, 20, 121, 91))
        self.lbl_HeadIcon.setStyleSheet("image:url(:/imcon/classify1.png)")
        self.lbl_HeadIcon.setText("")
        self.lbl_HeadIcon.setObjectName("lbl_HeadIcon")
        self.lbl_welIcon = QtWidgets.QLabel(self.centralwidget)
        self.lbl_welIcon.setGeometry(QtCore.QRect(620, 150, 51, 41))
        self.lbl_welIcon.setStyleSheet("image:url(:/imcon/senti1.png)")
        self.lbl_welIcon.setText("")
        self.lbl_welIcon.setObjectName("lbl_welIcon")
        self.lbl_wel = QtWidgets.QLabel(self.centralwidget)
        self.lbl_wel.setGeometry(QtCore.QRect(120, 160, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(11)
        self.lbl_wel.setFont(font)
        self.lbl_wel.setObjectName("lbl_wel")
        self.btnOpenMainWindow = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenMainWindow.setGeometry(QtCore.QRect(230, 250, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(11)
        self.btnOpenMainWindow.setFont(font)
        self.btnOpenMainWindow.setStyleSheet("\n"
"color: rgb(133, 66, 199);\n"
"background-color: rgb(0, 209, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imcon/key1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenMainWindow.setIcon(icon1)
        self.btnOpenMainWindow.setObjectName("btnOpenMainWindow")

        #click to open home window
        self.btnOpenMainWindow.clicked.connect(self.openMainWin)
        
        DesignedWelWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DesignedWelWindow)
        self.statusbar.setObjectName("statusbar")
        DesignedWelWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DesignedWelWindow)
        QtCore.QMetaObject.connectSlotsByName(DesignedWelWindow)

    def retranslateUi(self, DesignedWelWindow):
        _translate = QtCore.QCoreApplication.translate
        DesignedWelWindow.setWindowTitle(_translate("DesignedWelWindow", "This is a Welcome Page to You!"))
        self.lbl_Heading.setText(_translate("DesignedWelWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Abusive Word Detection System</span></p></body></html>"))
        self.lbl_wel.setText(_translate("DesignedWelWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#740057;\">Welcome to Our ProjectWork ,Abusive Word Detection System!.</span></p></body></html>"))
        self.btnOpenMainWindow.setText(_translate("DesignedWelWindow", "ACCESS PROJECT"))

import newresourses

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DesignedWelWindow = QtWidgets.QMainWindow()
    ui = Ui_DesignedWelWindow()
    ui.setupUi(DesignedWelWindow)
    DesignedWelWindow.show()
    sys.exit(app.exec_())

