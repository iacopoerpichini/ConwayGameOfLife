import os

import numpy as np
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog

from mvc.boardGol import BoardGoL
from mvc.model import ModelGol
from gui.about import Ui_About
from gui.rules import Ui_Rules
from gui.gui import Ui_GameOfLife

CURRENT_DIR = os.path.dirname(os.path.abspath('__file__'))

class RulesDialog(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set up the user interface from Designer.
        self.guiRules = Ui_Rules()
        self.guiRules.setupUi(self)


class AboutDialog(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set up the user interface from Designer.
        self.guiAbout = Ui_About()
        self.guiAbout.setupUi(self)
        # image = QtGui.QImage("../img/mvc.png")
        # qpixmap = QtGui.QPixmap.fromImage(image)
        # print(image)
        # self.guiAbout.img2.setPixmap(qpixmap)


class GuiGol(QMainWindow):
    def __init__(self, model: ModelGol):
        super().__init__()
        # Set up the user interface from Designer.
        self.gui = Ui_GameOfLife()
        self.gui.setupUi(self)
        # Create about, rules dialog and action quit.
        self._aboutDialog = AboutDialog()
        self._rulesDialog = RulesDialog()
        self.gui.actionAbout.triggered.connect(self._aboutDialog.exec_)
        self.gui.actionRules.triggered.connect(self._rulesDialog.exec_)
        self.gui.actionQuit.triggered.connect(QApplication.exit)

        # Create action for load and save
        self.gui.actionLoad.triggered.connect(self._load)
        self.gui.actionSave.triggered.connect(self._save)

        # set windows non resizable avoid graphics bug on resize
        self.setFixedSize(618, 750)

        # Set the GUI to observe the Game of Life Model
        self._model = model
        self._model.observe(self._updateView)
        self._updateView()

        # set central board GoL
        # Add the custom widget to the central QFrame to display the current state of the GOL grid
        self.board = BoardGoL(model)
        self.gui.boardLayout.addWidget(self.board, 0, 0)

    def _load(self):
        """
        Action connected to load menu item
        load a numpy array with load txt from numpy
        """
        print('load')
        self._model.clearGrid()
        try:
            path = QFileDialog.getOpenFileName(directory=CURRENT_DIR)
            if path[0] !='':
                grid = np.loadtxt(path[0], dtype=np.uint8)
                self._model.setGrid(grid)
        except Exception:
            print('Exception load')

    def _save(self):
        """
        Action connected for saving a board
        save a file txt from numpy array with save txt from numpy
        """
        print('save')
        grid = self._model.getGrid()
        try:
            path = QFileDialog.getSaveFileName(directory=CURRENT_DIR)
            if path[0] != '':
                np.savetxt(path[0] + '.txt', grid)
        except Exception:
            print('Exception save')


    def _updateView(self):
        """
        Update the play/pause button and the speed label if the simulation is running
        """
        self.gui.speedLabel.setText(f"Speed: {self._model.getSpeed()} (fps)")
        if self._model.isRunning():
            self.gui.play.setText("Pause")
            self.gui.sliderSpeed.setDisabled(True)
            self.gui.singleStep.setDisabled(True)
        else:
            self.gui.play.setText("Play")
            self.gui.sliderSpeed.setDisabled(False)
            self.gui.singleStep.setDisabled(False)

    def buttonPlay(self, slot):
        """
        slot of button play
        """
        self.gui.play.clicked.connect(slot)

    def buttonReset(self, slot):
        """
        slot of button reset
        """
        self.gui.reset.clicked.connect(slot)

    def buttonSingleStep(self, slot):
        """
        slot of button single step
        """
        self.gui.singleStep.clicked.connect(slot)

    def sliderSpeed(self, slot):
        """
        slot of slider speed
        """
        self.gui.sliderSpeed.valueChanged.connect(slot)