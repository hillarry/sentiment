# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DELL\Desktop\finalGUI\DlogSysInfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SystemInfo(object):
    def setupUi(self, SystemInfo):
        SystemInfo.setObjectName("SystemInfo")
        SystemInfo.resize(343, 315)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imcon/SysInfo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SystemInfo.setWindowIcon(icon)
        self.sysInfotxtBrowser = QtWidgets.QTextBrowser(SystemInfo)
        self.sysInfotxtBrowser.setGeometry(QtCore.QRect(0, 0, 351, 321))
        self.sysInfotxtBrowser.setStyleSheet("font: 8pt \"Courier New\";")
        self.sysInfotxtBrowser.setObjectName("sysInfotxtBrowser")

        self.retranslateUi(SystemInfo)
        QtCore.QMetaObject.connectSlotsByName(SystemInfo)

    def retranslateUi(self, SystemInfo):
        _translate = QtCore.QCoreApplication.translate
        SystemInfo.setWindowTitle(_translate("SystemInfo", "SystemInfo"))
        self.sysInfotxtBrowser.setHtml(_translate("SystemInfo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">System Info</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">* Powered by Ipython,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">* Designed by PyQt5 Designer</span></p></body></html>"))

import imicons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SystemInfo = QtWidgets.QDialog()
    ui = Ui_SystemInfo()
    ui.setupUi(SystemInfo)
    SystemInfo.show()
    sys.exit(app.exec_())

