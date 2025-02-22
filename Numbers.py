# ARITHMETIC CALCULATOR 1.0
# CREATED BY: ARYAN PATIL
# DATE: 21/22 FEBRUARY 2025
# OPERATES DIVISION MULTIPLICATION ADDITION SUBTRACTION (RAW ANSWERS)

import math
import cmath
while True:
    print("     ARITHMETIC & SCIENTIFIC CALCULATOR 2.0")
    print("+ What type of calculation are you committing? + ")
    print("     ARITHMETIC     &       ADVANCED\n(A) Addition        | (I) Integer Division  \n(S) Subtraction     | (E) Exponent") # Arithmetic
    print("(M) Multiplication  | (R) Remainder    \n(D) Division        | (P) Percentage") # Advanced Arithmetic
    print("\nType \"END\" to exit")
    Type = str(input("-->  "))
# BASIC ARITHMETIC
    if Type == "A":
        print("ARITHMETIC CALCULATOR 2.0")
        print("OPERATION: Addition")
        print("\t")
        augend = float(input("Number = "))
        print("PLUS")
        increment = float(input("Increment = "))
        print("")
        def addition():
            return float(augend) + float(increment)
        print("SUM: " + str(float(addition())) + "")
        print("\n")
    elif Type == "S":
        print("ARITHMETIC CALCULATOR 2.0")
        print("OPERATION: Subtraction")
        print("")
        minuend = float(input("Number = "))
        print("MINUS")
        decrement = float(input("Decrement = "))
        print("")
        def subtraction():
            return float(minuend) - float(decrement)
        print("SOLUTION: " + str(float(subtraction())))
        print("\n")
    elif Type == "M":
        print("ARITHMETIC CALCULATOR 2.0")
        print("OPERATION: Multiplication")
        print("")
        multiplier = float(input("Multiplier = "))
        print("TIMES")
        multiplicand = float(input("Multiplicand = "))
        print("")
        def multiplication():
            return float(multiplier) * float(multiplicand)
        print("PRODUCT: " + str(float(multiplication())))
        print("\n")
    elif Type == "D":
        print("ARITHMETIC CALCULATOR 2.0")
        print("OPERATION: Division")
        print("")
        numerator = float(input("Numerator = "))
        print("DIVIDED BY")
        denominator = float(input("Denominator = "))
        print("")
        def division():
            return float(numerator) / float(denominator)
        print("QUOTIENT: " + str(float(division())))
        print("")
        print("\n")
# ADVANCED ARITHMETIC
    elif Type == "I":
        print("ADVANCED ARITHMETIC CALCULATOR 2.0")
        print("+ Select the category you'd like. +")
        print("(F) Floor Division OR (C) Ceiling Division")
        print("")
        choice = str(input("-->  "))
        if choice == "F":
            print("OPERATION: Floor Division")
            print("")
            dividend = float(input("Dividend = "))
            print("FLOOR DIVIDED")
            divisor = float(input("Divisor = "))
            print("")
            def floordivision():
                return float(dividend) // float(divisor)
            print("SOLUTION: " + str(floordivision()))
            print("")
            print("\n")
        if choice == "C":
            print("OPERATION: Ceiling Division")
            print("")
            dividend = float(input("Dividend = "))
            print("CEILING DIVIDED")
            divisor = float(input("Divisor = "))
            print("")
            def ceilingdivision():
                return math.ceil(dividend / divisor)
            print("SOLUTION: " + str(ceilingdivision()))
            print("\n")
    elif Type == "E":
        print("ADVANCED ARITHMETIC CALCULATOR 2.0")
        print("OPERATION: Exponent (Power)")
        print("")
        base = float(input("Base = "))
        print("EXPONENTIATED")
        exponent = float(input("Exponent = "))
        def exponential():
            return base ** exponent
        print("SOLUTION: " + str(exponential()))
        print("")
        print("\n")
    elif Type == "R":
        print("ADVANCED ARITHMETIC CALCULATOR 2.0")
        print("OPERATION: Remainder (Division)")
        print("")
        dividend = float(input("Dividend = "))
        print("")
        divisor = float(input("Divisor = "))
        def remainder():
            return dividend % divisor
        print("SOLUTION: " + str(remainder()))
        print("")
        print("\n")
    elif Type == "AV":
        print("ADVANCED ARITHMETIC CALCULATOR 2.0") # Was removed but code may be useful.
        print("OPERATION: Absolute Value")
        print("")
        distance = float(input("Distance (Number) = "))
        print("")
        def absolutevalue():
            return math.fabs(distance)
        print("MAGNITUDE: " + str(float(absolutevalue())))
        print("Absolute Value is just the number in positive! You don't need a calculator for this.")
        print("\n")
    elif Type == "P":
        print("ADVANCED ARITHMETIC CALCULATOR 2.0")
        print("OPERATION: Percentage")
        print("")
        part = float(input("Part = "))
        print("")
        total = float(input("Total = "))
        def percentage():
            return (part / total) * 100
        print("PERCENTAGE: " + str(float(percentage())) + "% of 100")
        print("\n")
    elif Type == "END":
        exit()
    else:
        print("Invalid Type: Restarting...")
        print("\n\n")
