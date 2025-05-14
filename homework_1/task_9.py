number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))
if abs(number_1 - number_2) < 0.001:
    print("True")
else:
    print("False")
