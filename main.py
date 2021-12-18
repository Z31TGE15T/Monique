from mathCalculator import *
from physicsCalculator import *
from options import Options

def main():
    while True:
        choice = int(input("Choose Operation: "))
        if choice < 5:
            break

    if choice == 1:
        Options.math()
        secondaryChoice = int((input("Choose Math operation: ")))
        if secondaryChoice == 1:
            print("[1] Congrous Arch and Number of Laps")
            mathCalculator.congruousArchNumofLaps()
        elif secondaryChoice == 2:
            print("[2] Bhaskara and Parabola graphic")
            mathCalculator.bhaskaraAndParabola()
        elif secondaryChoice == 3:
            print("[3] Convert: Degrees to Radians")
            mathCalculator.degreesToRadians()
        elif secondaryChoice == 4:
            print("[4] Convert: Radians to Degrees")
            mathCalculator.radiansToDegrees()
        elif secondaryChoice == 5:
            print("[5] Cartesian Plan")
            mathCalculator.cartesianPlane()
        elif secondaryChoice == 6:
            mathCalculator.wowee_zowee()
        else:
            print("Invalid Input!!!")


    elif choice == 2:
        Options.physics()
        secondaryChoice = int((input("Choose Physics operation: ")))
        if secondaryChoice == 1:
            print("[1] Convert: Celisus to Fahrenheit")
            physicsCalculator.celsiusToFahren()
        elif secondaryChoice == 2:
            print("[2] Convert: Celisus to Kelvin")
            physicsCalculator.celsiusToKelvin()
        elif secondaryChoice == 3:
            print("[3] Convert: Kelvin to Celsius")
            physicsCalculator.kelvinToCelsius()
        elif secondaryChoice == 4:
            print("[4] Convert: Kelvin to Fahren")
            physicsCalculator.kelvinToFahren()
        elif secondaryChoice == 5:
            print("[5] Convert: Fahrenheit to Celsius")
            physicsCalculator.fahrenToCelsius()
        elif secondaryChoice == 6:
            print("[6] Convert: Fahrenheit to Kelvin")
            physicsCalculator.fahrenToKelvin()
        elif secondaryChoice == 7:
            print("[7] Superficial Dilation")
            physicsCalculator.superficialDilation()
        elif secondaryChoice == 8:
            print("[8] Volumetric Dilation")
            physicsCalculator.volumetricDilation()
        elif secondaryChoice == 9:
            print("[9] Thermal Linear Dilation")
            physicsCalculator.linearThermalDilation()

    else:
        exit()