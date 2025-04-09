values = input("Please enter a list of values: ")
values_list = values.split()
unique_values = []
for value in values_list:
    if value not in unique_values:
        unique_values.append(value)
print("The list without duplicates: ", unique_values)