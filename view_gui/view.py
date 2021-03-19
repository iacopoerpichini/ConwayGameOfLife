from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication

from boardGoL import boardGoL
from model import ModelGol
from view_gui.about import Ui_About
from view_gui.rules import Ui_Rules
from view_gui.gui import Ui_GameOfLife

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

        # Create action for load and save       # not implemented yet
        """ da capire come chiamare finestra esterna per salvare o caricare"""
        # self.gui.actionLoad.triggered.connect()
        # self.gui.actionSave.triggered.connect()

        # set windows non resizable
        self.setFixedSize(618, 750)
        """ usare yarn per settare tutte le costanti dopo """

        # Set the GUI to observe the Game of Life Model
        self._model = model
        self._model.observe(self.updateView)
        self.updateView()

        # set central board GoL
        # Add the custom widget to the central QFrame to display the current state of the GOL grid
        self.board = boardGoL(model)
        self.gui.boardLayout.addWidget(self.board, 0, 0)

    def updateView(self):
        """
        Update the play/pause button and the speed label if the simulation is running
        """
        self.gui.speedLabel.setText(f"Speed: {self._model.getSpeed()} (fps)")
        if self._model.isRunning():
            self.gui.play.setText("Pause")
            self.gui.sliderSpeed.setDisabled(True)
        else:
            self.gui.play.setText("Play")
            self.gui.sliderSpeed.setDisabled(False)

    def buttonPlay(self, slot):
        self.gui.play.clicked.connect(slot)

    def buttonReset(self, slot):
        self.gui.reset.clicked.connect(slot)

    def buttonSingleStep(self, slot):
        self.gui.singleStep.clicked.connect(slot)

    def sliderSpeed(self, slot):
        self.gui.sliderSpeed.valueChanged.connect(slot)

