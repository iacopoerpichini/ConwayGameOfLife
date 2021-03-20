from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from model import ModelGol


class BoardGoL(QLabel):

    # Signal definition
    changeStateSignal = QtCore.pyqtSignal(object)

    def __init__(self, model: ModelGol):
        QtWidgets.QGraphicsScene.__init__(self)
        # Connect to the model and show the initial grid
        self._model = model
        self._model.observe(self.updateGrid)
        self.updateGrid()

    def updateGrid(self):
        """"
        Show the image relative to the board
        """
        # take the grid from model and transorm it into a image
        grid = self._model.getGrid()

        width = grid.shape[0]
        height = grid.shape[1]
        image = QImage(grid, width, height, width, QImage.Format_Indexed8)
        qpixmap = QPixmap.fromImage(image)
        # Scale the created QPixmap to fit the widget
        self.setPixmap(qpixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio))

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

    def mouseMoveEvent(self, event):
        """
        Left click pressed for draw cell
        """
        try:
            ep = event.pos()
            if event.buttons() == QtCore.Qt.LeftButton:
                self.changeStateSignal.emit([ep.x(), ep.y()])
        except Exception:
            print('Mouse move event exception')
            pass

    def resizeEvent(self, event):
        """
        Set the inital grid for fit the dimension of the widget
        """
        try:
            self.updateGrid()
        except Exception:
            print('Failed initial resize')
            pass
