from math import floor

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

from model import ModelGol
from view_gui.view import GuiGol



class ControllerGol:

    # Signal definition
    changeStateSignal = QtCore.pyqtSignal(object)

    def __init__(self, application: QApplication, model: ModelGol, view: GuiGol):
        self._application = application
        # load the model and the view in the controller
        self._model = model
        self._view = view

        # connect to the controller all the elements on the view
        view.buttonPlay(self.play)

        self._view.board.changeStateSignal.connect(self.changeGrid)

    def play(self):
        """
        Start or stop game of life
        """
        if self._model.isRunning():
            self._model.setRunning(foo=False)
        else:
            self._model.setRunning(foo=True)

    def setSliderSpeed(self, speed):
        """
        Set the speed of simulation
        """
        self._model.setSpeed(speed)

    def changeGrid(self, coord):
        """
        Load the coord of the new point and emit the signal for display the new image
        """
        grid = self._model.getGrid()
        x, y = coord[0], coord[1]

        # remove the padding of external widget
        # maxWidth = self._view.gui.graphicsView.frameGeometry().width() - self._view.gui.graphicsView.x()
        # maxHeight = self._view.gui.graphicsView.frameGeometry().height() - self._view.gui.graphicsView.y()

        maxWidth = self._view.board.width()
        maxHeight = self._view.board.height()

        cell_h, cell_w = maxHeight/grid.shape[1], maxWidth/grid.shape[0]

        row, col = floor(x/cell_w), floor(y/cell_h)

        if grid[row, col] == 0:
            grid[row, col] = 1
        elif grid[row, col] == 1:
            grid[row, col] = 0

        print(grid)
        self._model.setGrid(grid)




