str = input("Please enter your string: ")
vowels = "aeiouAEIOU"
str1 = str
for char in str:
    if char in vowels:
        str1 = str1.replace(char, "")
print("Your new string without vowels is: ", (str1))
