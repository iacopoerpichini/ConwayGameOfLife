from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from model import ModelGol


class boardGoL(QLabel):
    # Signal definition
    changeStateSignal = QtCore.pyqtSignal(object)

    def __init__(self, model: ModelGol):
        QtWidgets.QGraphicsScene.__init__(self)

        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(1, 1)  # To allow the QLabel to shrink also with a pixmap attached

        # Connect to the model and show the initial grid
        self._model = model
        self._model.observe(self.updateGrid)
        self.updateGrid()


    def updateGrid(self):
        """"
        Show the image relative to the board
        """
        print('siamo in update grid')
        # take the grid from model and transorm it into a image
        grid = self._model.getGrid()

        width = grid.shape[0]
        height = grid.shape[1]
        bytes = width
        image = QImage(grid, width, height, bytes, QImage.Format_Indexed8)
        qpixmap = QPixmap.fromImage(image)


    def mousePressEvent(self, event):
        """
        Mouse event on click in the GoL board
        """
        try:
            if not self._model.isRunning():
                ep = event.pos()
                print('pos x:' + ep.x().__str__() + ' pos y: ' + ep.y().__str__())
                # left click fill cell or delete cell
                if event.button() == QtCore.Qt.LeftButton:
                    self.changeStateSignal.emit([ep.x(), ep.y()])
        except Exception:
            print('Mouse press event exception')
            pass


