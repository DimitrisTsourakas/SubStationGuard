import matplotlib.pyplot as plt
import numpy as np
import ast
from scipy.optimize import root_scalar
from datetime import datetime

def startLog():
    """ Function to start a log and display initial information for the execution
    """
    # Pretty Prints
    logInfo("")
    logInfo("")
    logInfo("Separation distance between MV/LV substation and secondary neutral grounding configurations")
    logInfo("")
    logInfo("")

def closeLog():
    """ Function to close a log and display final information for the execution
    """
    # Pretty Prints
    logInfo("Evaluation has finished")
    logInfo("Closing log")

def logInfo(message):
    """ Wrapper function to print Info logs with appended date timestamps

    Arguments: 
        message (string): Message to be printed
    """
    # Get the current datetime
    now = datetime.now()

    # Format the datetime as a string with seconds
    timestamp_str = now.strftime("%Y%b%d %H:%M:%S")

    # Get the milliseconds separately
    millis_str = now.strftime("%f")[:-3]

    # Combine the timestamp and milliseconds strings
    timestamp_with_millis_str = f"{timestamp_str}.{millis_str}"

    # Print the timestamp string with milliseconds
    print(f"<I {timestamp_with_millis_str}> {message}")

def logWarning(message):
    """ Wrapper function to print Warning logs with appended date timestamps

    Arguments: 
        message (string): Message to be printed
    """
    # Get the current datetime
    now = datetime.now()

    # Format the datetime as a string with seconds
    timestamp_str = now.strftime("%Y%b%d %H:%M:%S")

    # Get the milliseconds separately
    millis_str = now.strftime("%f")[:-3]

    # Combine the timestamp and milliseconds strings
    timestamp_with_millis_str = f"{timestamp_str}.{millis_str}"

    # Print the timestamp string with milliseconds
    print(f"<W {timestamp_with_millis_str}: {message}")

def logError(message):
    """ Wrapper function to print Error logs with appended date timestamps

    Arguments: 
        message (string): Message to be printed
    """
    # Get the current datetime
    now = datetime.now()

    # Format the datetime as a string with seconds
    timestamp_str = now.strftime("%Y%b%d %H:%M:%S")

    # Get the milliseconds separately
    millis_str = now.strftime("%f")[:-3]

    # Combine the timestamp and milliseconds strings
    timestamp_with_millis_str = f"{timestamp_str}.{millis_str}"

    # Print the timestamp string with milliseconds
    print(f"<E {timestamp_with_millis_str}: {message}")

def maxGridCurrent(If, Df, Sf):
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
    logInfo(f"Staring calculation of {formula}")
    logInfo("Inputs before calculation:")
    logInfo(f"If: {If}A")
    logInfo(f"Df: {Df}p.u.")
    logInfo(f"Sf: {Sf}p.u.")

    # Apply formula
    IG = If * Df * Sf

    # Logging after applying formula
    logInfo("Output after calculation:")
    logInfo(f"IG: {IG}A")
    logInfo(f"Calculation of {formula} finished successfully")

    return IG

def maxAllowM2MTouchVoltLimit(ts, k, Rb):
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
    logInfo(f"Staring calculation of {formula}")
    logInfo("Inputs before calculation:")
    logInfo(f"Rb: {Rb}Ω")
    logInfo(f"k: {k}As^0.5")
    logInfo(f"ts: {ts}s")

    # Apply formula 
    EmmTouch = Rb * k / pow(ts, 0.5)

    # Logging after applying formula
    logInfo("Output after calculation:")
    logInfo(f"EmmTouch: {EmmTouch}V")
    logInfo(f"Calculation of {formula} finished successfully")

    return EmmTouch

def groundPotentialRise(IG, kg, ρ):
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
    logInfo(f"Staring calculation of {formula}")
    logInfo("Inputs before calculation:")
    logInfo(f"IG: {IG}A")
    logInfo(f"kg: {kg}m^-1")
    logInfo(f"ρ: {ρ}Ωm")

    # Apply formula
    GPR = IG * kg * ρ

    # Logging after applying formula
    logInfo("Output after calculation:")
    logInfo(f"GPR: {GPR}V")
    logInfo(f"Calculation of {formula} finished successfully")

    return GPR

def inverseFunc(function, value):
    """ Define a function that returns the root of f(x) - value = 0

    Arguments: 
        function (lambda function): function to be inversed
        value (real): value at which to evaluate the inverse
    
    Returns: 
        Inversed value (real) 
    """
    return root_scalar(lambda x: function(x) - value, bracket=[0.01, 10000]).root

def criticalSeparationDistance(systemType, safetyStandard, GPR, Rb, k, ts, ksp, IB, ZT, HF, BF, F, Vlim):
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

    # Critical Seperation Distance Evaluation for System Type "TN" and Safety Standard "IEEE Std 80"
    if systemType == "TN" and safetyStandard == "0":
        # Calculate the maximum allowable metal-to-metal touch voltage limit
        EmmTouch = maxAllowM2MTouchVoltLimit(ts, k, Rb)

        # Logging before applying formula
        formula = "ksp-1(EmmTouch / GPR)"
        logInfo(f"Staring calculation of {formula}")
        logInfo("Inputs before calculation:")
        logInfo(f"EmmTouch: {EmmTouch}V")
        logInfo(f"GPR: {GPR}V")
        
        # Apply Formula 
        x_critical = inverseFunc(ksp, EmmTouch / GPR)
    
    # Critical Seperation Distance Evaluation for System Type "TN" and Safety Standard "CENELEC EN 50522"
    elif systemType == "TN" and safetyStandard == "1":
        # Calculate the the allowable touch Voltage
        UTp = allowableTouchVoltage(IB, ZT, HF, BF)
        
        # Logging before applying formula
        formula = "ksp-1(UTp * F / GPR)"
        logInfo(f"Staring calculation of {formula}")
        logInfo("Inputs before calculation:")
        logInfo(f"UTp: {UTp}V")
        logInfo(f"F: {F}")
        logInfo(f"GPR: {GPR}V")

        # Apply Formula
        x_critical = inverseFunc(ksp, UTp * F / GPR)

    # Critical Seperation Distance Evaluation for System Type "TT" and Safety Standard "CENELEC EN 50522"
    else:
        # Logging before applying formula
        formula = "ksp-1(Vlim / GPR)"
        logInfo(f"Staring calculation of {formula}")
        logInfo("Inputs before calculation:")
        logInfo(f"Vlim: {Vlim}V")
        logInfo(f"GPR: {GPR}V")

        # Apply Formula
        x_critical = inverseFunc(ksp, Vlim / GPR)

    # Logging after applying formula
    logInfo("Output after calculation:")
    logInfo(f"x_critical: {x_critical}m")
    logInfo(f"Calculation of {formula} finished successfully")

    return x_critical

def allowableTouchVoltage(IB, ZT, HF, BF):
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
    logInfo(f"Staring calculation of {formula}")
    logInfo("Inputs before calculation:")
    logInfo(f"IB: {IB}A")
    logInfo(f"ZT: {ZT}Ω")
    logInfo(f"BF: {BF}p.u.")
    logInfo(f"HF: {HF}p.u.")

    # Apply formula
    UTp = IB * ZT * BF / HF
    
    # Logging after applying formula
    logInfo("Output after calculation:")
    logInfo(f"UTp: {UTp}V")
    logInfo(f"Calculation of {formula} finished successfully")

    return UTp

def soilResistivity(Rg, kg):
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
    logInfo(f"Staring calculation of {formula}")
    logInfo("Inputs before calculation:")
    logInfo(f"Rg: {Rg}Ω")
    logInfo(f"kg: {kg}m^-1")
    
    # Apply formula
    ρ = Rg / kg

    # Logging after applying formula
    logInfo("Output after calculation:")
    logInfo(f"ρ: {ρ}Ωm")
    logInfo(f"Calculation of {formula} finished successfully")

    return ρ

def decrementFactor(XR, tf):
    """ Calculates the Decrement Factor accounting for the dc offset of the fault current 
    considering the X/R ratio (XR) and the fault duration (tf)
    Formula: Df = XR * tf

    Arguments: 
        XR (real): X/R ratio (s^-1)
        tf (real): Fault duration (s)

    Returns
        Df (real): Decrement Factor (p.u.)
    """
    # Logging before applying formula
    formula = "Df = XR * tf"
    logInfo(f"Staring calculation of {formula}")
    logInfo("Inputs before calculation:")
    logInfo(f"XR: {XR}s^-1")
    logInfo(f"tf: {tf}s")
    
    # Apply formula
    Df = XR * tf

    # Logging after applying formula
    logInfo("Output after calculation:")
    logInfo(f"Df: {Df}p.u.")
    logInfo(f"Calculation of {formula} finished successfully")

    return Df

def systemTypeSelection():
    """ Main Function for the selction of the System Type of MV/LV substation. Two system types can
    be selected, TN or TT.

    Returns:
        systemType (string): System Type of MV/LV substation
    """
    logInfo("PHASE 1: System Type of MV/LV substation")
    logInfo("")

    logInfo("Please Select System Type (TT or TN):")
    systemType = input()
    while systemType not in ["TT", "TN"]:
        logWarning("Invalid option. Please select either option TT or option TN:")
        systemType = input()

    logInfo(f"You selected System Type {systemType}.")

    return systemType

def safetyStandardSelection(systemType):
    """ Main Function for the selction of the Safety Standard. Two Safety Standards can be
    be selected, [0]=IEEE Std 80 or [1]=CENELEC EN 50522.

    Arguments:
        systemType (string): System Type of MV/LV substation

    Returns:
        safetyStandard (string): Safety Standard
    """
    logInfo("")
    logInfo("PHASE 2: Safety Standard")
    logInfo("")

    # Available Safety Standards Names
    safetyStandardNames = ["IEEE Std 80", "CENELEC EN 50522"]

    # Prompt user to choose Safety Standard in case of TN System Type
    if systemType == "TN":
        logInfo("Please Select Safety Standard ([0]=IEEE Std 80 or [1]=CENELEC EN 50522):")
        safetyStandard = input()
        while safetyStandard not in ["0", "1"]:
            logWarning("Invalid option. Please select either 0 for option IEEE Std 80 or 1 for option CENELEC EN 50522:")
            safetyStandard = input()

        logInfo(f"You selected Safety Standard {safetyStandardNames[int(safetyStandard)]}.")
    # Select Safety Standard "CENELEC EN 50522" in case of TT System
    else:
        safetyStandard = "1"
        logInfo (f"Selected Safety Standard {safetyStandardNames[int(safetyStandard)]}.")

    return safetyStandard

def floatParameterInput(parameterDescription, measureUnit):
    """ Function that prompts from user to provide a float value for a specific parameter and
    verifies the that the input is valid.

    Arguments:
        parameterDescription (string): Description of the parameter
        measureUnit (string): Unit of Measurement of the paramater
    Returns:
        parameter (real): Parameter variable filled with input value from user
    """
    logInfo(f"Parameter: {parameterDescription}")
    logInfo(f"Provide {parameterDescription} in {measureUnit}:")
    while True:
        parameter = input()
        # Validation of user input value
        try:
            parameter = float(parameter)
            if parameter < 0:
                raise ValueError
            logInfo(f"{parameterDescription} set as {parameter}{measureUnit}.")
            # Exit the loop if input is valid
            break
        except ValueError:
            logError(f"Input {parameter} is not a valid positive number. Please provide a positive number:")
    
    return parameter

def functionParameterInput(parameterDescription):
    """ Function that prompts from user to provide a function for a specific parameter and
    verifies the that the input function is valid.

    Arguments:
        parameterDescription (string): Description of the parameter
    Returns:
        function (lambda function): Parameter variable filled with input function from user
    """
    logInfo(f"Parameter: {parameterDescription}")
    logInfo(f"Provide {parameterDescription} function in terms of x:")
    while True:
        parameter = input()
        # Validation of user input function
        functionString = "lambda x: " + parameter + " if x > 0 else 0"
        if isValidFunction(functionString):
            logInfo(f"{parameterDescription} set as function f(x)={parameter}.")
            break
        logError(f"Input function {parameter} is not a valid function. Please provide a valid function in terms of x:")
    
    # Transformation of string into lambda function
    function = eval(functionString)
        
    return function

def promptYesNo():
    """ Function that prompts from user to provide a Yes or No input. 
    The function returns a string with the input provided by the user.

    Returns:
        answer (string): "Yes" or "No" strings provided by user 
    """
    answer = input()
    while answer not in ["Yes", "No"]:
        logWarning("Invalid option. Please select either option Yes or option No:")
        answer = input()
    
    return answer

def parameterSetup(systemType, safetyStandard):
    """ Main Function for the Parameters setup needed for the evaluation of Separation distance.
    Function considers the selected System Type and the selected Safety Standard to set the 
    necessary parameters. Function returns all set parameters.

    Arguments:
        systemType (string): System Type of MV/LV substation
        safetyStandard (string): Safety Standard

    Returns: 
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
        Rg (real): Ground Resistance (Ω)
        ρ (real): Soil Resistivity (Ωm)
        If (real): Symmetrical Ground Fault Current (A)
        Sf (real): Fault Current Division Factor (p.u.)
        XR (real): Symmetrical Ground Fault Current (s^-1)
        tf (real): Fault Duration (s)
        Df (real): Decrement Factor (p.u.)
        IG (real): Maximum Grid Current (A)
    """
    # Pretty Prints
    logInfo("")
    logInfo("PHASE 3: Parameter Setup")
    logInfo("")

    # Initialize Parameters
    Rb, k, IB, ZT, HF, BF, F, Vlim, Rg, ρ, If, Sf, XR, tf, Df = [0.0] * 15

    # Insert Geometric proportionality factor
    kg = floatParameterInput("Geometric proportionality factor", "m^-1")
    # Insert Surface potential proportionality factor function
    ksp = functionParameterInput("Surface potential proportionality factor")

    # Parameters Setup for System Type "TN" and Safety Standard "IEEE Std 80"
    if systemType == "TN" and safetyStandard == "0":
        # Insert Resistance of the human body
        Rb = floatParameterInput("Resistance of the human body", "Ω")
        # Insert Factor related to tolerable electric shock energy
        k = floatParameterInput("Factor related to tolerable electric shock energy", "A√s")
    
    # Parameters Setup for System Type "TN" and Safety Standard "CENELEC EN 50522"
    elif systemType == "TN" and safetyStandard == "1":
        # Insert Body current limit
        IB = floatParameterInput("Body current limit", "A")
        # Insert Body impedance
        ZT = floatParameterInput("Body impedance", "Ω")
        # Insert Heart current factor
        HF = floatParameterInput("Heart current factor", "p.u.")
        # Insert Body factor
        BF = floatParameterInput("Body factor", "p.u.")
        # Insert Constant F
        F = floatParameterInput("Constant F", "p.u.")

    # Parameters Setup for System Type "TT" and Safety Standard "CENELEC EN 50522"
    else:
        # Insert Voltage Limit
        Vlim = floatParameterInput("Voltage limit", "V")

    # Prompt for Calculation of Soil Resistivity
    logInfo("Please Select 'Yes' if Soil Resistivity should be calculated through Ground Resistance (Rg) and Geometric Proportionality Factor (kg) (Yes or No):")
    eval_ρ = promptYesNo()
    logInfo(f"You selected option {eval_ρ}.")
    if eval_ρ == "Yes":
        # Insert Ground Resistance
        Rg = floatParameterInput("Ground Resistance", "Ω")
        # Calculate Soil Resistivity
        ρ = soilResistivity(Rg, kg)
    else:
        # Insert Soil Resistivity
        ρ = floatParameterInput("Soil Resistivity", "Ωm")

    # Insert Fault Duration
    tf = floatParameterInput("Fault Duration", "s")

    # Prompt for Calculation of Maximum Grid Current
    logInfo("Please Select 'Yes' if Maximum Grid Current should be calculated according to IEEE Std 80 (Yes or No):")
    eval_IG = promptYesNo()
    logInfo(f"You selected option {eval_IG}.")
    if eval_IG == "Yes":
        # Insert Symmetrical Ground Fault Current
        If = floatParameterInput("Symmetrical Ground Fault Current", "A")
        # Insert Fault Current Division Factor
        Sf = floatParameterInput("Fault Current Division Factor", "p.u.")
        
        # Prompt for Calculation of Decrement Factor
        logInfo("Please Select 'Yes' if Decrement Factor should be calculated according to IEEE Std 80 (Yes or No):")
        eval_Df = promptYesNo()
        logInfo(f"You selected option {eval_Df}.")
        if eval_Df == "Yes":
            # Insert X/R Ratio
            XR = floatParameterInput("Symmetrical Ground Fault Current", "s^-1")
            ## Insert Fault Duration
            #tf = floatParameterInput("Fault Duration", "s")
            # Calculate Decrement Factor
            Df = decrementFactor(XR, tf)
        else:
            # Insert Decrement Factor
            Df = floatParameterInput("Decrement Factor", "p.u.")
        
        # Calculate Maximum Grid Current
        IG = maxGridCurrent(If, Df, Sf)
    else:
        # Insert Maximum Grid Current
        IG = floatParameterInput("Maximum Grid Current", "A")

    return kg, ksp, Rb, k, IB, ZT, HF, BF, F, Vlim, Rg, ρ, If, Sf, XR, tf, Df, IG

def plotCreation(systemType, safetyStandard, kg, ksp, Rb, k, IB, ZT, HF, BF, F, Vlim, ρ, tf, IG):
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
    # Pretty Prints
    logInfo("")
    logInfo("PHASE 4: Curve Creation")
    logInfo("")

    # Plot Parameters Setup for System Type "TN" and Safety Standard "IEEE Std 80"
    if systemType == "TN" and safetyStandard == "0":
        yLabel = "IG · √tf · ρ (A s^0.5 Ω m)"
        formulaLabel = "IG · √tf · ρ = Rb k / (ksp(x) · kg)"
        formula = lambda x: Rb * k / (ksp(x) * kg) if x > 0 else 0
    
    # Plot Parameters Setup for System Type "TN" and Safety Standard "CENELEC EN 50522"
    elif systemType == "TN" and safetyStandard == "1":
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

    # Create the plot
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(alpha=.4, linestyle='--')
    plt.plot(x_values, y_values, label=formulaLabel)
    plt.legend()

    # Case to be evaluated and be shown in the Plot
    # Calculate Ground Potential Rise
    GPR = groundPotentialRise(IG, kg, ρ)

    # Calcualte Critical Separation Distance
    x_critical = criticalSeparationDistance(systemType, safetyStandard, GPR, Rb, k, tf, ksp, IB, ZT, HF, BF, F, Vlim)

    # Set the evaluation point to highlight
    highlight_x = x_critical
    highlight_y = formula(x_critical)

    logInfo(f"Point to be highlighted in the Curve: ({highlight_x},{highlight_y})")
    
    # Add vertical and horizontal lines for the x and y axes
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    # Add a vertical line at the specified x coordinate
    plt.axvline(highlight_x, color='red', linestyle='--', label='Vertical Line')
    # Add a horizontal line at the specified y coordinate
    plt.axhline(highlight_y, color='red', linestyle='--', label='Horizontal Line')
    # Add a marker for the specified point
    plt.plot(highlight_x, highlight_y, 's', color='red')
    # annotate the line with a label
    plt.annotate(f'ρ = {ρ}', xy=(-3, highlight_y), xytext=(-5, 1.3 * highlight_y), arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.show()

def isValidFunction(func_str):
    """ Validates if the provided string is a valid lambda function containing a single variable x.
    Function returns True if the function is valid and False if the function is invalid.

    Arguments:
        func_str (string): string containing a lambda function in terms of x

    Returns: 
        True or False
    """
    try:
        # Parse the function string into an Abstract Syntax Tree (AST)
        ast_tree = ast.parse(func_str.strip())

        # Check that the AST consists of a single Lambda expression
        if not isinstance(ast_tree, ast.Module) or len(ast_tree.body) != 1 or not isinstance(ast_tree.body[0], ast.Expr) or not isinstance(ast_tree.body[0].value, ast.Lambda):
            return False

        # Check that the Lambda expression takes a single argument named 'x'
        args = ast_tree.body[0].value.args
        if len(args.args) != 1 or args.args[0].arg != 'x':
            return False

        # Check that the Lambda expression only references the 'x' variable
        for node in ast.walk(ast_tree):
            if isinstance(node, ast.Name) and node.id != 'x':
                return False

        return True
    except SyntaxError:
        return False