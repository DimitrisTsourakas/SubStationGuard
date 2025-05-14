from .BaseController import BaseController
from . import Validation as validation

class SoilResistivityController(BaseController):
    def __init__(self, parent):

        super().__init__(parent)
        
        self.ui = parent.ui

        self.parent = parent

        # Calculate Soil Resistivity through Ground Resistance

        # Make error labels invisible
        self.ui.label_60.setVisible(False)
        self.ui.label_61.setVisible(False)

        # Show options based on comboBox_7
        self.setup_toggle_behavior(
            self.ui.comboBox_7,
            show_on_yes = [
                self.ui.label_48, self.ui.label_49, self.ui.lineEdit_22, self.ui.toolButton_48
            ],
            show_on_no = [
                self.ui.label_51, self.ui.label_52, self.ui.lineEdit_23, self.ui.toolButton_49
            ]
        )

        # Validate Soil Resistivity inputs 
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_23,
            error_label=self.ui.label_60,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )
        
        # Validate Ground Resistance inputs 
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_22,
            error_label=self.ui.label_61,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )