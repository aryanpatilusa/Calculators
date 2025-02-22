# ARITHMETIC CALCULATOR 1.0
# CREATED BY: ARYAN PATIL
# DATE: 21 FEBRUARY 2025
# OPERATES DIVISION MULTIPLICATION ADDITION SUBTRACTION (RAW ANSWERS)

while True:
    print("ARITHMETIC CALCULATOR 1.0")
    print("+ What type of calculation are you commiting? + ")
    print("(M) Multiplication | (D) Division | (A) Addition | (S) Subtraction")
    Type = str(input("-->  "))

    if Type == "A":
        print("ARITHMETIC CALCULATOR 1.0")
        print("OPERATION: Addition")
        print("\t")
        firstnumber = float(input("First Number = "))
        print("PLUS")
        secondnumber = float(input("Second Number = "))
        print("")
        def addition():
            return float(firstnumber) + float(secondnumber)
        print("SOLUTION: " + str(float(addition())) + "")
        exit()
    elif Type == "S":
        print("ARITHMETIC CALCULATOR 1.0")
        print("OPERATION: Subtraction")
        print("")
        firstnumber = float(input("First Number = "))
        print("MINUS")
        secondnumber = float(input("Second Number = "))
        print("")
        def subtraction():
            return float(firstnumber) - float(secondnumber)
        print("SOLUTION:" + str(float(subtraction())) + "")
        exit()
    elif Type == "M":
        print("ARITHMETIC CALCULATOR 1.0")
        print("OPERATION: Multiplication")
        print("")
        firstnumber = float(input("First Number = "))
        print("TIMES")
        secondnumber = float(input("Second Number = "))
        print("")
        def multiplication():
            return float(firstnumber) * float(secondnumber)
        print("SOLUTION: " + str(float(multiplication())) + "")
        exit()
    elif Type == "D":
        print("ARITHMETIC CALCULATOR 1.0")
        print("OPERATION: Division")
        print("")
        firstnumber = float(input("First Number = "))
        print("DIVIDED BY")
        secondnumber = float(input("Second Number = "))
        print("")
        def division():
            return float(firstnumber) / float(secondnumber)
        print("SOLUTION: " + str(float(division())) + "")
        exit()
    else:
        print("Invalid Type: Restarting...")
        print("\n\n")
