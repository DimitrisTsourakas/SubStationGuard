from .BaseController import BaseController
from . import Validation as validation
from PySide6.QtWidgets import QFileDialog

class SystemTypeController(BaseController):
    def __init__(self, parent):

        super().__init__(parent)
        
        self.ui = parent.ui

        self.parent = parent

        # =========================================================================================
        # System Type of MV/LV Substation
        # =========================================================================================

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

        # =========================================================================================
        # Setup Buttons for parameters extended information
        # =========================================================================================

        # Info Button - System Type of MV/LV Substation
        self.ui.toolButton_63.clicked.connect(
            lambda: self.showParameterInfo(
                "System Type of MV/LV Substation",
                "<b>Description:</b> Defines the grounding system type.<br>"
                "<b>Options:</b>"
                "<div style='margin-left:20px'><b>TN:</b> Direct neutral-to-earth connection.</div>"
                "<div style='margin-left:20px'><b>TT:</b> Neutral grounded independently of "
                "consumer installation.</div>"
                "<b>Symbol:</b> systemType<br>"
                "<b>Values:</b> TN or TT<br>"
                "<b>Unit:</b> N/A"
            )
        )
        
        # Info Button - Geometric Proportionality Factor
        self.ui.toolButton_64.clicked.connect(
            lambda: self.showParameterInfo(
                "Geometric Proportionality Factor (kg)",
                "<b>Description:</b> Factor related to grounding system geometry, used in "
                "resistivity and voltage calculations.<br>"
                "<b>Symbol:</b> kg<br>"
                "<b>Range:</b> ~0.1–10 m⁻¹ (depends on geometry)<br>"
                "<b>Unit:</b> m⁻¹"
            )
        )

        # Info Button - Surface Potential Proportionality Function
        self.ui.toolButton_65.clicked.connect(
            lambda: self.showParameterInfo(
                "Surface Potential Proportionality Function (ksp(x))",
                "<b>Description:</b> Function describing the surface potential proportionality "
                "factor as a function of distance x, capturing the effect of geometry.<br>"
                "<b>Options:</b>"
                "<div style='margin-left:20px'><b>Data Points CSV File:</b> Function via a csv "
                "with data points. (Interpolation is used for points that are not included in the "
                "file.</div>"
                "<div style='margin-left:20px'><b>Custom Mathematical Expression:</b> Function via "
                "a customized mathematical expression of x.</div>"
                "<b>Symbol:</b> ksp(x)<br>"
                "<b>Values:</b> CSV points or mathematical expression<br>"
                "<b>Unit:</b> p.u."
            )
        )

        # Info Button - Fault Duration
        self.ui.toolButton_66.clicked.connect(
            lambda: self.showParameterInfo(
                "Fault Duration (tf)",
                "<b>Description:</b> Time duration of fault before clearance.<br>"
                "<b>Symbol:</b> tf<br>"
                "<b>Range:</b> 0.1–10 s (system dependent)<br>"
                "<b>Unit:</b> s"
            )
        )

        # =========================================================================================
        # Validation of input Parameters
        # =========================================================================================

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
            validator_func=validation.is_valid_function,
            error_message="Enter a valid fuction of x"
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
        def safe_str(text, default=""):
            return text if text is not None else default
        option = self.ui.comboBox_10.currentIndex()
        return {
            "systemType": str(self.ui.comboBox_9.currentText()),
            "geometricFactor": safe_float(self.ui.lineEdit_32.text()),
            "surfacePotentialFuncOption": option,
            "surfacePotentialFunc": (
                safe_str(self.ui.lineEdit_33.text())
                if option
                else safe_str(self.ui.lineEdit_35.text())
            ),
            "faultDuration": safe_float(self.ui.lineEdit_34.text()),
        }
    
    def resetParameters(self):
        self.ui.comboBox_9.setCurrentIndex(0)
        self.ui.comboBox_10.setCurrentIndex(0)
        self.ui.lineEdit_32.setText("")
        self.ui.lineEdit_33.setText("")
        self.ui.lineEdit_34.setText("")
        self.ui.lineEdit_35.setText("")