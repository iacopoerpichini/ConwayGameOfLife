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
        Rules.resize(671, 392)
        Rules.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Rules)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Rules)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(Rules)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(Rules)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Rules)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
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
        self.label_4.setText(_translate("Rules", "For add a cel just click in a square of the central panel.\n"
"\n"
" Click button play for run the simulation.\n"
"\n"
"Is possible to stop the simulation and modifying the state of the board.\n"
"is also possible to make a single step of the simulation and choose the speed."))

