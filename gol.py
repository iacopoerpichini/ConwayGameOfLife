import argparse
import sys
from PyQt5.QtWidgets import QApplication
from mvc.controller import ControllerGol
from mvc.model import ModelGol
from mvc.view import GuiGol

def readCmdParams():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--gridSize", type=int, default=50)
    return parser.parse_args()

if __name__ == '__main__':
    # see if user chose grid size on cmd, default 50
    args = readCmdParams()
    app = QApplication(sys.argv)
    # force style for all system to Fusion
    app.setStyle('Fusion')
    # Create the model view controller object
    model = ModelGol(args.gridSize)
    view = GuiGol(model)
    controller = ControllerGol(app, model, view)
    # launch the application
    view.show()
    sys.exit(app.exec_())
