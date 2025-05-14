decimal = input("Please enter a number in decimal system: ")
if not decimal.isdigit():
    print("Invalid number.")
else:
    decimal = int(decimal)
    binary = " "
    if decimal == 0:
        binary = "0"
    else:
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
    print("Your number in binary system: ", binary)
    decimal_new = 0
    power = 1
    for digit in binary[::-1]:
        if digit == "1":
            decimal_new += power
        power *= 2
    print("Your number in decimal system:", decimal_new)
