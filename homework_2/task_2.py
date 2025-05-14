from typing import Dict, List

numbers_list: str = input("Enter the list of numbers: ")
numbers: List[str] = numbers_list.split()

unique_numbers: Dict[str, int] = {}
for number in numbers:
    unique_numbers[number] = unique_numbers.get(number, 0) + 1

unique: List[str] = []
repeating: List[str] = []
even: List[str] = []
odd: List[str] = []
negative: List[str] = []
floating: List[str] = []
multiple5: List[int] = []
comparison_list: List[float] = []

for key in unique_numbers:
    if "." in key:
        num: float = float(key)
        floating.append(key)
    else:
        num = int(key)
    comparison_list.append(num)

    if unique_numbers[key] == 1:
        unique.append(key)
    else:
        repeating.append(key)

    if int(num) % 2 == 0:
        even.append(key)
    else:
        odd.append(key)

    if num < 0:
        negative.append(key)

    if int(num) % 5 == 0:
        multiple5.append(int(num))

print("Unique numbers:", unique)
print("Repeating numbers:", repeating)
print("Even numbers:", even)
print("Odd numbers:", odd)
print("Negative numbers:", negative)
print("Floating numbers:", floating)
print("Sum of multiples of 5:", sum(multiple5))
print("Max. number:", max(comparison_list))
print("Min. number:", min(comparison_list))
