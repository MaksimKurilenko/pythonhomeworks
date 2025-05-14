units_dict = {
    0: "",
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
}
tens_dict = {
    0: "",
    1: "X",
    2: "XX",
    3: "XXX",
    4: "XL",
    5: "L",
    6: "LX",
    7: "LXX",
    8: "LXXX",
    9: "XC",
}
decimal = input("Please enter a decimal number from 1 to 100: ")
if not decimal.isdigit():
    print("Invalid number. Number can only contain digits.")
else:
    decimal = int(decimal)
    if decimal < 1 or decimal > 100:
        print("Invalid number. Please enter a number from 1 to 100 ")
    if decimal == 100:
        print("Your Roman number: C")
    else:
        tens = decimal // 10
        units = decimal % 10
        roman_number = tens_dict[tens] + units_dict[units]
        print("Your Roman number: ", roman_number)
