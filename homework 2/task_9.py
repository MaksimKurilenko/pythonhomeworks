user_string = str(input("Please enter your text: ")).lower()
n = int(input("Please enter a number for encoding: "))
alphabeth = list("abcdefghijklmnopqrstuvwxyz")
words = user_string.split()
new_string = " "
for word in words:
    for char in word:
       if char in alphabeth: 
            index_char=alphabeth.index(char)
            new_index = (index_char + n)%len(alphabeth)
            new_string += alphabeth[new_index]
    else:
            new_string += char
    new_string += " "
print("Your Cesarus encoded string:" , new_string)