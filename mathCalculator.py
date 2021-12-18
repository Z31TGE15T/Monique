import matplotlib.pyplot as plt
import numpy as np

class mathCalculator:
    def congruousArchNumofLaps():
        user_input = int(input("Enter Number: "))
        y = user_input % 360
        x = user_input / 360
        print("Congruous Arch: " + str(y) + "°");
        print("N° of laps: " + str(round(x)));

    def bhaskaraAndParabola():
        a = int(input('Input A: '))
        b = int(input('Input B: '))
        c = int(input('Input C: '))

        # calculate delta and zero points
        delta = b**2 - 4*a*c
        if delta > 0:
            x_1 = (-b + delta ** (1 / 2)) / (2 * a)
            x_2 = (-b - delta ** (1 / 2)) / (2 * a)
        if delta == 0:
            x_0 = -b/(2*a)
        else:
            pass

        # calculate parabola extreme coordinates
        p = -b/(2*a)
        q = -delta/(4*a)
        extreme = [p,q]
        print("Results: x1: {}, x2: {}, vX: {}, vY {}".format(x_1, x_2, p, q))
        # define parabola function
        def parabola(x,a,b,c):
            y = a*x**2 + b*x + c
            return y

        # plot function
        x = np.linspace(int(p)-5,int(p)+5,100)
        y = parabola(x,a,b,c)
        plt.plot(x,y)
        plt.axhline(y=0, color='black', linestyle='-')
        plt.axvline(x=0, color='black', linestyle='-')
        plt.text(p-0.5, q-3, '[' + str(round(p,2)) +',' + str(round(q,2)) + ']',color='orange', fontsize=9)
        plt.plot(p, q, marker="o")

        if delta > 0:
            plt.plot(x_1, 0, marker="o", color='green')
            plt.text(x_1 - 0.5, 2, '[' + str(round(x_1,2)) + ']', color='green', fontsize=9)
            plt.plot(x_2, 0, marker="o", color='green')
            plt.text(x_2 - 0.5, 2, '[' + str(round(x_2,2)) + ']', color='green', fontsize=9)

        if delta == 0:
            plt.plot(x_0, 0, marker="o", color='green')
            plt.text(x_0 - 0.5, 2, '[' + str(round(x_0,2)) + ']', color='green', fontsize=9)

        plt.show()

    def stiffmeisterCoefficent():
        x = int(input("N° of Guys that a girl slept: "))
        realnumber = x * 3
        print("Real number of guys that she slept: " + str(realnumber))

    def degreesToRadians():
        degrees = int(input("N° in degrees: "))
        radians = degrees * 3.14 / 180
        print("N° in Radians: " + (str(radians)))

    def radiansToDegrees():
        radians = float(input("N° in Radians: "))
        degrees = radians * 180 / 3.14
        print("N° in Degrees: " + (str(degrees)))

    def wowee_zowee():
        alpha = int(input("Enter Alpha: "))
        radius = int(input("Enter Radius: "))
        L = (alpha * 3.14 * radius) / 180
        print("Result: " + str(L))
    
    def cartesianPlane():
        # Enter x and y coords
        print("WARNING: Don't enter all values at once, press Enter to input new X value")
        xs = float(input("Enter X: ")), float(input("Enter X: ")), float(input("Enter X: ")), float(input("Enter X: "))
        print('-------------------------------------------------------------------------------------------------------')
        print("WARNING: Don't enter all values at once, press Enter to input new Y value")
        ys = float(input("Enter Y: ")), float(input("Enter Y: ")), float(input("Enter Y: ")), float(input("Enter Y: "))
        colors = ['m', 'g', 'r', 'b']

        #Select length of axes and the space beetween tick lables
        colors = ['m', 'g', 'r', 'b']

        # Select length of axes and the space between tick labels
        xmin, xmax, ymin, ymax = -10, 10, -10, 10
        ticks_frequency = 1

        # Plot points
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.scatter(xs, ys, c=colors)

        # Draw lines connecting points to axes
        for x, y, c in zip(xs, ys, colors):
            ax.plot([x, x], [0, y], c=c, ls='--', lw=1.5, alpha=0.5)
            ax.plot([0, x], [y, y], c=c, ls='--', lw=1.5, alpha=0.5)

        # Set identical scales for both axes
        ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

        # Set bottom and left spines as x and y axes of coordinate system
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')

        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Create 'x' and 'y' labels placed at the end of the axes
        ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
        ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

        # Create custom major ticks to determine position of tick labels
        x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
        y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
        ax.set_xticks(x_ticks[x_ticks != 0])
        ax.set_yticks(y_ticks[y_ticks != 0])

        # Create minor ticks placed at each integer to enable drawing of minor grid
        # lines: note that this has no effect in this example with ticks_frequency=1
        ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
        ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

        # Draw major and minor grid lines
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

        # Draw arrows
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

        plt.show()