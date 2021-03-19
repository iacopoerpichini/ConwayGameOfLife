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
    Model class for game of life define param for the backend
    """
    def __init__(self):
        super().__init__()
        # parameters
        self._speed = 1
        self._runnig = False
        self._grid = np.zeros((10,20), dtype=np.uint8)

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


