from .BaseController import BaseController
from . import Validation as validation

class GridCurrentController(BaseController):
    def __init__(self, parent):

        super().__init__(parent)
        
        self.ui = parent.ui

        self.parent = parent

        # Calculate Maximum Grid Current according to IEEE Std 80

        # Make error labels invisible
        self.ui.label_97.setVisible(False)
        self.ui.label_98.setVisible(False)
        self.ui.label_99.setVisible(False)

        # Show options based on comboBox_6
        self.setup_toggle_behavior(
            self.ui.comboBox_6,
            show_on_yes = [
                self.ui.label_41, self.ui.label_42, self.ui.lineEdit_20, self.ui.toolButton_44,
                self.ui.label_43, self.ui.label_44, self.ui.lineEdit_21, self.ui.toolButton_45,
                self.ui.label_73, self.ui.comboBox_16, self.ui.toolButton_59
            ],
            show_on_no = [
                self.ui.label_45, self.ui.label_46, self.ui.lineEdit_28, self.ui.toolButton_46
            ]
        )

        # Intercept show and hide events of comboBox_16 to show or hide widgets
        self.ui.comboBox_16.installEventFilter(self)
        
        # Validate Symmetrical Ground Fault Current inputs 
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_20,
            error_label=self.ui.label_97,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Fault Current Division Factor inputs 
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_21,
            error_label=self.ui.label_98,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Maximum Grid Current inputs 
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_28,
            error_label=self.ui.label_99,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

    def extractParametersFromGui(self):
        def safe_float(text, default=0.0):
            try:
                return float(text)
            except (ValueError, TypeError):
                return default
        return {
            "calcMaxGridCurrent": str(self.ui.comboBox_6.currentIndex()),
            "faultCurrent": safe_float(self.ui.lineEdit_20.text()),
            "faultDivisionFactor": safe_float(self.ui.lineEdit_21.text()),
            "maxGridCurrent": safe_float(self.ui.lineEdit_28.text())
        }
    
    def resetParameters(self):
        self.ui.comboBox_6.setCurrentIndex(0)
        self.ui.lineEdit_20.setText("")
        self.ui.lineEdit_21.setText("")
        self.ui.lineEdit_28.setText("")