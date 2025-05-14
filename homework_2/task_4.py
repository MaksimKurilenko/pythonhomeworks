values_set1 = input("Please enter the first set of numbers:")
values_set2 = input("Please enter the second set of numbers:")
set_1 = set(values_set1.split())
set_2 = set(values_set2.split())
intersections = set_1 & set_2
difference1 = set_1 - set_2
difference2 = set_2 - set_1
symm_diff = set_1 ^ set_2
print("Set 1 and Set 2 intersections are: ", intersections)
print("Set 1 number(s) missing in Set 2", difference1)
print("Set 2 number(s) missing in Set 1", difference2)
print("Symmetrical difference of Set 1 and Set 2:", symm_diff)
