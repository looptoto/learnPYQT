# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 70, 271, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 100, 251, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.checkBox_Under = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Under.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.checkBox_Under.setObjectName("checkBox_Under")
        self.checkBox_Italic = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Italic.setGeometry(QtCore.QRect(90, 20, 71, 16))
        self.checkBox_Italic.setObjectName("checkBox_Italic")
        self.checkBox_Bold = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Bold.setGeometry(QtCore.QRect(160, 20, 71, 16))
        self.checkBox_Bold.setObjectName("checkBox_Bold")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 160, 261, 51))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_black = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_black.setGeometry(QtCore.QRect(0, 20, 89, 16))
        self.radioButton_black.setObjectName("radioButton_black")
        self.radioButton_Red = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_Red.setGeometry(QtCore.QRect(60, 20, 89, 16))
        self.radioButton_Red.setObjectName("radioButton_Red")
        self.radioButton_Blue = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_Blue.setGeometry(QtCore.QRect(110, 20, 89, 16))
        self.radioButton_Blue.setObjectName("radioButton_Blue")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 240, 301, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_quit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout.addWidget(self.pushButton_quit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_confirm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.horizontalLayout.addWidget(self.pushButton_confirm)
        self.pushButton_clear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)

        self.retranslateUi(Dialog)
        self.pushButton_confirm.clicked.connect(Dialog.accept)
        self.pushButton_quit.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "呆萌2-3 信号 槽点"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "PyQt5 cookbook\n"
"Python and QT"))
        self.checkBox_Under.setText(_translate("Dialog", "UnderLine"))
        self.checkBox_Italic.setText(_translate("Dialog", "Italic"))
        self.checkBox_Bold.setText(_translate("Dialog", "Bold"))
        self.radioButton_black.setText(_translate("Dialog", "Black"))
        self.radioButton_Red.setText(_translate("Dialog", "Red"))
        self.radioButton_Blue.setText(_translate("Dialog", "Blue"))
        self.pushButton_quit.setText(_translate("Dialog", "退出"))
        self.pushButton_confirm.setText(_translate("Dialog", "确定"))
        self.pushButton_clear.setText(_translate("Dialog", "清空"))
