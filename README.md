# **Safety Performance Evaluation of MV/LV Distribution Substations**

## Separation distance between MV/LV substation and secondary neutral grounding configurations

This repository contains a **Python Qt application** for the **safety performance evaluation of typical grounding configurations of MV/LV distribution substations**, based on the methodology presented in:

> Z.G. Datsios, P.N. Mikropoulos, *Safety performance evaluation of typical grounding configurations of MV/LV distribution substations*, Electric Power Systems Research, Vol. 150, pp. 36–44, 2017.  
> [DOI:10.1016/j.epsr.2017.04.016](https://doi.org/10.1016/j.epsr.2017.04.016)

---

### 📖 Overview

Grounding systems in MV/LV substations are crucial for safety, ensuring that **touch and step voltages** remain within acceptable limits during fault conditions.  
This tool implements the **evaluation procedures** described in the paper, allowing engineers and researchers to:

- Calculate **critical separation distances** between MV/LV substations and LV neutral grounding configurations.  
- Compare **IEEE Std 80** and **CENELEC EN 50522** safety criteria.  
- Visualize results through interactive plots.  
- Import and export parameters for reproducible studies.  

---

### ⚡ Features

- **Graphical User Interface (GUI)** built with PySide6.  
- **Parameter input panels** for:
  - System type  
  - Soil resistivity  
  - Grid current  
  - Decrement factor  
  - Safety standard  
- **Info dialogs** with detailed descriptions, units, and expected ranges.  
- **Interactive plotting** with PyQtGraph:  
  - Safety performance curves  
  - Highlighted critical points  
  - CSV-based or analytical user-defined functions for surface potential  
- **Import/Export Parameters** in JSON format.  
- **Logging panel** with severity-based color coding (*Info = white, Warning = yellow, Error = red*).

---

## 📊 Methodology

The calculations are based on the paper’s methodology:

- **Soil resistivity (ρ):**

    ρ = Rg / kg       

- **Maximum Grid Current (IG):**

    IG = If · Df · Sf

- **Ground Potential Rise (GPR):**

    GPR = IG · kg · ρ

- **Decrement Factor (Df):**

    Ta = X / (2 · π · 60 · R)

    Df = sqrt(1 + (Ta · (1 - exp(-2 · tf / Ta))) / tf)

- **Allowable Touch Voltage (UTp):**

    UTp = IB · ZT · BF / HF

- **Critical Separation Distance (xcr):**

    xcr = ksp⁻¹(EmmTouch / GPR)

    or 

    xcr = ksp⁻¹(UTp · F / GPR)

    or 

    xcr = ksp⁻¹(Vlim / GPR)


where:  
- ρ = soil resistivity (Ω·m)  
- Rg = Ground Resistance (Ω)
- kg = geometric proportionality factor (m⁻¹)
- IG = Maximum grid current (A) 
- Df = Decrement factor accounting for the dc offset of the fault current (p.u.)
- Sf = Fault current division factor, which considers fault current return paths additional to the ground (p.u.)
- If = fault current (A)
- GPR = Ground potential rise (V)
- tf = fault duration (s)
- X = Inductive reactance (Ω)
- R = System resistance at fault (Ω)
- UTp = Allowable Touch Voltage (V)
- Rb = body resistance (Ω)  
- k = tolerable energy factor (As½)
- IB = Body current limit (A)
- ZT = Body impedance (Ω)
- HF = Heart current factor (p.u.)
- BF = Body factor (p.u.)  
- F = Constant F (p.u.) 
- Vlim = Voltage limit (V)
- EmmTouch = Maximum allowable metal-to-metal touch voltage limit (V)
- ksp(x) = surface potential proportionality factor expressed as a function of separation distance, x (m), accounting for the effect of grounding system geometry on Vsp
- xcr = Critical Separation Distance (m)


![SubStationGuard Application Logic Flowchart](assets/SubStationGuard%20Application%20Logic%20Flowchart.png)


---

## 🚀 Installation

