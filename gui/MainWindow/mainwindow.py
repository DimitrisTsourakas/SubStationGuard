# This Python file uses the following encoding: utf-8

import sys

from controllers.SystemTypeController import SystemTyperController
from controllers.SoilResistivityController import SoilResistivityController
from controllers.GridCurrentController import GridCurrentController
from controllers.DecrementFactorController import DecrementFactorController
from controllers.SafetyStandardController import SafetyStandardController


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
        
        self.system_type_controller = SystemTyperController(self)

        self.soil_resistivity_controller = SoilResistivityController(self)

        self.grid_current_controller = GridCurrentController(self)
        
        self.decrement_factor_controller = DecrementFactorController(self)
        
        self.safety_standard_controller = SafetyStandardController(self)
        

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())

