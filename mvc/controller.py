from math import floor
import numpy as np
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from mvc.model import ModelGol
from mvc.view import GuiGol


class ControllerGol:

    # Signal definition
    changeStateSignal = QtCore.pyqtSignal(object)

    def __init__(self, application: QApplication, model: ModelGol, view: GuiGol):
        self._application = application
        # load the model and the view in the controller
        self._model = model
        self._view = view

        # timer for play pause action
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.step)

        # connect to the controller all the elements on the view
        self._view.buttonPlay(self.play)
        self._view.buttonSingleStep(self.step)
        self._view.buttonReset(self.reset)
        self._view.sliderSpeed(self.setSliderSpeed)
        self._view.board.changeStateSignal.connect(self.changeGrid)


    def play(self):
        """
        Start or stop game of life
        """
        self._model.setRunning(not self._model.isRunning())
        if self._model.isRunning():
            msec = 1 / self._model.getSpeed() * 1000
            self._timer.setInterval(msec)
            self._timer.start()
        else:
            self._timer.stop()

    def step(self):
        """
        Compute a game of life iteration and generate a new frame
        """
        grid = self._model.getGrid()
        newGrid = np.zeros(grid.shape, dtype=np.uint8)
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if self._neighbors(i, j) == 3:
                    newGrid[i, j] = 255 # born a new cell
                elif self._neighbors(i, j) >= 4 or self._neighbors(i, j) <= 1:
                    newGrid[i, j] = 0 # die for over/under population
                elif self._neighbors(i, j) == 2:
                    newGrid[i, j] = grid[i, j]
        self._model.setGrid(newGrid)

    def _neighbors(self, i, j):
        """
        Return the number of neighbors of a node i, j
        :return: # neighbours
        """
        grid = self._model.getGrid()
        indexes = [] # contains the filter for the conv 3x3
        indexes.append([i - 1, j - 1])
        indexes.append([i, j - 1])
        indexes.append([i + 1, j - 1])
        indexes.append([i - 1, j])
        indexes.append([i + 1, j])
        indexes.append([i - 1, j + 1])
        indexes.append([i, j + 1])
        indexes.append([i + 1, j + 1])
        indexes = self._checkIndexes(indexes, grid.shape[0], grid.shape[1])
        neighbours = 0
        for index in indexes:
            neighbours += grid[index[0], index[1]]
        return floor(neighbours / 255) #255 is for the colour in the bitmap

    def _checkIndexes(self, indexes, maxRows, maxCols):
        """
        use for control the paddings cell
        """
        goodIndexes = []
        for index in indexes:
            if index[0] >= 0 and index[1] >= 0 and index [0] < maxRows and index[1] < maxCols:
                goodIndexes.append(index)
        return goodIndexes

    def reset(self):
        """
        Clear the grid in the model and update the view
        if the simulation is running stop the simulation
        """
        self._model.clearGrid()
        if self._model.isRunning():
            self._model.setRunning(False)
            self._timer.stop()

        # print(self._model.getGrid()) ok
        self._view.board.updateGrid()


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
        maxWidth, maxHeight = self._view.board.width(), self._view.board.height()
        if x <= maxWidth and y <= maxHeight:
            numberCellH, numberCellW = maxHeight/grid.shape[1], maxWidth/grid.shape[0]
            # change the index of row and col for display the right figure cause numpy array indexes
            col, row = floor(x/numberCellW), floor(y/numberCellH)
            if col >= 0 and row >= 0:
                if grid[row, col] == 0:
                    grid[row, col] = 255 # white color
                elif grid[row, col] == 255:
                    grid[row, col] = 0 # black color
                self._model.setGrid(grid)





