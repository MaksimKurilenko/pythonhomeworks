from typing import Dict

user_string: str = input("Please enter your string: ")
substring_dict: Dict[str, int] = {}

for i in range(len(user_string)):
    sub_string: str = ""
    for j in range(i, len(user_string)):
        if user_string[j] in sub_string:
            break
        sub_string += user_string[j]
        substring_dict[sub_string] = len(sub_string)

longest_substring: str = max(substring_dict, key=lambda s: substring_dict.get(s, 0))
print("Longest substring:", longest_substring)
