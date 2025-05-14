from .BaseController import BaseController
from . import Validation as validation

class SystemTyperController(BaseController):
    def __init__(self, parent):

        super().__init__(parent)
        
        self.ui = parent.ui

        self.parent = parent

        # System Type of MV/LV Substation

        # Make error labels invisible
        self.ui.label_100.setVisible(False)
        self.ui.label_101.setVisible(False)
        self.ui.label_102.setVisible(False)
        
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