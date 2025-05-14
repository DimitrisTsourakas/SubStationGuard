from .BaseController import BaseController
from . import Validation as validation

class SafetyStandardController(BaseController):
    def __init__(self, parent):

        super().__init__(parent)
        
        self.ui = parent.ui

        self.parent = parent

        # Safety Standard

        # Make error labels invisible
        self.ui.label_89.setVisible(False)
        self.ui.label_90.setVisible(False)
        self.ui.label_91.setVisible(False)
        self.ui.label_92.setVisible(False)
        self.ui.label_93.setVisible(False)
        self.ui.label_94.setVisible(False)
        self.ui.label_95.setVisible(False)
        self.ui.label_96.setVisible(False)

        # Show options based on comboBox_8
        self.setup_toggle_behavior(
            self.ui.comboBox_8,
            show_on_yes = [
                self.ui.label_54, self.ui.label_55, self.ui.lineEdit_13, self.ui.toolButton_51,
                self.ui.label_56, self.ui.label_57, self.ui.lineEdit_14, self.ui.toolButton_52
            ],
            show_on_no = [
                self.ui.label_58, self.ui.label_59, self.ui.lineEdit_24, self.ui.toolButton_53,
                self.ui.label_63, self.ui.label_64, self.ui.lineEdit_25, self.ui.toolButton_54,
                self.ui.label_65, self.ui.label_66, self.ui.lineEdit_26, self.ui.toolButton_55,
                self.ui.label_67, self.ui.label_68, self.ui.lineEdit_29, self.ui.toolButton_56,
                self.ui.label_69, self.ui.label_70, self.ui.lineEdit_30, self.ui.toolButton_57,
                self.ui.label_71, self.ui.label_72, self.ui.lineEdit_31, self.ui.toolButton_58
            ]
        )

        # Setup Safety Standard based on System Type of MV/LV Substation
        self.ui.comboBox_9.currentTextChanged.connect(self.update_safety_standard_options)
        
        # Validate Resistance of the human body inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_13,
            error_label=self.ui.label_96,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Factor related to tolerable electric shock energy inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_14,
            error_label=self.ui.label_95,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Body current limit inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_24,
            error_label=self.ui.label_94,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Body impedance inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_25,
            error_label=self.ui.label_93,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Heart current factor inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_26,
            error_label=self.ui.label_92,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Body factor inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_29,
            error_label=self.ui.label_91,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Constant F inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_30,
            error_label=self.ui.label_90,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )
        
        # Validate Voltage limit inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_31,
            error_label=self.ui.label_89,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

    def update_safety_standard_options(self, system_type):
        """ Function that updates safety standard combo box based on the selected system type, TN or TT

        Arguments:
            system_type (string): System Type of MV/LV Substation (TN or TT)
        """
        if system_type == "TT":
            self.enable_combo_item(self.ui.comboBox_8, 0, False)
            self.enable_combo_item(self.ui.comboBox_8, 1, True)
            self.ui.comboBox_8.setCurrentIndex(1)
        elif system_type == "TN":
            self.enable_combo_item(self.ui.comboBox_8, 0, True)
            self.enable_combo_item(self.ui.comboBox_8, 1, True)