user_string = input("Please enter your string: ")
new_string = " "
i = 0
while i < len(user_string):
    count = 1
    for n in range(i + 1, len(user_string)):
        if user_string[i] == user_string[n]:
            count += 1
        else:
            break
    new_string += user_string[i] + str(count)
    i += count
print("Compressed string:", new_string)
