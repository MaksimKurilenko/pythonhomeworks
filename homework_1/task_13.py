from typing import Dict

units_dict: Dict[int, str] = {
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

tens_dict: Dict[int, str] = {
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

decimal_str: str = input("Please enter a decimal number from 1 to 100: ")

if not decimal_str.isdigit():
    print("Invalid number. Number can only contain digits.")
else:
    decimal: int = int(decimal_str)

    if decimal < 1 or decimal > 100:
        print("Invalid number. Please enter a number from 1 to 100")
    elif decimal == 100:
        print("Your Roman number: C")
    else:
        tens: int = decimal // 10
        units: int = decimal % 10
        roman_number: str = tens_dict[tens] + units_dict[units]
        print("Your Roman number:", roman_number)
