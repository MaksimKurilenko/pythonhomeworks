password = input("Please enter your password: ")
if len(password) < 16:
    print("Password is too short")
elif password.isdigit() or password.isalpha():
    print("Password is too weak")
else:
    print("Good Password")
