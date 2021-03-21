from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel
from mvc.model import ModelGol


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
        width, height = grid.shape[0], grid.shape[1]
        qpixmap = QPixmap.fromImage(QImage(grid, width, height, width, QImage.Format_Indexed8))
        # Scale the created QPixmap to fit the widget
        self.setPixmap(qpixmap.scaled(self.width(), self.height()))

    def mousePressEvent(self, event):
        """
        Mouse event on click in the GoL board
        """
        try:
            if not self._model.isRunning():  # if the model is running i cant draw
                click = event.pos()
                print('pos x:' + click.x().__str__() + ' pos y: ' + click.y().__str__())
                # left click fill cell or delete cell
                if event.button() == QtCore.Qt.LeftButton:
                    self.changeStateSignal.emit([click.x(), click.y()])
        except Exception:
            print('Mouse press event exception')
            pass

    def mouseMoveEvent(self, event):
        """
        Left click pressed for draw cell
        """
        try:
            if not self._model.isRunning():  # if the model is running i cant draw
                click = event.pos()
                # hold left click for draw/delete cell
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.changeStateSignal.emit([click.x(), click.y()])
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
