import math
import cmath

# ===================================
# FX-991CW INSPIRED CALCULATOR
# ===================================

ANGLE_MODE = "DEG"
ANS = 0


# ---------- Helpers ----------

def convert_angle(x):
    return math.radians(x) if ANGLE_MODE == "DEG" else x


def convert_inverse(x):
    return math.degrees(x) if ANGLE_MODE == "DEG" else x


# ---------- Trigonometry ----------

def sin(x):
    return math.sin(convert_angle(x))


def cos(x):
    return math.cos(convert_angle(x))


def tan(x):
    return math.tan(convert_angle(x))


def asin(x):
    return convert_inverse(math.asin(x))


def acos(x):
    return convert_inverse(math.acos(x))


def atan(x):
    return convert_inverse(math.atan(x))


# ---------- Expression Engine ----------

allowed = {
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "asin": asin,
    "acos": acos,
    "atan": atan,

    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,

    "sqrt": math.sqrt,

    "log": math.log10,
    "ln": math.log,

    "abs": abs,

    "pi": math.pi,
    "e": math.e,

    "cmath": cmath,
    "math": math,

    "factorial": math.factorial,
    "perm": math.perm,
    "comb": math.comb,
}


# ---------- Menus ----------

def expression_mode():
    global ANS

    print("\nEXPRESSION MODE")
    print("Examples:")
    print("sin(30)")
    print("sqrt(144)")
    print("5+3*8")
    print("comb(10,3)")
    print("perm(10,3)")
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

        value = float(input("Enter Value: "))

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

        x = float(input("Enter Value: "))

        if choice == "1":
            print("Result =", math.log10(x))

        elif choice == "2":
            print("Result =", math.log(x))

        elif choice == "3":
            print("Result =", math.exp(x))

        elif choice == "4":
            print("Result =", 10 ** x)


def combinatorics_mode():

    while True:

        print("\n===== COMBINATORICS =====")
        print("1. nPr")
        print("2. nCr")
        print("3. Factorial")
        print("4. Back")

        choice = input("Choice: ")

        if choice == "4":
            break

        if choice == "1":

            n = int(input("n = "))
            r = int(input("r = "))

            print("Result =", math.perm(n, r))

        elif choice == "2":

            n = int(input("n = "))
            r = int(input("r = "))

            print("Result =", math.comb(n, r))

        elif choice == "3":

            n = int(input("Number = "))
            print("Result =", math.factorial(n))


def constants_mode():

    while True:

        print("\n===== CONSTANTS =====")
        print("1. PI")
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
            print("φ =", (1 + math.sqrt(5)) / 2)


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
            print("Current Mode =", ANGLE_MODE)

        elif choice == "4":
            break


# ---------- Main Loop ----------

while True:

    print("\n" + "=" * 40)
    print("       FX-991CW PYTHON EDITION")
    print("=" * 40)
    print("1. Expression Mode")
    print("2. Trigonometry")
    print("3. Logarithms")
    print("4. Combinatorics")
    print("5. Constants")
    print("6. Settings")
    print("7. Exit")

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
        settings_mode()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")