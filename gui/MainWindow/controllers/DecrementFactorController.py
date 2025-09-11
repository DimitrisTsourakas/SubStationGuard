from .BaseController import BaseController
from . import Validation as validation

class DecrementFactorController(BaseController):
    def __init__(self, parent):

        super().__init__(parent)
        
        self.ui = parent.ui

        self.parent = parent

        # =========================================================================================
        # Calculate Decrement Factor according to IEEE Std 80
        # =========================================================================================

        # Make error labels invisible
        self.ui.label_62.setVisible(False)
        self.ui.label_87.setVisible(False)
        self.ui.label_88.setVisible(False)

        # Show options based on comboBox_16
        self.setup_toggle_behavior(
            self.ui.comboBox_16,
            show_on_yes = [
                self.ui.label_74, self.ui.label_75, self.ui.lineEdit_45, self.ui.toolButton_60,
                self.ui.label_76, self.ui.label_77, self.ui.lineEdit_46, self.ui.toolButton_61
            ],
            show_on_no = [
                self.ui.label_78, self.ui.label_79, self.ui.lineEdit_38, self.ui.toolButton_62
            ]
        )

        # =========================================================================================
        # Setup Buttons for parameters extended information
        # =========================================================================================
        
        # Info Button - Calculate Decrement Factor according to IEEE Std 80
        self.ui.toolButton_59.clicked.connect(
        lambda: self.showParameterInfo(
            "Calculation options of Decrement Factor",
            "<b>Description:</b> Determines the way Decrement Factor is calculated.<br>"
            "<b>Options:</b>"
            "<div style='margin-left:20px'><b>Option 1:</b> Calculate the Decrement Factor (Df) "
            "considering the ratio of Inductive Reactance (X) with System Resistance at fault (R) "
            "and the Fault duration (tf) using the following calculation algorithm:<br>"
            "<pre>Ta = X / (2 · π · 60 · R)</pre>"
            "<pre>Df = √(1 + (Ta/tf) · (1 - exp(-2 · tf / Ta)))</pre><br></div>"
            "<div style='margin-left:20px'><b>Option 2:</b> Directly provide a user-defined "
            "Decrement Factor (Df) in p.u.</div>"
            )
        )

        # Info Button - Inductive Reactance
        self.ui.toolButton_60.clicked.connect(
        lambda: self.showParameterInfo(
            "Inductive Reactance (X)",
            "<b>Description:</b> The Inductive Reactance at the fault location in Ω.<br>"
            "Used to calculate the Decrement Factor accounting for the dc offset of the fault "
            "current.<br>"
            "<b>Symbol:</b> X<br>"
            "<b>Range:</b> Depends on line; typically 0.1-10 Ω<br>"
            "<b>Unit:</b> Ω"
            )
        )

        # Info Button - System Resistance at fault
        self.ui.toolButton_61.clicked.connect(
        lambda: self.showParameterInfo(
            "System Resistance at fault (R)",
            "<b>Description:</b> The System Resistance at the fault location in Ω.<br>"
            "Used to calculate the Decrement Factor accounting for the dc offset of the fault "
            "current.<br>"
            "<b>Symbol:</b> R<br>"
            "<b>Range:</b> Depends on line; typically 0.1-10 Ω<br>"
            "<b>Unit:</b> Ω"
            )
        )

        # Info Button - Decrement Factor
        self.ui.toolButton_62.clicked.connect(
        lambda: self.showParameterInfo(
            "Decrement Factor (p.u.)",
            "<b>Description:</b> Factor that accounts for asymmetrical fault current's dc offset"
            "and decay.<br>"
            "<b>Symbol:</b> Df<br>"
            "<b>Range:</b> typically 0.8-1.0 p.u.<br>"
            "<b>Unit:</b> p.u."
            )
        )
        
        # =========================================================================================
        # Validation of input Parameters
        # =========================================================================================

        # Validate Inductive Reactance inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_45,
            error_label=self.ui.label_88,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate System resistance at fault inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_46,
            error_label=self.ui.label_87,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Decrement Factor inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_38,
            error_label=self.ui.label_62,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

    def extractParametersFromGui(self):
        def safe_float(text, default=0.0):
            try:
                return float(text)
            except (ValueError, TypeError):
                return default
        def safe_str(text, default=""):
            return text if text is not None else default
        return {
            "calcDecrementFactor": safe_str(self.ui.comboBox_16.currentIndex()),
            "inductiveReactance": safe_float(self.ui.lineEdit_45.text()),
            "resistanceAtFault": safe_float(self.ui.lineEdit_46.text()),
            "decrementFactor": safe_float(self.ui.lineEdit_38.text())
        }

    def resetParameters(self):
        self.ui.comboBox_16.setCurrentIndex(0)
        self.ui.lineEdit_45.setText("")
        self.ui.lineEdit_46.setText("")
        self.ui.lineEdit_38.setText("")