from .BaseController import BaseController
from .SystemTypeController import SystemTypeController
from .GridCurrentController import GridCurrentController
from .SoilResistivityController import SoilResistivityController
from .SafetyStandardController import SafetyStandardController
from .DecrementFactorController import DecrementFactorController
from data.SeparationDistanceData import SeparationDistanceData
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

    def evaluateAndPlot(self):
        data = self.extractAllParameters()
        evaluator = SeparationDistanceEvaluator(logFunc=self.logToGui)
        evaluator.plotCreation(data, self.ui.graphicsView)

    def logToGui(self, message: str):
        self.ui.plainTextEdit.appendPlainText(message)