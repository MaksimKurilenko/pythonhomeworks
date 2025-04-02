numbers_list = input("Enter the list of numbers:")
numbers = numbers_list.split()
unique_numbers = {}
for number in numbers:
    unique_numbers[number] = unique_numbers.get(number, 0) +1
unique = []
repeating = []
even = []
odd = []
negative = []
floating = []
multiple5 = []
comparison_list = []
for key in unique_numbers:
    if '.' in key:
        num = float(key)
        floating.append(key)
    else:
        num = int(key)
    comparison_list.append(num)
    if unique_numbers.get(key) == 1:
        unique.append(key)
    else:
        repeating.append(key)
    if num%2 == 0:
        even.append(key)
    else: 
        odd.append(key)
    if num<0:
        negative.append(key)
    if num%5 == 0:
        multiple5.append(int(key))
    
print("Unique numbers:", unique)
print("Repeating nubers:", repeating)
print("Even numbers:", even)
print("Odd items:", odd)
print("Negative numbers:", negative)
print("Floating numbers:", floating)
print("Sum of multipliers of 5: ", sum(multiple5))
print("Max. number:",max(comparison_list))
print("Min. number:", min(comparison_list))