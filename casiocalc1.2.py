import math
import cmath
from collections import Counter

# ======================================
# FX-991CW PYTHON EDITION
# ======================================

ANGLE_MODE = "DEG"
ANS = 0


# ======================================
# ANGLE HELPERS
# ======================================

def to_radians(x):
    if ANGLE_MODE == "DEG":
        return math.radians(x)
    return x


def from_radians(x):
    if ANGLE_MODE == "DEG":
        return math.degrees(x)
    return x


# ======================================
# TRIG FUNCTIONS
# ======================================

def sin(x):
    return math.sin(to_radians(x))


def cos(x):
    return math.cos(to_radians(x))


def tan(x):
    return math.tan(to_radians(x))


def asin(x):
    return from_radians(math.asin(x))


def acos(x):
    return from_radians(math.acos(x))


def atan(x):
    return from_radians(math.atan(x))


# ======================================
# EXPRESSION MODE
# ======================================

allowed = {
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "asin": asin,
    "acos": acos,
    "atan": atan,

    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,

    "abs": abs,
    "round": round,

    "pi": math.pi,
    "e": math.e,

    "factorial": math.factorial,
    "perm": math.perm,
    "comb": math.comb,

    "cmath": cmath,
    "math": math
}


def expression_mode():
    global ANS

    print("\n===== EXPRESSION MODE =====")
    print("Examples:")
    print("2+3*4")
    print("sin(30)")
    print("sqrt(144)")
    print("factorial(5)")
    print("comb(10,3)")
    print("Ans*2")

    expr = input("\nExpression: ")

    try:
        expr = expr.replace("^", "**")
        expr = expr.replace("Ans", str(ANS))

        result = eval(
            expr,
            {"__builtins__": None},
            allowed
        )

        ANS = result

        print("\nResult =", result)

    except Exception as e:
        print("Error:", e)


# ======================================
# TRIGONOMETRY MODE
# ======================================

def trig_mode():

    while True:

        print("\n===== TRIGONOMETRY =====")
        print("1. sin")
        print("2. cos")
        print("3. tan")
        print("4. asin")
        print("5. acos")
        print("6. atan")
        print("7. Back")

        choice = input("Choice: ")

        if choice == "7":
            break

        try:
            value = float(input("Value: "))

            if choice == "1":
                print("Result =", sin(value))

            elif choice == "2":
                print("Result =", cos(value))

            elif choice == "3":
                print("Result =", tan(value))

            elif choice == "4":
                print("Result =", asin(value))

            elif choice == "5":
                print("Result =", acos(value))

            elif choice == "6":
                print("Result =", atan(value))

        except:
            print("Invalid Input")


# ======================================
# LOGARITHM MODE
# ======================================

def log_mode():

    while True:

        print("\n===== LOGARITHMS =====")
        print("1. log10(x)")
        print("2. ln(x)")
        print("3. e^x")
        print("4. 10^x")
        print("5. Back")

        choice = input("Choice: ")

        if choice == "5":
            break

        try:
            x = float(input("Value: "))

            if choice == "1":
                print("Result =", math.log10(x))

            elif choice == "2":
                print("Result =", math.log(x))

            elif choice == "3":
                print("Result =", math.exp(x))

            elif choice == "4":
                print("Result =", 10 ** x)

        except:
            print("Invalid Input")


# ======================================
# COMBINATORICS MODE
# ======================================

def combinatorics_mode():

    while True:

        print("\n===== COMBINATORICS =====")
        print("1. nCr")
        print("2. nPr")
        print("3. Factorial")
        print("4. Back")

        choice = input("Choice: ")

        if choice == "4":
            break

        try:

            if choice == "1":

                n = int(input("n: "))
                r = int(input("r: "))

                print("Result =", math.comb(n, r))

            elif choice == "2":

                n = int(input("n: "))
                r = int(input("r: "))

                print("Result =", math.perm(n, r))

            elif choice == "3":

                n = int(input("Number: "))

                print("Result =", math.factorial(n))

        except:
            print("Invalid Input")


# ======================================
# CONSTANTS MODE
# ======================================

def constants_mode():

    while True:

        print("\n===== CONSTANTS =====")
        print("1. Pi")
        print("2. Euler Number")
        print("3. Golden Ratio")
        print("4. Back")

        choice = input("Choice: ")

        if choice == "4":
            break

        elif choice == "1":
            print("π =", math.pi)

        elif choice == "2":
            print("e =", math.e)

        elif choice == "3":
            phi = (1 + math.sqrt(5)) / 2
            print("φ =", phi)


# ======================================
# COMPLEX NUMBER MODE
# ======================================

def complex_mode():

    while True:

        print("\n===== COMPLEX NUMBERS =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Magnitude")
        print("6. Phase Angle")
        print("7. Back")

        choice = input("Choice: ")

        if choice == "7":
            break

        try:

            if choice in ["1", "2", "3", "4"]:

                z1 = complex(input("First Complex Number: "))
                z2 = complex(input("Second Complex Number: "))

                if choice == "1":
                    print("Result =", z1 + z2)

                elif choice == "2":
                    print("Result =", z1 - z2)

                elif choice == "3":
                    print("Result =", z1 * z2)

                elif choice == "4":
                    print("Result =", z1 / z2)

            elif choice == "5":

                z = complex(input("Complex Number: "))
                print("Magnitude =", abs(z))

            elif choice == "6":

                z = complex(input("Complex Number: "))
                print(
                    "Phase Angle =",
                    math.degrees(cmath.phase(z))
                )

        except:
            print("Invalid Input")


# ======================================
# STATISTICS MODE
# ======================================

def statistics_mode():

    while True:

        print("\n===== STATISTICS =====")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        print("4. Variance")
        print("5. Standard Deviation")
        print("6. Back")

        choice = input("Choice: ")

        if choice == "6":
            break

        try:

            data = list(
                map(
                    float,
                    input(
                        "Enter values separated by spaces: "
                    ).split()
                )
            )

            if choice == "1":

                print(
                    "Mean =",
                    sum(data) / len(data)
                )

            elif choice == "2":

                data.sort()
                n = len(data)

                if n % 2 == 1:
                    print("Median =", data[n // 2])
                else:
                    print(
                        "Median =",
                        (data[n//2-1] + data[n//2]) / 2
                    )

            elif choice == "3":

                print(
                    "Mode =",
                    Counter(data).most_common(1)[0][0]
                )

            elif choice == "4":

                mean = sum(data) / len(data)

                variance = sum(
                    (x - mean) ** 2
                    for x in data
                ) / len(data)

                print("Variance =", variance)

            elif choice == "5":

                mean = sum(data) / len(data)

                variance = sum(
                    (x - mean) ** 2
                    for x in data
                ) / len(data)

                print(
                    "Standard Deviation =",
                    math.sqrt(variance)
                )

        except:
            print("Invalid Input")
# ======================================
# EQUATION SOLVER
# ======================================

def equation_solver():

    while True:

        print("\n===== EQUATION SOLVER =====")
        print("1. Linear Equation (ax + b = 0)")
        print("2. Quadratic Equation (ax² + bx + c = 0)")
        print("3. Simultaneous 2x2 Equations")
        print("4. Simultaneous 3x3 Equations")
        print("5. Back")
        print("6. Back")

        choice = input("Choice: ")

        if choice == "6":
            break

        try:

            # -------------------------
            # Linear
            # -------------------------
            if choice == "1":

                print("\nEquation Form:")
                print("ax + b = 0")

                a = float(input("a = "))
                b = float(input("b = "))

                if a == 0:
                    print("Not a valid linear equation.")
                else:
                    x = -b / a
                    print("x =", x)

            # -------------------------
            # Quadratic
            # -------------------------
            elif choice == "2":

                print("\nEquation Form:")
                print("ax² + bx + c = 0")

                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))

                if a == 0:
                    print("Not a quadratic equation.")
                    continue

                discriminant = b**2 - 4*a*c

                if discriminant > 0:

                    x1 = (-b + math.sqrt(discriminant)) / (2*a)
                    x2 = (-b - math.sqrt(discriminant)) / (2*a)

                    print("Root 1 =", x1)
                    print("Root 2 =", x2)

                elif discriminant == 0:

                    x = -b / (2*a)

                    print("Repeated Root =", x)

                else:

                    x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
                    x2 = (-b - cmath.sqrt(discriminant)) / (2*a)

                    print("Complex Root 1 =", x1)
                    print("Complex Root 2 =", x2)

            # -------------------------
            # Simultaneous Equations
            # -------------------------
            elif choice == "3":

                print("\nEquation 1:")
                print("a1x + b1y = c1")

                a1 = float(input("a1 = "))
                b1 = float(input("b1 = "))
                c1 = float(input("c1 = "))

                print("\nEquation 2:")
                print("a2x + b2y = c2")

                a2 = float(input("a2 = "))
                b2 = float(input("b2 = "))
                c2 = float(input("c2 = "))

                determinant = a1*b2 - a2*b1

                if determinant == 0:
                    print("No unique solution.")
            
                else:
                    x = (c1*b2 - c2*b1) / determinant

                    y = (a1*c2 - a2*c1) / determinant

                    print("x =", x)
                    print("y =", y)

        except Exception as e:

            print("Error:", e) 

    if  choice == "4":

        print("Equation 1: a1x + b1y + c1z = d1")

    a1 = float(input("a1 = "))
    b1 = float(input("b1 = "))
    c1 = float(input("c1 = "))
    d1 = float(input("d1 = "))

    print("\nEquation 2:")

    a2 = float(input("a2 = "))
    b2 = float(input("b2 = "))
    c2 = float(input("c2 = "))
    d2 = float(input("d2 = "))

    print("\nEquation 3:")

    a3 = float(input("a3 = "))
    b3 = float(input("b3 = "))
    c3 = float(input("c3 = "))
    d3 = float(input("d3 = "))

    D = (
        a1*(b2*c3-b3*c2)
        - b1*(a2*c3-a3*c2)
        + c1*(a2*b3-a3*b2)
    )

    if D == 0:
        print("No unique solution.")
    else:

        Dx = (
            d1*(b2*c3-b3*c2)
            - b1*(d2*c3-d3*c2)
            + c1*(d2*b3-d3*b2)
        )

        Dy = (
            a1*(d2*c3-d3*c2)
            - d1*(a2*c3-a3*c2)
            + c1*(a2*d3-a3*d2)
        )

        Dz = (
            a1*(b2*d3-b3*d2)
            - b1*(a2*d3-a3*d2)
            + d1*(a2*b3-a3*b2)
        )

        print("x =", Dx/D)
        print("y =", Dy/D)
        print("z =", Dz/D)


# ======================================
# SETTINGS
# ======================================

def settings_mode():

    global ANGLE_MODE

    while True:

        print("\n===== SETTINGS =====")
        print("1. Degree Mode")
        print("2. Radian Mode")
        print("3. Show Current Mode")
        print("4. Back")

        choice = input("Choice: ")

        if choice == "1":
            ANGLE_MODE = "DEG"
            print("Degree Mode Enabled")

        elif choice == "2":
            ANGLE_MODE = "RAD"
            print("Radian Mode Enabled")

        elif choice == "3":
            print("Current Mode:", ANGLE_MODE)

        elif choice == "4":
            break


# ======================================
# MAIN MENU
# ======================================

while True:

    print("\n" + "=" * 45)
    print("       FX-991CW PYTHON EDITION")
    print("=" * 45)

    print("1. Expression Mode")
    print("2. Trigonometry")
    print("3. Logarithms")
    print("4. Combinatorics")
    print("5. Constants")
    print("6. Complex Numbers")
    print("7. Statistics")
    print("8. Equation Solver")
    print("9. Settings")
    print("10. Exit")

    choice = input("Select: ")

    if choice == "1":
        expression_mode()

    elif choice == "2":
        trig_mode()

    elif choice == "3":
        log_mode()

    elif choice == "4":
        combinatorics_mode()

    elif choice == "5":
        constants_mode()

    elif choice == "6":
        complex_mode()

    elif choice == "7":
        statistics_mode()

    elif choice == "8":
        equation_solver()

    elif choice == "9":
        settings_mode()

    elif choice == "10":
        print("Goodbye!")
        break


  
    else:
        print("Invalid Choice")