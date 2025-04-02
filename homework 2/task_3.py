user_list = input("Please enter list of numbers:")
numbers = user_list.split()
numbers_list = []
difference_list = []
for number in numbers:
    numbers_list.append(int(number))
max_value = max(numbers_list)
for element in numbers_list:
    b = max_value - element
    if b !=0:
        difference_list.append(b)
min_value = min(difference_list)
second_largest = max_value - min_value
print("Second largest number is: ", second_largest)
