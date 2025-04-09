user_string = input("Please enter your string: ")
substring_dict = {}
for i in range(len(user_string)):
    sub_string = ""
    for j in range(i, len(user_string)):
        if user_string[j] in sub_string:
            break
        sub_string += user_string[j]
        substring_dict[sub_string] = len(sub_string)
longest_substring = max(substring_dict, key=substring_dict.get)
print("Longest substring:", longest_substring)
