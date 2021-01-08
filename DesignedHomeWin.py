# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DELL\Desktop\finalGUI\DesignedHomeWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from DlogSysInfo import Ui_SystemInfo
from DlogExtLink import Ui_ExternalLinks
from DlogAbtUs import Ui_AboutUs
from PyQt5.QtWidgets import QMessageBox
import prouitest

class Ui_HomeMainWindow(object):
    def openSysInfo(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_SystemInfo()
        self.ui.setupUi(self.window)
        self.window.show()

    def openExternalLink(self):
        
        self.window = QtWidgets.QDialog()
        self.ui =Ui_ExternalLinks()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAboutUs(self):
        
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AboutUs()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, HomeMainWindow):
        HomeMainWindow.setObjectName("HomeMainWindow")
        HomeMainWindow.resize(1041, 622)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imcon/senti2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HomeMainWindow.setWindowIcon(icon)
        #HomeMainWindow.setStyleSheet("border-color: rgb(85, 0, 0);\n"
#"background-color: rgb(255, 246, 247);\n"
#"")
        HomeMainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.068, y1:1, x2:0.113636, y2:0.807, stop:0.409091 rgba(221, 115, 106, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(HomeMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_Heading = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Heading.setGeometry(QtCore.QRect(370, 40, 541, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(26)
        self.lbl_Heading.setFont(font)
        self.lbl_Heading.setObjectName("lbl_Heading")
        self.lbl_MainIcon = QtWidgets.QLabel(self.centralwidget)
        self.lbl_MainIcon.setGeometry(QtCore.QRect(270, 0, 91, 81))
        self.lbl_MainIcon.setStyleSheet("image:url(:/imcon/classify1.png)")
        self.lbl_MainIcon.setText("")
        self.lbl_MainIcon.setObjectName("lbl_MainIcon")
        self.label_entertext = QtWidgets.QLabel(self.centralwidget)
        self.label_entertext.setGeometry(QtCore.QRect(70, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_entertext.setFont(font)
        self.label_entertext.setObjectName("label_entertext")
        self.lineEdit_InputText = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_InputText.setGeometry(QtCore.QRect(190, 180, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.lineEdit_InputText.setFont(font)
        self.lineEdit_InputText.setObjectName("lineEdit_InputText")
        self.lineEdit_InputText.setPlaceholderText("     Enter the text what you want to type     ")
        self.btnAnalyze = QtWidgets.QPushButton(self.centralwidget)
        self.btnAnalyze.setGeometry(QtCore.QRect(840, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.btnAnalyze.setFont(font)
        self.btnAnalyze.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-color: rgb(239, 0, 0);")
        self.btnAnalyze.clicked.connect(self.on_click)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imcon/system2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAnalyze.setIcon(icon1)
        self.btnAnalyze.setObjectName("btnAnalyze")
        self.lbl_Language = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Language.setGeometry(QtCore.QRect(120, 310, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.lbl_Language.setFont(font)
        self.lbl_Language.setObjectName("lbl_Language")
        self.label_sentiment = QtWidgets.QLabel(self.centralwidget)
        self.label_sentiment.setGeometry(QtCore.QRect(120, 400, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_sentiment.setFont(font)
        self.label_sentiment.setObjectName("label_sentiment")
        self.label_classification = QtWidgets.QLabel(self.centralwidget)
        self.label_classification.setGeometry(QtCore.QRect(710, 310, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_classification.setFont(font)
        self.label_classification.setObjectName("label_classification")
        self.btnAbusive = QtWidgets.QPushButton(self.centralwidget)

        self.btnAbusive.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(255, 97, 90, 255), stop:0.0511364 rgba(252, 63, 131, 14), stop:1 rgba(255, 36, 36, 228));")


        
        self.btnAbusive.setGeometry(QtCore.QRect(610, 380, 161, 71))
        self.btnAbusive.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.btnAbusive.setFont(font)
##        self.btnAbusive.setStyleSheet("color: rgb(255, 0, 0);\n"
##"gridline-color: rgb(193, 0, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imcon/Icon4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAbusive.setIcon(icon2)
        self.btnAbusive.setObjectName("btnAbusive")
        
        self.btnNonAbusive = QtWidgets.QPushButton(self.centralwidget)

        self.btnNonAbusive.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 207, 0, 255), stop:0.0511364 rgba(252, 63, 131, 14), stop:0.426136 rgba(16, 203, 4, 221));")
   
        
        self.btnNonAbusive.setGeometry(QtCore.QRect(790, 380, 161, 71))
        self.btnNonAbusive.setEnabled(False)
       
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.btnNonAbusive.setFont(font)
##        self.btnNonAbusive.setStyleSheet("color: rgb(0, 150, 0);\n"
##"gridline-color: rgb(0, 166, 0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imcon/Icon3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNonAbusive.setIcon(icon3)
        self.btnNonAbusive.setObjectName("btnNonAbusive")
        HomeMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HomeMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        HomeMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HomeMainWindow)
        self.statusbar.setObjectName("statusbar")
        HomeMainWindow.setStatusBar(self.statusbar)
        self.actionSystem_Info = QtWidgets.QAction(HomeMainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imcon/SysInfo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSystem_Info.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.actionSystem_Info.setFont(font)
        self.actionSystem_Info.setObjectName("actionSystem_Info")
        
        #open System Info Dialog
        self.actionSystem_Info.triggered.connect(self.openSysInfo)
        
        self.actionExternal_Link = QtWidgets.QAction(HomeMainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imcon/link3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExternal_Link.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.actionExternal_Link.setFont(font)
        self.actionExternal_Link.setObjectName("actionExternal_Link")

        #open External Links Dialog
        self.actionExternal_Link.triggered.connect(self.openExternalLink)
        
        self.actionAbout_Us = QtWidgets.QAction(HomeMainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imcon/about2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Us.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.actionAbout_Us.setFont(font)
        self.actionAbout_Us.setObjectName("actionAbout_Us")

        #open About Us Dialog
        self.actionAbout_Us.triggered.connect(self.openAboutUs)
        
        self.menuAbout.addAction(self.actionSystem_Info)
        self.menuAbout.addAction(self.actionExternal_Link)
        self.menuAbout.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(HomeMainWindow)
        self.btnAnalyze.clicked.connect(self.lineEdit_InputText.clear)
        QtCore.QMetaObject.connectSlotsByName(HomeMainWindow)

    def retranslateUi(self, HomeMainWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeMainWindow.setWindowTitle(_translate("HomeMainWindow", "Abusive Word Detection System"))
        self.lbl_Heading.setText(_translate("HomeMainWindow", "<html><head/><body><p><span style=\" color:#55007f;\">Abusive Word Detection System</span></p></body></html>"))
        self.label_entertext.setText(_translate("HomeMainWindow", "Enter Text"))
        self.btnAnalyze.setText(_translate("HomeMainWindow", "Analyze"))
        self.lbl_Language.setText(_translate("HomeMainWindow", "<html><head/><body><p><span style=\" color:#47006b;\">Language:</span><span style=\" color:#00b900;\">English</span></p></body></html>"))
        self.label_sentiment.setText(_translate("HomeMainWindow", "<html><head/><body><p><span style=\" color:#3e005d;\">Accuracy:</span></p></body></html>"))
        self.label_classification.setText(_translate("HomeMainWindow", "<html><head/><body><p><span style=\" color:#55007f;\">Classification</span></p></body></html>"))
        self.btnAbusive.setText(_translate("HomeMainWindow", "Abusive"))
        self.btnNonAbusive.setText(_translate("HomeMainWindow", "NonAbusive"))
        self.menuAbout.setTitle(_translate("HomeMainWindow", "About"))
        self.actionSystem_Info.setText(_translate("HomeMainWindow", "System Info"))
        self.actionExternal_Link.setText(_translate("HomeMainWindow", "External Link"))
        self.actionAbout_Us.setText(_translate("HomeMainWindow", "About Us"))
        #self.actionAbout_Us.setShortcut(_translate("HomeMainWindow", "Ctrl+U"))
    def on_click(self):
        text_input=self.lineEdit_InputText.text()
        x=str(text_input)
        command=prouitest.testing(x)
        self.label_sentiment.setText("<html><head/><body><p><span style=\" color:#3e005d;\">Accuracy:85.88%</span></p></body></html>") 
        if command==1:
            #self.btnAnalyze.clicked.connect(self.show_popup)
            #self.btnAnalyze.clicked.connect(
            self.btnAbusive.setEnabled(True)

            #self.btnAbusive.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(255, 97, 90, 255), stop:0.0511364 rgba(252, 63, 131, 14), stop:1 rgba(255, 36, 36, 228));")

            QMessageBox.warning(QMessageBox(),"Warning","We can't allow your abusive message")
            self.btnAbusive.setEnabled(False)
           
            #self.btnAbusive.setEnabled(True)
            #self.btnAbusive.clicked.connect(self.show_popup)
        elif command==0:
            
            #self.btnAnalyze.clicked.connect(self.show)
            self.btnNonAbusive.setEnabled(True)

            #self.btnNonAbusive.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 207, 0, 255), stop:0.0511364 rgba(252, 63, 131, 14), stop:0.585227 rgba(16, 203, 4, 221));")
   
            QMessageBox.information(QMessageBox(),"Allow","We allow your message")
        
            self.btnNonAbusive.setEnabled(False)
            #self.btnNonAbusive.clicked.connect(self.show)
        #self.label_sentiment.setText("<html><head/><body><p><span style=\" color:#3e005d;\">Accuracy:85.88%</span></p></body></html>")      
              
    '''def show_popup(self):
        msg=QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Your sentence has abusive words.We can't allow your message.")
        x=msg.exec_()
        self.btnAbusive.setEnabled(False)'''
    
    '''def show(self):
        msg=QMessageBox()
        msg.setWindowTitle("Allow")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Your message has no abusive words.We can allow your message.")
        x=msg.exec_()
        self.btnNonAbusive.setEnabled(False)'''

        
import newresourses

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeMainWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeMainWindow()
    ui.setupUi(HomeMainWindow)
    HomeMainWindow.show()
    sys.exit(app.exec_())

