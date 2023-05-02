import Functions as functions

def main():
    # Start Log
    functions.startLog()

    # PHASE 1: System Type Selection
    systemType = functions.systemTypeSelection()
    
    # PHASE 2: Safety Standard Selection
    safetyStandard = functions.safetyStandardSelection(systemType)
    
    # PHASE 3: Parameters Setup
    kg, ksp, Rb, k, IB, ZT, HF, BF, F, Vlim, Rg, ρ, If, Sf, XR, tf, Df, IG = functions.parameterSetup(systemType, safetyStandard)

    # PHASE 4: Curve Creation
    functions.plotCreation(systemType, safetyStandard, kg, ksp, Rb, k, IB, ZT, HF, BF, F, Vlim, ρ, tf, IG)

    # Close Log
    functions.closeLog()

if __name__ == "__main__":
    main()