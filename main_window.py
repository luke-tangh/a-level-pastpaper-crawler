# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 134)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(12, 12, 321, 88))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SubjectLabel = QtWidgets.QLabel(self.widget)
        self.SubjectLabel.setObjectName("SubjectLabel")
        self.verticalLayout_2.addWidget(self.SubjectLabel)
        self.YearLabel = QtWidgets.QLabel(self.widget)
        self.YearLabel.setObjectName("YearLabel")
        self.verticalLayout_2.addWidget(self.YearLabel)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.SubjectComboBox = QtWidgets.QComboBox(self.widget)
        self.SubjectComboBox.setObjectName("SubjectComboBox")
        self.SubjectComboBox.addItem("")
        self.SubjectComboBox.addItem("")
        self.SubjectComboBox.addItem("")
        self.SubjectComboBox.addItem("")
        self.SubjectComboBox.addItem("")
        self.SubjectComboBox.addItem("")
        self.SubjectComboBox.addItem("")
        self.SubjectComboBox.addItem("")
        self.SubjectComboBox.addItem("")
        self.verticalLayout.addWidget(self.SubjectComboBox)
        self.YearComboBox = QtWidgets.QComboBox(self.widget)
        self.YearComboBox.setObjectName("YearComboBox")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.verticalLayout.addWidget(self.YearComboBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.SubmitButton = QtWidgets.QPushButton(self.widget)
        self.SubmitButton.setObjectName("SubmitButton")
        self.gridLayout.addWidget(self.SubmitButton, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SubjectLabel.setText(_translate("MainWindow", "Subject"))
        self.YearLabel.setText(_translate("MainWindow", "Year"))
        self.SubjectComboBox.setItemText(0, _translate("MainWindow", "9231 Mathematics - Further"))
        self.SubjectComboBox.setItemText(1, _translate("MainWindow", "9479 Art & Design"))
        self.SubjectComboBox.setItemText(2, _translate("MainWindow", "9489 History"))
        self.SubjectComboBox.setItemText(3, _translate("MainWindow", "9608 Computer Science (old)"))
        self.SubjectComboBox.setItemText(4, _translate("MainWindow", "9618 Computer Science (new)"))
        self.SubjectComboBox.setItemText(5, _translate("MainWindow", "9700 Biology"))
        self.SubjectComboBox.setItemText(6, _translate("MainWindow", "9701 Chemistry"))
        self.SubjectComboBox.setItemText(7, _translate("MainWindow", "9702 Physics"))
        self.SubjectComboBox.setItemText(8, _translate("MainWindow", "9709 Mathematics"))
        self.YearComboBox.setItemText(0, _translate("MainWindow", "2022"))
        self.YearComboBox.setItemText(1, _translate("MainWindow", "2021"))
        self.YearComboBox.setItemText(2, _translate("MainWindow", "2020"))
        self.YearComboBox.setItemText(3, _translate("MainWindow", "2019"))
        self.YearComboBox.setItemText(4, _translate("MainWindow", "2018"))
        self.YearComboBox.setItemText(5, _translate("MainWindow", "2017"))
        self.YearComboBox.setItemText(6, _translate("MainWindow", "2016"))
        self.YearComboBox.setItemText(7, _translate("MainWindow", "2015"))
        self.YearComboBox.setItemText(8, _translate("MainWindow", "2014"))
        self.YearComboBox.setItemText(9, _translate("MainWindow", "2013"))
        self.YearComboBox.setItemText(10, _translate("MainWindow", "2012"))
        self.SubmitButton.setText(_translate("MainWindow", "Download"))
