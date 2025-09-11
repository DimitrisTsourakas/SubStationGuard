from .BaseController import BaseController
from . import Validation as validation

class SafetyStandardController(BaseController):
    def __init__(self, parent):

        super().__init__(parent)
        
        self.ui = parent.ui

        self.parent = parent

        # =========================================================================================
        # Safety Standard
        # =========================================================================================

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

        # =========================================================================================
        # Setup Buttons for parameters extended information
        # =========================================================================================

        # Info Button - Safety Standard
        self.ui.toolButton_50.clicked.connect(
            lambda: self.showParameterInfo(
                "Safety Standard",
                "<b>Description:</b> Standard applied for safety criteria in substation grounding "
                "design.<br>"
                "<b>Options:</b>"
                "<div style='margin-left:20px'><b>IEEE Std 80:</b> Guide for Safety in AC "
                "Substation Grounding (focus on step and touch voltage criteria, mainly applied "
                "in North America).</div>"
                "<div style='margin-left:20px'><b>CENELEC EN 50522:</b> Earthing of Power "
                "Installations Exceeding 1 kV AC (European standard emphasizing soil resistivity "
                "measurement and design rules).</div>"
                "<b>Symbol:</b> safetyStandard<br>"
                "<b>Values:</b> 0 (IEEE), 1 (CENELEC)<br>"
                "<b>Unit:</b> N/A"
            )
        )

        # Info Button - Body Resistance
        self.ui.toolButton_51.clicked.connect(
            lambda: self.showParameterInfo(
                "Body Resistance (Rb)",
                "<b>Description:</b> Human body resistance between contact points, depends on skin "
                "condition.<br>"
                "<b>Symbol:</b> Rb<br>"
                "<b>Range:</b> 500–1,000 Ω (dry), lower if wet<br>"
                "<b>Unit:</b> Ω"
            )
        )

        # Info Button - Energy Factor
        self.ui.toolButton_52.clicked.connect(
            lambda: self.showParameterInfo(
                "Energy Factor (k)",
                "<b>Description:</b> Factor related to tolerable shock energy based on IEEE/CENELEC "
                "standards.<br>"
                "<b>Symbol:</b> k<br>"
                "<b>Range:</b> ~0.116–0.157 As½ (IEEE values)<br>"
                "<b>Unit:</b> As½"
            )
        )

        # Info Button - Body Current Limit
        self.ui.toolButton_53.clicked.connect(
            lambda: self.showParameterInfo(
                "Body Current Limit (IB)",
                "<b>Description:</b> Threshold current through the human body considered "
                "tolerable.<br>"
                "<b>Symbol:</b> IB<br>"
                "<b>Range:</b> ~0.5–5 A (depends on standards)<br>"
                "<b>Unit:</b> A"
            )
        )

        # Info Button - Body Impedance
        self.ui.toolButton_54.clicked.connect(
            lambda: self.showParameterInfo(
                "Body Impedance (ZT)",
                "<b>Description:</b> Equivalent impedance of the human body for shock "
                "calculations.<br>"
                "<b>Symbol:</b> ZT<br>"
                "<b>Range:</b> 500–1,000 Ω (typical)<br>"
                "<b>Unit:</b> Ω"
            )
        )

        # Info Button - Heart Factor
        self.ui.toolButton_55.clicked.connect(
            lambda: self.showParameterInfo(
                "Heart Factor (HF)",
                "<b>Description:</b> Factor considering current path through the heart.<br>"
                "<b>Symbol:</b> HF<br>"
                "<b>Range:</b> 0–1 p.u.<br>"
                "<b>Unit:</b> p.u."
            )
        )

        # Info Button - Body Factor
        self.ui.toolButton_56.clicked.connect(
            lambda: self.showParameterInfo(
                "Body Factor (BF)",
                "<b>Description:</b> Factor considering body contact area and distribution.<br>"
                "<b>Symbol:</b> BF<br>"
                "<b>Range:</b> 0–1 p.u.<br>"
                "<b>Unit:</b> p.u."
            )
        )

        # Info Button - Constant F
        self.ui.toolButton_57.clicked.connect(
            lambda: self.showParameterInfo(
                "Constant F",
                "<b>Description:</b> Safety standard constant used in CENELEC EN 50522.<br>"
                "<b>Symbol:</b> F<br>"
                "<b>Range:</b> 0–1 p.u.<br>"
                "<b>Unit:</b> p.u."
            )
        )

        # Info Button - Voltage Limit
        self.ui.toolButton_58.clicked.connect(
            lambda: self.showParameterInfo(
                "Voltage Limit (Vlim)",
                "<b>Description:</b> Maximum permissible touch voltage according to standard.<br>"
                "<b>Symbol:</b> Vlim<br>"
                "<b>Range:</b> 50–430 V (depends on fault duration and standard)<br>"
                "<b>Unit:</b> V"
            )
        )


        # =========================================================================================
        # Validation of input Parameters
        # =========================================================================================

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
    
    def extractParametersFromGui(self):
        def safe_float(text, default=0.0):
            try:
                return float(text)
            except (ValueError, TypeError):
                return default
        def safe_str(text, default=""):
            return text if text is not None else default
        return {
            "safetyStandard": safe_str(self.ui.comboBox_8.currentIndex()),
            "bodyResistance": safe_float(self.ui.lineEdit_13.text()),
            "energyFactor": safe_float(self.ui.lineEdit_14.text()),
            "bodyCurrentLimit": safe_float(self.ui.lineEdit_24.text()),
            "bodyImpedance": safe_float(self.ui.lineEdit_25.text()),
            "heartFactor": safe_float(self.ui.lineEdit_26.text()),
            "bodyFactor": safe_float(self.ui.lineEdit_29.text()),
            "constantF": safe_float(self.ui.lineEdit_30.text()),
            "voltageLimit": safe_float(self.ui.lineEdit_31.text())
        }
    
    def resetParameters(self):
        self.ui.comboBox_8.setCurrentIndex(0)
        self.ui.lineEdit_13.setText("")
        self.ui.lineEdit_14.setText("")
        self.ui.lineEdit_24.setText("")
        self.ui.lineEdit_25.setText("")
        self.ui.lineEdit_26.setText("")
        self.ui.lineEdit_29.setText("")
        self.ui.lineEdit_30.setText("")
        self.ui.lineEdit_31.setText("")