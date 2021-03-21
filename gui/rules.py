# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rules.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Rules(object):
    def setupUi(self, Rules):
        Rules.setObjectName("Rules")
        Rules.resize(632, 447)
        Rules.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Rules)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Rules)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Rules)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(Rules)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(Rules)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_9 = QtWidgets.QLabel(Rules)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_5 = QtWidgets.QLabel(Rules)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Rules)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(Rules)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(Rules)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.buttonBox = QtWidgets.QDialogButtonBox(Rules)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Rules)
        self.buttonBox.accepted.connect(Rules.accept)
        self.buttonBox.rejected.connect(Rules.reject)
        QtCore.QMetaObject.connectSlotsByName(Rules)

    def retranslateUi(self, Rules):
        _translate = QtCore.QCoreApplication.translate
        Rules.setWindowTitle(_translate("Rules", "Rules"))
        self.label_2.setText(_translate("Rules", "Game of Life Rules"))
        self.label.setText(_translate("Rules", "The simulation of starts from an initial state of populated locations and then progresses through time.\n"
"\n"
"The evolution of the board state is governed by a few simple rules:\n"
"\n"
"1. Each populated location with one or zero neighbors dies (from loneliness).\n"
"\n"
"2. Each populated location with four or more neighbors dies (from overpopulation).\n"
"\n"
"3. Each populated location with two or three neighbors survives.\n"
"\n"
"4. Each unpopulated location that becomes populated if it has exactly three populated neighbors.\n"
"\n"
"5. All updates are performed simultaneously in parallel."))
        self.label_3.setText(_translate("Rules", "Usage"))
        self.label_4.setText(_translate("Rules", "For add a cell just click in a square of the central panel."))
        self.label_9.setText(_translate("Rules", "It\'s possible to hold click on left button of mouse and drag for set to alive more cells. "))
        self.label_5.setText(_translate("Rules", "Button Play start and stop the simulation, Single step do a single iteration of Game of Live evolution."))
        self.label_6.setText(_translate("Rules", "Reset button stop the simulation if it\'s running and clear all the board."))
        self.label_7.setText(_translate("Rules", "When the simulation is not running is possible to set the speed of simulation with the Speed Slider."))
        self.label_8.setText(_translate("Rules", "Finally is possible to load/save board state with the action in the file menu."))

