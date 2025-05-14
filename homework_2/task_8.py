import random

a = random.randint(1, 100)
print(a)
while True:
    b = int(
        input("System have guessed a number from 1 to 100. Try to win. Your guess: ")
    )
    if b < a:
        print("Your number is smaller than the System number. Try again.")
    elif b > a:
        print("Your number is bigger than the System number. Try again.")
    else:
        print("You won!")
        break
