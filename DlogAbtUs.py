# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DELL\Desktop\finalGUI\DlogAbtUs.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutUs(object):
    def setupUi(self, AboutUs):
        AboutUs.setObjectName("AboutUs")
        AboutUs.resize(478, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imcon/about1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutUs.setWindowIcon(icon)
        self.AboutUstextBrowser = QtWidgets.QTextBrowser(AboutUs)
        self.AboutUstextBrowser.setGeometry(QtCore.QRect(0, 0, 491, 321))
        self.AboutUstextBrowser.setObjectName("AboutUstextBrowser")

        self.retranslateUi(AboutUs)
        QtCore.QMetaObject.connectSlotsByName(AboutUs)

    def retranslateUi(self, AboutUs):
        _translate = QtCore.QCoreApplication.translate
        AboutUs.setWindowTitle(_translate("AboutUs", "About Us"))
        self.AboutUstextBrowser.setHtml(_translate("AboutUs", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">About Us</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> We are the Project Group(I) ,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       warmly supervised by Daw Yin Min Oo</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> The participents are hereby -</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\t Hein Win Htun (VIT-3) \t Htet Htet Mon (VIT-1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\t Zaw Lynn Htet (VIT-28) \t Ei Ei Phyoe (VIT-7)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> \t\t\t Hnin Nandar Myint (VIT-10)</span></p></body></html>"))

import imicons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutUs = QtWidgets.QDialog()
    ui = Ui_AboutUs()
    ui.setupUi(AboutUs)
    AboutUs.show()
    sys.exit(app.exec_())

