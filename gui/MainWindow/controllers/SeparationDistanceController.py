from .BaseController import BaseController
from .SystemTypeController import SystemTypeController
from .GridCurrentController import GridCurrentController
from .SoilResistivityController import SoilResistivityController
from .SafetyStandardController import SafetyStandardController
from .DecrementFactorController import DecrementFactorController
from data.SeparationDistanceData import SeparationDistanceData
from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor
from evaluators.SeparationDistanceEvaluator import SeparationDistanceEvaluator

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