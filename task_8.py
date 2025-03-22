string = input ("Please enter your string: ")
string1 = string.replace(" ", "").lower()
if string1 == string1[::-1]:
    print("True")
else:
    print("False")
    
