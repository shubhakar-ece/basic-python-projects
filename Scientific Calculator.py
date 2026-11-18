import math

while True:
    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Exit")

    choice = input("Enter your choice (1-11): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a + b)

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a - b)

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a * b)

    elif choice == '4':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if b == 0:
            print("Cannot divide by zero!")
        else:
            print("Result =", a / b)

    elif choice == '5':
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result =", a ** b)

    elif choice == '6':
        num = float(input("Enter number: "))
        print("Result =", math.sqrt(num))

    elif choice == '7':
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.sin(math.radians(angle)))

    elif choice == '8':
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.cos(math.radians(angle)))

    elif choice == '9':
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.tan(math.radians(angle)))

    elif choice == '10':
        num = float(input("Enter number: "))
        print("Result =", math.log10(num))

    elif choice == '11':
        print("Calculator Closed.")
        break

    else:
        print("Invalid choice! Please try again.")