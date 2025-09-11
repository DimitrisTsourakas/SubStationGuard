from .BaseController import BaseController
from .SystemTypeController import SystemTypeController
from .GridCurrentController import GridCurrentController
from .SoilResistivityController import SoilResistivityController
from .SafetyStandardController import SafetyStandardController
from .DecrementFactorController import DecrementFactorController
from data.SeparationDistanceData import SeparationDistanceData
from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor
from PySide6.QtWidgets import QFileDialog, QMessageBox
from evaluators.SeparationDistanceEvaluator import SeparationDistanceEvaluator
from dataclasses import asdict
import json
import webbrowser

class SeparationDistanceController(BaseController):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = parent.ui
        self.parent = parent
        self.systemTypeController = SystemTypeController(parent)
        self.soilResistivityController = SoilResistivityController(parent)
        self.gridCurrentController = GridCurrentController(parent)
        self.safetyStandardController = SafetyStandardController(parent)
        self.decrementalFactorController = DecrementFactorController(parent)
        self.ui.evaluateButton.clicked.connect(self.evaluateAndPlot)
        self.ui.resetButton.clicked.connect(self.resetAllParameters)
        self.ui.actionShow_Parameters.toggled.connect(self.ui.tabWidget.setVisible)
        self.ui.actionShow_Logs.toggled.connect(self.ui.tabWidget_2.setVisible)
        self.ui.actionShow_Plot.toggled.connect(self.ui.graphicsView.setVisible)
        self.ui.actionImport_Parameters.triggered.connect(self.importParameters)
        self.ui.actionExport_Parameters.triggered.connect(self.exportParameters)
        self.ui.actionDocumentation.triggered.connect(self.openDocumentation)

    def extractAllParameters(self) -> SeparationDistanceData:
        params = {
            **self.systemTypeController.extractParametersFromGui(),
            **self.soilResistivityController.extractParametersFromGui(),
            **self.gridCurrentController.extractParametersFromGui(),
            **self.safetyStandardController.extractParametersFromGui(),
            **self.decrementalFactorController.extractParametersFromGui()
        }
        return SeparationDistanceData(**params)
    
    def resetAllParameters(self):
        self.systemTypeController.resetParameters()
        self.soilResistivityController.resetParameters()
        self.gridCurrentController.resetParameters()
        self.safetyStandardController.resetParameters()
        self.decrementalFactorController.resetParameters()
        self.ui.graphicsView.clear()

    def evaluateAndPlot(self):
        data = self.extractAllParameters()
        evaluator = SeparationDistanceEvaluator(logFunc=self.logToGui)
        evaluator.plotCreation(data, self.ui.graphicsView)

    def logToGui(self, message: str):
        cursor = self.ui.plainTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        fmt = QTextCharFormat()
        # Set color based on log level
        if message.startswith("<E"):  # Error
            fmt.setForeground(QColor("red"))
        elif message.startswith("<W"):  # Warning
            fmt.setForeground(QColor("orange"))
        else:  # Info
            fmt.setForeground(QColor("black"))
        # Insert the text with the chosen format
        cursor.insertText(message + "\n", fmt)

        # Auto scroll to the bottom
        self.ui.plainTextEdit.setTextCursor(cursor)
        self.ui.plainTextEdit.ensureCursorVisible()

    def importParameters(self):
        path, _ = QFileDialog.getOpenFileName(self.parent, "Import Parameters", "", "JSON Files (*.json)")
        if not path:
            return
        try:
            with open(path, "r") as f:
                data = json.load(f)
            self.loadParameters(data)
            QMessageBox.information(self.parent, "Import", "Parameters imported successfully.")
        except Exception as e:
            QMessageBox.critical(self.parent, "Import Error", str(e))

    def exportParameters(self):
        path, _ = QFileDialog.getSaveFileName(self.parent, "Export Parameters", "", "JSON Files (*.json)")
        if not path:
            return
        try:
            data = asdict(self.extractAllParameters())
            with open(path, "w") as f:
                json.dump(data, f, indent=3)
            QMessageBox.information(self.parent, "Export", "Parameters exported successfully.")
        except Exception as e:
            QMessageBox.critical(self.parent, "Export Error", str(e))

    def loadParameters(self, data):
        # Basic config
        self.ui.comboBox_9.setCurrentIndex(self.ui.comboBox_9.findText(str(data.get("systemType", "TN"))))  # "TN" or "TT"
        self.ui.comboBox_8.setCurrentIndex(int(data.get("safetyStandard", 0)))                              # "0" (IEEE) or "1" (CENELEC)
        self.ui.comboBox_7.setCurrentIndex(int(data.get("calcSoilResistivity", 0)))                         # "0" (Calculate Soil Resistivity) "1" (Do not calculate Soil Resistivity)
        self.ui.comboBox_6.setCurrentIndex(int(data.get("calcMaxGridCurrent", 0)))                          # "0" (Calculate Maximum Gid Current) "1" (Do not calculate Maximum Gid Current)
        self.ui.comboBox_16.setCurrentIndex(int(data.get("calcDecrementFactor", 0)))                        # "0" (Calculate Decrement Factor) "1" (Do not calculate Decrement Factor)
        self.ui.comboBox_10.setCurrentIndex(int(data.get("surfacePotentialFuncOption", 0)))                 # "0" (Data Points from CSV File) "1" (Custom Mathematical Expression)

        # Electrical parameters
        self.ui.lineEdit_32.setText(str(data.get("geometricFactor", "")))             # kg (m^-1)
        self.ui.lineEdit_23.setText(str(data.get("soilResistivity", "")))             # ρ (Ωm)
        self.ui.lineEdit_22.setText(str(data.get("groundResistance", "")))            # Rg (Ω)

        self.ui.lineEdit_20.setText(str(data.get("faultCurrent", "")))                # If (A)
        self.ui.lineEdit_38.setText(str(data.get("decrementFactor", "")))             # Df (p.u.)
        self.ui.lineEdit_21.setText(str(data.get("faultDivisionFactor", "")))         # Sf (p.u.)
        self.ui.lineEdit_45.setText(str(data.get("inductiveReactance", "")))          # X (Ω)
        self.ui.lineEdit_46.setText(str(data.get("resistanceAtFault", "")))           # R (Ω)
        self.ui.lineEdit_34.setText(str(data.get("faultDuration", "")))               # tf (s)

        # Human factors
        self.ui.lineEdit_13.setText(str(data.get("bodyResistance", "")))              # Rb (Ω)
        self.ui.lineEdit_14.setText(str(data.get("energyFactor", "")))                # k (As^0.5)
        self.ui.lineEdit_24.setText(str(data.get("bodyCurrentLimit", "")))            # IB (A)
        self.ui.lineEdit_25.setText(str(data.get("bodyImpedance", "")))               # ZT (Ω)
        self.ui.lineEdit_26.setText(str(data.get("heartFactor", "")))                 # HF (p.u.)
        self.ui.lineEdit_29.setText(str(data.get("bodyFactor", "")))                  # BF (p.u.)
        self.ui.lineEdit_30.setText(str(data.get("constantF", "")))                   # F (p.u.)
        self.ui.lineEdit_31.setText(str(data.get("voltageLimit", "")))                # Vlim (V)

        # Functional
        if str(data.get("surfacePotentialFuncOption", "0")) == "0":
            self.ui.lineEdit_35.setText(str(data.get("surfacePotentialFunc", "")))     # ksp(x) (function)
        else:
            self.ui.lineEdit_33.setText(str(data.get("surfacePotentialFunc", "")))     # ksp(x) (function)

        # Results (optional)
        self.ui.lineEdit_28.setText(str(data.get("maxGridCurrent", "")))              # IG (A)\
        

    def openDocumentation(self):
        """Open the online documentation (GitHub README)."""
        url = "https://github.com/DimitrisTsourakas/Safety-performance-evaluation-of-typical-grounding-configurations-of-MV-LV-distributionsubstations/blob/main/README.md"
        webbrowser.open(url)