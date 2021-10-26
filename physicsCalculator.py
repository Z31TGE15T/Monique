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
        print("Result: " + str(round(Tf)) + "°F")

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
        deltaS = 2 * a * s0 * (tf - t0)
        print("Result: " + str((deltaS)) + "cm2")

    def volumetricDilation():
        print("WARNING: Scientific Notation / Alpha must be in decimal!!!!")
        a = float(input("Enter alpha: "))
        t0 = int(input("Enter inital tempertature(°C): "))
        tf = int(input("Enter final temperature(°C): "))
        v0 = int(input("Enter intial volume: "))
        deltaV = 3 * a * v0 * (tf - t0)
        print("Result: " + str(deltaV) + " cm3")

    def linearThermalDilation(): 
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
    
    def kphToMach():
        kph = float(input("Enter velcocity in Kilometers(Kph): "))
        mach = kph / 1234.8
        print(mach)
    
    def machToKPH():
        mach = float(input())
        kph = mach * 1225.044
        print(kph)
    