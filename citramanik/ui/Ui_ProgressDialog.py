# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'citramanik_progressbar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from citramanik.ui.citramanik_resources_rc import *


class Ui_CitramanikProgressBar(object):
    def setupUi(self, CitramanikProgressBar):
        CitramanikProgressBar.setObjectName("CitramanikProgressBar")
        CitramanikProgressBar.resize(400, 151)
        self.topFrame = QtWidgets.QFrame(CitramanikProgressBar)
        self.topFrame.setGeometry(QtCore.QRect(0, 0, 400, 41))
        self.topFrame.setStyleSheet("background-color: #b42b6f;\n"
"background-image: url(:/image/imgs/img-bg-sections_progressBar.png);")
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.topFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.wrapper_exporting = QtWidgets.QVBoxLayout()
        self.wrapper_exporting.setObjectName("wrapper_exporting")
        self.label_exporting = QtWidgets.QLabel(self.topFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_exporting.setFont(font)
        self.label_exporting.setStyleSheet("color: #e5e8eb; background:none;")
        self.label_exporting.setObjectName("label_exporting")
        self.wrapper_exporting.addWidget(self.label_exporting)
        self.verticalLayout_6.addLayout(self.wrapper_exporting)
        self.bottom_frame = QtWidgets.QFrame(CitramanikProgressBar)
        self.bottom_frame.setGeometry(QtCore.QRect(0, 40, 400, 111))
        self.bottom_frame.setStyleSheet("background-color: #e5e8eb;")
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.bottom_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.wrapper_progresscontent = QtWidgets.QVBoxLayout()
        self.wrapper_progresscontent.setObjectName("wrapper_progresscontent")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.wrapper_progresscontent.addItem(spacerItem)
        self.progress_bar = QtWidgets.QProgressBar(self.bottom_frame)
        self.progress_bar.setMinimumSize(QtCore.QSize(0, 24))
        self.progress_bar.setStyleSheet("QProgressBar{text-align:center;color: rgb(53, 53, 53)}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: #b42b6f;\n"
"}")
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.wrapper_progresscontent.addWidget(self.progress_bar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.wrapper_progresscontent.addItem(spacerItem1)
        self.wrapper_statuscancel = QtWidgets.QHBoxLayout()
        self.wrapper_statuscancel.setObjectName("wrapper_statuscancel")
        self.label_currentfile = QtWidgets.QLabel(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_currentfile.setFont(font)
        self.label_currentfile.setStyleSheet("color: #b42b6f;")
        self.label_currentfile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_currentfile.setObjectName("label_currentfile")
        self.wrapper_statuscancel.addWidget(self.label_currentfile)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.wrapper_statuscancel.addItem(spacerItem2)
        self.btn_cancel = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_cancel.setMinimumSize(QtCore.QSize(80, 28))
        self.btn_cancel.setStyleSheet("QPushButton{\n"
"color: #fff;\n"
"background-color: #b42b6f;\n"
"border:0px solid;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton::hover{;\n"
"color: #fff;\n"
"background-color: rgb(206, 49, 128);\n"
"border:none;\n"
"}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.wrapper_statuscancel.addWidget(self.btn_cancel)
        self.wrapper_progresscontent.addLayout(self.wrapper_statuscancel)
        self.verticalLayout_7.addLayout(self.wrapper_progresscontent)

        self.retranslateUi(CitramanikProgressBar)
        QtCore.QMetaObject.connectSlotsByName(CitramanikProgressBar)

    def retranslateUi(self, CitramanikProgressBar):
        _translate = QtCore.QCoreApplication.translate
        CitramanikProgressBar.setWindowTitle(_translate("CitramanikProgressBar", "Citramanik - Exporting..."))
        self.label_exporting.setText(_translate("CitramanikProgressBar", "Exporting..."))
        self.label_currentfile.setText(_translate("CitramanikProgressBar", "Preparing..."))
        self.btn_cancel.setText(_translate("CitramanikProgressBar", "Cancel"))
