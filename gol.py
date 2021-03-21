import sys
from PyQt5.QtWidgets import QApplication
from mvc.controller import ControllerGol
from mvc.model import ModelGol
from mvc.view import GuiGol

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # force style for all system to Fusion
    app.setStyle('Fusion')
    # Create the model view controller object
    model = ModelGol()
    view = GuiGol(model)
    controller = ControllerGol(app, model, view)
    # launch the application
    view.show()
    sys.exit(app.exec_())
