import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal

# observable class see at lesson for observe value changed in model
class Observable(QObject):
    value_changed = pyqtSignal(object)

    def __init__(self):
        super().__init__()

    def observe(self, slot):
        self.value_changed.connect(slot)

    def notify(self):
        self.value_changed.emit(self)

class ModelGol(Observable):
    """
    Model class for game of life
    Represent the raw data for the evolution bord of GoL, the flag relative to the run action of the program and the
    state of speed slider
    """
    def __init__(self, gridSize):
        super().__init__()
        # parameters
        self._speed = 15 # default 15 fps 1 min 30 max
        self._runnig = False
        self._gridSize = gridSize
        self._grid = np.zeros((self._gridSize,self._gridSize), dtype=np.uint8) # square grid
        self._palette = 'bw'

    """
        getter and setter method of data model variables
    """
    def getSpeed(self):
        return self._speed

    def setSpeed(self, speed):
        self._speed = speed
        self.notify()

    def isRunning(self):
        return self._runnig

    def setRunning(self, foo):
        self._runnig = foo
        self.notify()

    def getGrid(self):
        return self._grid

    def setGrid(self, grid):
        self._grid = grid
        self.notify()

    def getPalette(self):
        return self._palette

    def setPalette(self, palette):
        self._palette = palette
        self.notify()

    def clearGrid(self):
        self._grid = np.zeros((self._gridSize,self._gridSize), dtype=np.uint8) # square grid


