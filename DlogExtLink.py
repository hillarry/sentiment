# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DELL\Desktop\finalGUI\DlogExtLink.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExternalLinks(object):
    def setupUi(self, ExternalLinks):
        ExternalLinks.setObjectName("ExternalLinks")
        ExternalLinks.resize(343, 313)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imcon/link1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExternalLinks.setWindowIcon(icon)
        self.ExternalLinktextBrowser = QtWidgets.QTextBrowser(ExternalLinks)
        self.ExternalLinktextBrowser.setGeometry(QtCore.QRect(0, 0, 351, 321))
        self.ExternalLinktextBrowser.setObjectName("ExternalLinktextBrowser")

        self.retranslateUi(ExternalLinks)
        QtCore.QMetaObject.connectSlotsByName(ExternalLinks)

    def retranslateUi(self, ExternalLinks):
        _translate = QtCore.QCoreApplication.translate
        ExternalLinks.setWindowTitle(_translate("ExternalLinks", "External Links"))
        self.ExternalLinktextBrowser.setHtml(_translate("ExternalLinks", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">External Links</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">- </span><a href=\"www.pyorg.com\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">Python</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">- </span><a href=\"www.pyqt.com\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">PyQt</span></a></p></body></html>"))

import imicons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExternalLinks = QtWidgets.QDialog()
    ui = Ui_ExternalLinks()
    ui.setupUi(ExternalLinks)
    ExternalLinks.show()
    sys.exit(app.exec_())

