class physicsCalculator:
    def celsiusToKelvin():
        Tc = float(input("Enter temperature in Celsius(°C): "))
        Tk = Tc + 273
        print("Result: " + str(round(Tk)) + " K")
    
    def kelvinToCelsius():
        Tk = float(input("Enter temperature in Kelvin(K): "))
        Tc = Tk - 273
        print("Result: " + str(round(Tc)) + "°C")
    
    def celsiusToFahren():
        Tc = float(input("Enter temperature in Celsius(°C): "))
        Tf = Tc * (1.8) + 32
        print("Result:" + str(round(Tf)) + "°F")

    def fahrenToCelsius():
        Tf = float(input("Enter temperature in Fahrenheit(°F): "))
        Tc = (Tf - 32) / 1.8
        print("Result: " + str(round(Tc)) + "°F")

    def kelvinToFahren():
        Tk = float(input("Enter temperature in Kelvin(K): "))
        Tf = 1.8 * (Tk - 273) + 32
        print("Result: " + str(round(Tf)) + "°F")

    def superficialDilation(): 
        print("WARNING: Scientific Notation / Alpha must be in decimal!!!!")
        a = float(input("Enter alpha: "))
        s0 = int(input("Enter intial surface: "))
        t0 = int(input("Enter inital tempertature(°C): "))
        tf = int(input("Enter final temperature(°C): "))
        deltaS = 2 * a * s0 * (t0 + tf)
        print("Result: " + str((deltaS)))

    def volumetricDilation():
        print("WARNING: Scientific Notation / Alpha must be in decimal!!!!")
        a = float(input("Enter alpha: "))
        t0 = int(input("Enter inital tempertature(°C): "))
        tf = int(input("Enter final temperature(°C): "))
        v0 = int(input("Enter intial volume: "))
        deltaV = 3 * a * v0 * (t0 + tf)
        print("Result: " + str(deltaV) + " cm3")

    def linearThermalDilation(): #FIX: WORKING IN PROGRESS, RESULT NOT ACCURATE: Expected 100.036 not 100.035999999999
        print("WARNING: Scientific Notation / Alpha must be in decimal!!!!")
        alpha = float(input("Enter alpha: "))
        l0 = int(input("Enter inital length: "))
        deltaTheta = int(input("Enter temperature(°C): "))
        L = l0 * (1 + (alpha * deltaTheta))
        print(str(L))
    
    def fahrenToKelvin():
        Tf = float(input("Enter Temperature in Fahrenheit(°F)"))
        Tk = (Tf + 459.67) * 5 / 9
        print(str(Tk) + "K")
    
#Debug Space