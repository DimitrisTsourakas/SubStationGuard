from data.SeparationDistanceData import SeparationDistanceData
from .BaseEvaluator import BaseEvaluator

import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import ast
from scipy.optimize import root_scalar
from scipy.interpolate import interp1d
from typing import Callable

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView

class SurfacePotentialError(Exception):
    pass
class SeparationDistanceEvaluator(BaseEvaluator):
    def __init__(self, logFunc=None):
        super().__init__(logFunc)

    def maxGridCurrent(self, If: float, Df: float, Sf: float) -> float:
        """ Calculates the maximum grid current (IG) considering symmetrical ground fault current (If),
        decrement factor accounting for the dc offset of the fault current (Df) and fault current 
        division factor, which considers fault current return paths additional to the ground (Sf).
        Formula: IG = If * Df * Sf

        Arguments:
            If (real): Symmetrical ground fault current (A)
            Df (real): Decrement factor accounting for the dc offset of the fault current (p.u.)
            Sf (real): Fault current division factor, which considers fault current return paths 
                    additional to the ground (p.u.)
        
        Returns:
            IG (real): Maximum grid current (A)
        """
        # Logging before applying formula
        formula = "IG = If * Df * Sf"
        self.logInfo(f"Starting calculation of {formula}")
        self.logInfo("Inputs before calculation:")
        self.logInfo(f"   If: {If}A")
        self.logInfo(f"   Df: {Df}p.u.")
        self.logInfo(f"   Sf: {Sf}p.u.")

        # Apply formula
        IG = If * Df * Sf

        # Logging after applying formula
        self.logInfo("Output after calculation:")
        self.logInfo(f"   IG: {IG}A")
        self.logInfo(f"Calculation of {formula} finished successfully")

        return IG

    def maxAllowM2MTouchVoltLimit(self, ts: float, k: float, Rb: float) -> float:
        """ Calucates the maximum allowable metal-to-metal touch voltage limit (EmmTouch) considering
        duration of the electric shock current (ts), a factor related to tolerable electric shock 
        energy (k) taking values of 0.116 and 0.157 As^0.5 for people weighing 50 kg and 70 kg, 
        respectively and resistance of the human body (Rb).
        Formula: EmmTouch = Rb * k / √ts

        Arguments:
            ts (real): Duration of the electric shock current (s)
            k (real): Factor related to tolerable electric shock energy (As^0.5)
            Rb (real): Resistance of the human body (Ω)
        
        Returns:
            EmmTouch (real): Maximum allowable metal-to-metal touch voltage limit (V)
        """
        # Logging before applying formula
        formula = "EmmTouch = Rb * k / √ts"
        self.logInfo(f"Starting calculation of {formula}")
        self.logInfo("Inputs before calculation:")
        self.logInfo(f"   Rb: {Rb}Ω")
        self.logInfo(f"   k: {k}As^0.5")
        self.logInfo(f"   ts: {ts}s")

        # Apply formula 
        EmmTouch = Rb * k / pow(ts, 0.5)

        # Logging after applying formula
        self.logInfo("Output after calculation:")
        self.logInfo(f"   EmmTouch: {EmmTouch}V")
        self.logInfo(f"Calculation of {formula} finished successfully")

        return EmmTouch

    def groundPotentialRise(self, IG: float, kg: float, ρ: float) -> float:
        """ Calculates the ground potential rise (GPR) considering maximum grid current (IG), geometric
        proportionality factor, accounting for the effect of grounding system geometry on ground 
        resistance Rg (kg) and soil resistivity (ρ)
        Formula: GPR = IG * kg * ρ
        
        Arguments:
            IG (real): Maximum grid current (A)
            kg (real): Geometric proportionality factor (m^-1)
            ρ (real): Soil resistivity (Ωm)
        
        Returns:
            GPR (real): Ground potential rise (V)
        """
        # Logging before applying formula
        formula = "GPR = IG * kg * ρ"
        self.logInfo(f"Starting calculation of {formula}")
        self.logInfo("Inputs before calculation:")
        self.logInfo(f"   IG: {IG}A")
        self.logInfo(f"   kg: {kg}m^-1")
        self.logInfo(f"   ρ: {ρ}Ωm")

        # Apply formula
        GPR = IG * kg * ρ

        # Logging after applying formula
        self.logInfo("Output after calculation:")
        self.logInfo(f"   GPR: {GPR}V")
        self.logInfo(f"Calculation of {formula} finished successfully")

        return GPR

    def inverseFunc(self, function: Callable[[float], float], value: float) -> float:
        """ Define a function that returns the root of f(x) - value = 0

        Arguments: 
            function (lambda function): function to be inversed
            value (real): value at which to evaluate the inverse
        
        Returns: 
            Inversed value (real) 
        """
        # Check if function came from CSV interpolation
        if getattr(function, "_is_interpolated", False):
            xs, ys = function._xs, function._ys

            if not (min(ys) <= value <= max(ys)):
                raise ValueError(f"Value {value} outside interpolated ksp(x) range [{min(ys)}, {max(ys)}]")
            inverse_interp = interp1d(ys, xs, fill_value="extrapolate", bounds_error=False)
            return float(inverse_interp(value))

        # Otherwise use root_scalar for user-defined formula
        def f(x): return function(x) - value
        a, b = 0.01, 10000

        # Precheck: is there a root in bracket?
        if f(a) * f(b) > 0:
            raise ValueError(f"No root: f({a})={f(a):.4f}, f({b})={f(b):.4f} have same sign.")
        
        result = root_scalar(f, bracket=[a, b], method='brentq')
        if not result.converged:
            raise RuntimeError("Root-finding did not converge.")
        return result.root

    def criticalSeparationDistance(self, systemType: str, safetyStandard: int, GPR: float, Rb: float,
                                     k: float, ts: float, ksp: Callable[[float], float], IB: float,
                                     ZT: float, HF: float, BF: float, F: float, Vlim: float) -> float:
        """ Calculates the critical separation distance considering the inverse function of surface 
        potential proportionality factor, ground potential rise (GPR) and max allowable touch 
        voltage (V). Maximum voltage is calculated according to the type of the System and the 
        Safety Standard applied. 
        Formula: xcr = ksp-1(V / GPR)

        Arguments:
            systemType (string): System Type of MV/LV substation
            safetyStandard (string): Safety Standard applied
            GPR (real): Ground potential rise (A m^-1 Ω)
            Rb (real): Resistance of the human body (Ω)
            k (real): Factor related to tolerable electric shock energy (As^0.5)
            ts (real): Duration of the electric shock current (s)
            Rb (real): Resistance of the human body (Ω)
            IB (real): Body current limit (A)
            ZT (real): Body impedance (Ω)
            HF (real): Heart current factor (p.u.)
            BF (real): Body factor (p.u.)
            F (real): Constant F (p.u.) 
            Vlim (real): Voltage limit (V)
            ksp(x) (function in terms of x): surface potential proportionality factor expressed as a
                    function of separation distance, x (m), accounting for the effect of grounding 
                    system geometry on Vsp
        
        Returns:
            xcr (real): Critical Separation Distance (m)
        """

        self.startLog()
        # Critical Seperation Distance Evaluation for System Type "TN" and Safety Standard "IEEE Std 80"
        if systemType == "TN" and safetyStandard == 0:
            # Calculate the maximum allowable metal-to-metal touch voltage limit
            EmmTouch = self.maxAllowM2MTouchVoltLimit(ts, k, Rb)

            # Logging before applying formula
            formula = "xcr = ksp-1(EmmTouch / GPR)"
            self.logInfo(f"Starting calculation of {formula}")
            self.logInfo("Inputs before calculation:")
            self.logInfo(f"   EmmTouch: {EmmTouch}V")
            self.logInfo(f"   GPR: {GPR}V")
            
            # Apply Formula 
            x_critical = self.inverseFunc(ksp, EmmTouch / GPR)
        
        # Critical Seperation Distance Evaluation for System Type "TN" and Safety Standard "CENELEC EN 50522"
        elif systemType == "TN" and safetyStandard == 1:
            # Calculate the the allowable touch Voltage
            UTp = self.allowableTouchVoltage(IB, ZT, HF, BF)
            
            # Logging before applying formula
            formula = "xcr = ksp-1(UTp * F / GPR)"
            self.logInfo(f"Starting calculation of {formula}")
            self.logInfo("Inputs before calculation:")
            self.logInfo(f"   UTp: {UTp}V")
            self.logInfo(f"   F: {F}")
            self.logInfo(f"   GPR: {GPR}V")

            # Apply Formula
            x_critical = self.inverseFunc(ksp, UTp * F / GPR)

        # Critical Seperation Distance Evaluation for System Type "TT" and Safety Standard "CENELEC EN 50522"
        else:
            # Logging before applying formula
            formula = "xcr = ksp-1(Vlim / GPR)"
            self.logInfo(f"Starting calculation of {formula}")
            self.logInfo("Inputs before calculation:")
            self.logInfo(f"   Vlim: {Vlim}V")
            self.logInfo(f"   GPR: {GPR}V")

            # Apply Formula
            x_critical = self.inverseFunc(ksp, Vlim / GPR)

        # Logging after applying formula
        self.logInfo("Output after calculation:")
        self.logInfo(f"   x_critical: {x_critical}m")
        self.logInfo(f"Calculation of {formula} finished successfully")

        self.closeLog()

        return x_critical

    def allowableTouchVoltage(self, IB: float, ZT: float, HF: float, BF: float) -> float:
        """ Calculates the allowable touch Voltage considering the body current limit (IB), the body
        impedance (ZT), the heart current factor (HF) and the body factor (BF)
        Formula: UTp = IB * ZT * BF / HF

        Arguments: 
            IB (real): body current limit (A)
            ZT (real): body impedance (Ω)
            HF (real): heart current factor (p.u.)
            BF (real): body factor (p.u.)  

        Returns:
            UTp (real): Allowable Touch Voltage (V)
        """
        # Logging before applying formula
        formula = "UTp = IB * ZT * BF / HF"
        self.logInfo(f"Starting calculation of {formula}")
        self.logInfo("Inputs before calculation:")
        self.logInfo(f"   IB: {IB}A")
        self.logInfo(f"   ZT: {ZT}Ω")
        self.logInfo(f"   BF: {BF}p.u.")
        self.logInfo(f"   HF: {HF}p.u.")

        # Apply formula
        UTp = IB * ZT * BF / HF
        
        # Logging after applying formula
        self.logInfo("Output after calculation:")
        self.logInfo(f"   UTp: {UTp}V")
        self.logInfo(f"Calculation of {formula} finished successfully")

        return UTp

    def soilResistivity(self, Rg: float, kg: float) -> float:
        """ Calculates the soil Resistivity considering the ground Resistance (Rg) and the Geometric
        proportionality factor (kg)
        Formula: ρ = Rg / kg

        Arguments: 
            Rg (real): Ground Resistance (Ω)
            kg (real): Geometric proportionality factor (m^-1)

        Returns
            ρ (real): Soil resistivity (Ωm)
        """
        # Logging before applying formula
        formula = "ρ = Rg / kg"
        self.logInfo(f"Starting calculation of {formula}")
        self.logInfo("Inputs before calculation:")
        self.logInfo(f"   Rg: {Rg}Ω")
        self.logInfo(f"   kg: {kg}m^-1")
        
        # Apply formula
        ρ = Rg / kg

        # Logging after applying formula
        self.logInfo("Output after calculation:")
        self.logInfo(f"   ρ: {ρ}Ωm")
        self.logInfo(f"Calculation of {formula} finished successfully")

        return ρ

    def decrementFactor(self, X: float, R: float, tf: float) -> float:
        """ Calculates the Decrement Factor accounting for the dc offset of the fault current 
        considering the X/R ratio and the fault duration (tf)
        Formula1: Ta = X / (2 * math.pi * 60 * R)
        Formula2: Df = math.sqrt(1 + (Ta * (1 - math.exp(-2 * tf / Ta))) / tf)

        Arguments: 
            X (real): Inductive reactance (Ω)
            R (real): System resistance at fault (Ω)
            tf (real): Fault duration (s)

        Returns
            Df (real): Decrement Factor (p.u.)
        """
        # Logging before applying formula
        formula1 = "Ta = X / (2 * math.pi * 60 * R)"
        self.logInfo(f"Starting calculation of {formula1}")
        self.logInfo("Inputs before calculation:")
        self.logInfo(f"   X: {X}Ω")
        self.logInfo(f"   R: {R}Ω")

        # Apply formula
        Ta = X / (2 * math.pi * 60 * R)

        # Logging after applying formula
        self.logInfo("Output after calculation:")
        self.logInfo(f"   Ta: {Ta}s")
        self.logInfo(f"Calculation of {formula1} finished successfully")

        # Logging before applying formula
        formula2 = "Df = math.sqrt(1 + (Ta * (1 - math.exp(-2 * tf / Ta))) / tf )"
        self.logInfo(f"Starting calculation of {formula2}")
        self.logInfo("Inputs before calculation:")
        self.logInfo(f"   Ta: {Ta}s")
        self.logInfo(f"   tf: {tf}s")
        
        # Apply formula
        Df = math.sqrt(1 + (Ta * (1 - math.exp(-2 * tf / Ta))) / tf)

        # Logging after applying formula
        self.logInfo("Output after calculation:")
        self.logInfo(f"   Df: {Df}p.u.")
        self.logInfo(f"Calculation of {formula2} finished successfully")

        return Df

    def createSurfacePotentialFunc(self, option: int, source: str) -> Callable[[float], float]:
        """
        option == 0: `source` is path to CSV file with two columns (x, y).
        option == 1: `source` is a math expression in `x` (e.g. "10 + 2*x**0.5").
        Returns f(x) -> y.
        """
        if option == 0:
            # --- CSV path: linear interpolation ---
            try:
                df = pd.read_csv(source, header=None)
            except Exception as e:
                raise SurfacePotentialError(f"Could not read CSV '{source}': {e!s}")

            if df.shape[1] < 2:
                raise SurfacePotentialError("CSV must have at least two columns (x, y).")

            xs = df.iloc[:, 0].to_numpy(dtype=float)
            ys = df.iloc[:, 1].to_numpy(dtype=float)

            # Ensure sorted for numpy.interp
            sort_idx = np.argsort(xs)
            xs, ys = xs[sort_idx], ys[sort_idx]

            def f(x: float) -> float:
                # out‐of‐bounds behavior: extrapolate with endpoint values
                return float(np.interp(x, xs, ys, left=ys[0], right=ys[-1]))
            
            # Set attributes to acknowlegde that function is created by csv provided points
            f._xs = xs
            f._ys = ys
            f._is_interpolated = True
            return f

        elif option == 1:
            # --- Math expression: parse & compile ---
            # Whitelist of safe names: x plus all math.* functions/constants
            safe_names = {"x": None}
            safe_names.update({k: getattr(math, k) for k in dir(math) if not k.startswith("_")})

            # Allowed AST node types
            allowed_nodes = (
                ast.Expression, ast.BinOp, ast.UnaryOp, ast.Call,
                ast.Name, ast.Load, ast.Constant,
                ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
                ast.USub, ast.UAdd,
            )

            node = ast.parse(source, mode="eval")
            for sub in ast.walk(node):
                if not isinstance(sub, allowed_nodes):
                    raise SurfacePotentialError(f"Disallowed syntax: {type(sub).__name__}")
                if isinstance(sub, ast.Name) and sub.id not in safe_names:
                    raise SurfacePotentialError(f"Use of name '{sub.id}' is not allowed")

            code = compile(node, "<surfacePotential>", "eval")
            def f(x: float) -> float:
                try:
                    return eval(code, {"__builtins__": {}}, {**safe_names, "x": x})
                except Exception as e:
                    raise SurfacePotentialError(f"Error evaluating expression at x={x}: {e!s}")

            return f

        else:
            raise SurfacePotentialError("Invalid option; must be 0 (CSV) or 1 (expression).")

    def plotCreation(self, separationDistanceDataObj: SeparationDistanceData, targetView: QGraphicsView):
        """ Main function responsible for the creation of plots. Function will setup plot parameters
        like title, labels etc. according to the curve that is going to be generated. System Type and
        Safety Standard determine the final parameter setup. Additionally, the function evaluates and
        displays in the graph, the case that user defined by selecting a Soil Resistivity value.

        Arguments:
            systemType (string): System Type of MV/LV substation
            safetyStandard (string): Safety Standard applied
            kg (real): Geometric proportionality factor (m^-1)
            ksp(x) (lambda function): surface potential proportionality factor expressed as a function
                    of separation distance, x (m), accounting for the effect of grounding system
                    geometry on Vsp
            Rb (real): Resistance of the human body (Ω)
            k (real): Factor related to tolerable electric shock energy (As^0.5)
            IB (real): Body current limit (A)
            ZT (real): Body impedance (Ω)
            HF (real): Heart current factor (p.u.)
            BF (real): Body factor (p.u.)
            F (real): Constant F (p.u.) 
            Vlim (real): Voltage limit (V)
            ρ (real): Soil Resistivity (Ωm)
            tf (real): Fault Duration (s)
            IG (real): Maximum Grid Current (A)
        """
        # Parse parameters from data object
        systemType = separationDistanceDataObj.systemType
        safetyStandard = int(separationDistanceDataObj.safetyStandard)
        kg = separationDistanceDataObj.geometricFactor
        surfacePotentialFuncOption = int(separationDistanceDataObj.surfacePotentialFuncOption)
        kspSource = separationDistanceDataObj.surfacePotentialFunc
        Rb = separationDistanceDataObj.bodyResistance
        k = separationDistanceDataObj.energyFactor
        IB = separationDistanceDataObj.bodyCurrentLimit
        ZT = separationDistanceDataObj.bodyImpedance
        HF = separationDistanceDataObj.heartFactor
        BF = separationDistanceDataObj.bodyFactor
        F = separationDistanceDataObj.constantF
        Vlim = separationDistanceDataObj.voltageLimit
        tf = separationDistanceDataObj.faultDuration

        self.logInfo(separationDistanceDataObj)
        # Creation of Surface Potential Function
        ksp = self.createSurfacePotentialFunc(surfacePotentialFuncOption, kspSource)
        # Calculation of Soil Resistivity
        calcSoilResistivity = int(separationDistanceDataObj.calcSoilResistivity)
        if calcSoilResistivity == 0:
            Rg = separationDistanceDataObj.groundResistance
            ρ = self.soilResistivity(Rg, kg)
        else:
            ρ = separationDistanceDataObj.soilResistivity
        # Calculation of Maximum Grid Current
        calcMaxGridCurrent = int(separationDistanceDataObj.calcMaxGridCurrent)
        if calcMaxGridCurrent == 0:
            If = separationDistanceDataObj.faultCurrent
            Sf = separationDistanceDataObj.faultDivisionFactor
            # Calculation of Decrement Factor
            calcDecrementFactor = int(separationDistanceDataObj.calcDecrementFactor)
            if calcDecrementFactor == 0:
                X = separationDistanceDataObj.inductiveReactance
                R = separationDistanceDataObj.resistanceAtFault
                Df = self.decrementFactor(X, R, tf)
            else:
                Df = separationDistanceDataObj.decrementFactor
            IG = self.maxGridCurrent(If, Df, Sf)
        else:
            IG = separationDistanceDataObj.maxGridCurrent
        
        # Plot Parameters Setup for System Type "TN" and Safety Standard "IEEE Std 80"
        if systemType == "TN" and safetyStandard == 0:
            yLabel = "IG · √tf · ρ (A s^0.5 Ω m)"
            formulaLabel = "IG · √tf · ρ = Rb k / (ksp(x) · kg)"
            formula = lambda x: Rb * k / (ksp(x) * kg) if x > 0 else 0
        
        # Plot Parameters Setup for System Type "TN" and Safety Standard "CENELEC EN 50522"
        elif systemType == "TN" and safetyStandard == 1:
            yLabel = "IG · ρ / UTp(tf)  (A Ω m / V)"
            formulaLabel = "IG · ρ / UTp(tf) = F / (ksp(x) · kg)"
            formula = lambda x: F / (ksp(x) * kg) if x > 0 else 0

        # Plot Parameters Setup for System Type "TT" and Safety Standard "CENELEC EN 50522"
        else:
            yLabel = "IG · ρ (A Ω m)"
            formulaLabel = "IG · ρ = Vlim / (ksp(x) · kg)"
            formula = lambda x: Vlim / (ksp(x) * kg) if x > 0 else 0

        title = "Critical separation distance between MV/LV substation and LV neutral grounding configurations"
        xLabel = "Separation Distance, x (m)"
        x_values = np.linspace(0, 500, 1000000)
        y_values = [formula(x) for x in x_values]

        figure = Figure(figsize=(8, 6))
        canvas = FigureCanvas(figure)
        plot = figure.add_subplot(111)
        
        # Create the plot
        plot.set_title(title)
        plot.set_xlabel(xLabel)
        plot.set_ylabel(yLabel)
        plot.grid(alpha=.4, linestyle='--')
        plot.plot(x_values, y_values, label=formulaLabel)
        plot.legend()

        # Case to be evaluated and be shown in the Plot
        # Calculate Ground Potential Rise
        GPR = self.groundPotentialRise(IG, kg, ρ)

        # Calcualte Critical Separation Distance
        x_critical = self.criticalSeparationDistance(systemType, safetyStandard, GPR, Rb, k, tf, ksp, IB, ZT, HF, BF, F, Vlim)

        # Set the evaluation point to highlight
        highlight_x = x_critical
        highlight_y = formula(x_critical)

        self.logInfo(f"Point to be highlighted in the Curve: ({highlight_x},{highlight_y})")
        
        # Add vertical and horizontal lines for the x and y axes
        plot.axvline(0, color='black')
        plot.axhline(0, color='black')
        # Add a vertical line at the specified x coordinate
        plot.axvline(highlight_x, color='red', linestyle='--', label='Vertical Line')
        # Add a horizontal line at the specified y coordinate
        plot.axhline(highlight_y, color='red', linestyle='--', label='Horizontal Line')
        # Add a marker for the specified point
        plot.plot(highlight_x, highlight_y, 's', color='red')
        # annotate the line with a label
        plot.annotate(f'ρ = {ρ}', xy=(-3, highlight_y), xytext=(-5, 1.3 * highlight_y), arrowprops=dict(facecolor='black', arrowstyle='->'))
        #plot.show()

        # Render into the QGraphicsView
        scene = QGraphicsScene()
        scene.addWidget(canvas)
        targetView.setScene(scene)
        targetView.show()