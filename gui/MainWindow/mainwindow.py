# This Python file uses the following encoding: utf-8

import sys

from controllers.SeparationDistanceController import SeparationDistanceController

from PySide6.QtWidgets import QApplication, QMainWindow


# Important:

# You need to run the following command to generate the ui_form.py file

#     pyside6-uic form.ui -o ui_form.py, or

#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_MainWindow



class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        
        self.separation_distance_controller = SeparationDistanceController(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())

