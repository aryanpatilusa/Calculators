print("Time Converter\n This program allows you to convert EST to any time in the world.\n RULES: EST, 24 Hour Clock, Decimal Answer (9:26 --> 9.26)")
current_time = float(input("What is the current TIME?: "))
print("")
print("(CST) Central Time | (MST) Mountain Time | (PST) Pacific Time")
convert_time = (input("What time do you want to convert to?: "))

if convert_time == "CST":
    def est_to_cst():
        return float(current_time) - 1
    print("The time in CST is {}.".format(est_to_cst()))

elif convert_time == "MST":
    def est_to_mst():
        return float(current_time) - 2
    print("The time in MST is {}.".format(est_to_mst()))

elif convert_time == "PST":
    def est_to_pst():
        return float(current_time) - 3
    print("The time in PST is {}.".format(est_to_pst()))
else:
    print("Invalid Entry!")
