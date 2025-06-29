from dataclasses import dataclass, field
from typing import Callable, Optional

@dataclass
class SeparationDistanceData:
    # Basic config
    systemType: str = None                      # "TN" or "TT"
    safetyStandard: str = None                  # "0" (IEEE) or "1" (CENELEC)
    calcSoilResistivity: str = None             # "0" (Calculate Soil Resistivity) "1" (Do not calculate Soil Resistivity)
    calcMaxGridCurrent: str = None              # "0" (Calculate Maximum Gid Current) "1" (Do not calculate Maximum Gid Current)
    calcDecrementFactor: str = None             # "0" (Calculate Decrement Factor) "1" (Do not calculate Decrement Factor)

    # Electrical parameters
    geometricFactor: float = None               # kg (m^-1)
    soilResistivity: float = None               # ρ (Ωm)
    groundResistance: Optional[float] = None    # Rg (Ω)

    faultCurrent: float = None                  # If (A)
    decrementFactor: float = None               # Df (p.u.)
    faultDivisionFactor: float = None           # Sf (p.u.)
    inductiveReactance: Optional[float] = None  # X (Ω)
    resistanceAtFault: Optional[float] = None   # R (Ω)
    faultDuration: float = None                 # tf (s)

    # Human factors
    bodyResistance: Optional[float] = None       # Rb (Ω)
    energyFactor: Optional[float] = None         # k (As^0.5)
    bodyCurrentLimit: Optional[float] = None     # IB (A)
    bodyImpedance: Optional[float] = None        # ZT (Ω)
    heartFactor: Optional[float] = None          # HF (p.u.)
    bodyFactor: Optional[float] = None           # BF (p.u.)
    constantF: Optional[float] = None            # F (p.u.)
    voltageLimit: Optional[float] = None         # Vlim (V)

    # Functional
    surfacePotentialFunc: Callable[[float], float] = field(default=lambda x: 1) # ksp(x) (function)

    # Results (optional)
    maxGridCurrent: Optional[float] = None               # IG (A)
    groundPotentialRise: Optional[float] = None          # GPR (V)
    criticalSeparationDistance: Optional[float] = None   # xcr (m)