# TEMPERATURE CALCULATOR 1.0
# CREATED BY: ARYAN PATIL
# DATE: 20 FEBRUARY 2025
# CONVERTS (CELSIUS, FAHRENHEIT, AND KELVIN) TO ANY

# Start of Calculator
print("TEMPERATURE CALCULATOR 1.0")
print("+ What are you CONVERTING to? +")
print("(C) Celsius | (F) Fahrenheit | (K) Kelvin")
Type = input("-->  ")

# START OF CATEGORY: CELSIUS
if Type == "C":
    print("What scale is the number currently in?")
    print("(F) Fahrenheit | (K) Kelvin")
    ctype = input("-->  ")

    # converting Fahrenheit to Celsius
    if ctype == "F":
        cel_fah = float(input("Enter the number in FAHRENHEIT : "))
        def fah_celsius():
            return (cel_fah - 32) * 5 / 9  # FAHRENHEIT TO CELSIUS
        print("Celsius: " + str(float(fah_celsius())) + "°C")
        exit()

    # Converting Kelvin to Celsius
    elif ctype == "K":
        cel_kel = float(input("Enter the number in KELVIN : "))
        def kel_celsius():
            return cel_kel - 273.15  # KELVIN TO CELSIUS
        print("Celsius: " + str(float(kel_celsius())) + "°C")
        exit()
    else:
        print("Invalid Entry.")
        exit()
# END OF CATEGORY: CELSIUS

# START OF CATEGORY: FAHRENHEIT
if Type == "F":
    print("What scale is the number currently in?")
    print("(C) Celsius | (K) Kelvin")
    ftype = input("-->  ")

    # Converting Celsius to Fahrenheit
    if ftype == "C":
        fah_cel = float(input("Enter the number in CELSIUS : "))
        def cel_fahrenheit():
            return (fah_cel * 9 / 5) + 32 # CELSIUS TO FAHRENHEIT
        print("Fahrenheit: " + str(float(cel_fahrenheit())) + "°F")
        exit()

    # Converting Kelvin to Fahrenheit
    elif ftype == "K":
        fah_kel = float(input("Enter the number in KELVIN : "))
        def kel_fahrenheit():
            return (fah_kel - 273.15) * 9 / 5 + 32 # KELVIN TO FAHRENHEIT
        print("Fahrenheit: " + str(float(kel_fahrenheit())) + "°F")
        exit()
    else:
        print("Invalid Entry.")
        exit()
# END OF CATEGORY: FAHRENHEIT

# START OF CATEGORY: KELVIN
if Type == "K":
    print("What scale is the number currently in?")
    print("(C) Celsius | (F) Fahrenheit")
    ktype = input("--> ")

    # Converting Celsius to Kelvin
    if ktype == "C":
        kel_cel = float(input("Enter the number in CELSIUS : "))
        def cel_kelvin():
            return kel_cel + 273.15
        print("Kelvin: " + str(float(cel_kelvin())) + " K")
        exit()
    elif ktype == "F":
        kel_fah = float(input("Enter the number in FAHRENHEIT : "))
        def fah_kelvin():
            return (kel_fah - 32) * 5 / 9 + 273.15
        print("Kelvin : " + str(float(fah_kelvin())) + " K")
    else:
        print("Invalid Entry.")
        exit()
    # END OF CATEGORY: KELVIN
# EXIT CODE
else:
    print("Invalid Letter: Retry.")
    exit()
