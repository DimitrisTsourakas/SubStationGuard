from .BaseController import BaseController
from . import Validation as validation
from PySide6.QtWidgets import QFileDialog

class SystemTypeController(BaseController):
    def __init__(self, parent):

        super().__init__(parent)
        
        self.ui = parent.ui

        self.parent = parent

        # System Type of MV/LV Substation

        # Make error labels invisible
        self.ui.label_100.setVisible(False)
        self.ui.label_101.setVisible(False)
        self.ui.label_102.setVisible(False)

        # Show options based on comboBox_10
        self.setup_toggle_behavior(
            self.ui.comboBox_10,
            show_on_yes = [
                self.ui.label_49, self.ui.lineEdit_35, self.ui.pushButton
            ],
            show_on_no = [
                self.ui.label_84, self.ui.label_101, self.ui.lineEdit_33
            ]
        )

        # Connect button with browseFile function
        self.ui.pushButton.clicked.connect(self.browseFile)
        
        # Validate Geometric proportionality factor inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_32,
            error_label=self.ui.label_102,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Surface potential proportionality factor inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_33,
            error_label=self.ui.label_101,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid fuction"
        )

        # Validate Fault Duration inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_34,
            error_label=self.ui.label_100,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

    def browseFile(self):
        path, _ = QFileDialog.getOpenFileName(self.parent, "Select Data file", "", "CSV Files (*.csv);;All Files (*)")
        if not path:
            return
        print("Data File Selected: ", path)
        self.ui.lineEdit_35.setText(path)

    def extractParametersFromGui(self):
        def safe_float(text, default=0.0):
            try:
                return float(text)
            except (ValueError, TypeError):
                return default
        return {
            "systemType": str(self.ui.comboBox_9.currentText()),
            "geometricFactor": safe_float(self.ui.lineEdit_32.text()),
            "surfacePotentialFunc": self.ui.lineEdit_33.text(),
            "faultDuration": safe_float(self.ui.lineEdit_34.text()),
        }
    
    def resetParameters(self):
        self.ui.comboBox_9.setCurrentIndex(0)
        self.ui.lineEdit_32.setText("")
        self.ui.lineEdit_33.setText("")
        self.ui.lineEdit_34.setText("")
        self.ui.lineEdit_35.setText("")