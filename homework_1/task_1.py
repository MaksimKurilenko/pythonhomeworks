user_last_name = input("Last name: ")
user_first_name = input("First name: ")
user_middle_name = input("Middle name: ")
str = "Your initials are: " + (
    user_last_name + " " + user_first_name[0] + "." + user_middle_name[0] + "."
)
print(str)
