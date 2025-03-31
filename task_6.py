Magic_number = input("Please enter your number: ")
sum1 = sum(int(digit) for digit in str(Magic_number))
if sum1 % 7 == 0:
    print ("Magic Number!")
else:
    print("Sum of digits for your number is", sum1)