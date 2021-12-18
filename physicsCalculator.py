import decimal

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
        print("Result: " + str(round(Tc)) + "°C")
    
    def kelvinToFahren():
        Tk = int(input("Enter temperature in Kelvin(K): "))
        Tf = 1.8 * (Tk - 273) + 32
        print("Result: " + str(round(Tf)) + "°F")

    def fahrenToKelvin():
        Tf = int(input("Enter Temperature in Fahrenheit(°F)"))
        Tk = (Tf + 459.67) * 5 / 9
        print(str(Tk) + "K")

    def superficialDilation(): 
        a = decimal.Decimal(input("Enter alpha: "))
        s0 = int(input("Enter intial surface: "))
        t0 = int(input("Enter inital tempertature(°C): "))
        tf = int(input("Enter final temperature(°C): "))
        deltaS = round(a * s0 * (tf - t0), 4)
        print("Result: " + str((deltaS)) + "cm2")

    def volumetricDilation():
        v0 = int(input("Enter intial volume: "))
        a = decimal.Decimal(input("Enter alpha: "))
        t0 = int(input("Enter inital tempertature(°C): "))
        tf = int(input("Enter final temperature(°C): "))
        deltaV = round(a * v0 * (tf - t0), 4)
        print("Result: " + str(deltaV) + " cm3")

    def linearThermalDilation(): 
        l0 = int(input("Enter inital length: "))
        alpha = decimal.Decimal(input("Enter alpha: "))
        tf = int(input("Enter final temperature(°C):"))
        t0 = int(input("Enter final temperature(°C): "))
        deltaL = round(l0 * alpha * (tf - t0), 4)
        print(str(deltaL))
    
    def kphToMach():
        kph = int(input("Enter velcocity in Kilometers(Kph): "))
        mach = kph / 1234.8
        print(mach)
    
    def machToKPH():
        mach = int(input("Enter velcocity in mach(M):"))
        kph = mach * 1225.044
        print(kph)
    