sum = int(input("Please enter your sum for exchange = "))
n_100 = sum // 100
sum %= 100
n_50 = sum // 50
sum %= 50
n_10 = sum // 10
sum %= 10
n_5 = sum // 5
sum %= 5
n_1 = sum // 1
if n_100 > 0:
    print("You will get", n_100, "hundred banknotes")
if n_50 > 0:
    print("You will get", n_50, "fifty banknotes")
if n_10 > 0:
    print("You will get", n_10, "ten banknotes")
if n_5 > 0:
    print("You will get", n_5, "five banknotes")
if n_1 > 0:
    print("You will get", n_1, "one banknotes")
