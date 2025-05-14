def flatten_list(lst):
    i = 0
    while i < len(lst):
        if type(lst[i]) == list:
            flatten_list(lst[i])
            lst[i : i + 1] = lst[i]
        else:
            i += 1
    return lst


# example:
list_a = [1, 2, 3, [4, 5, 6, 7], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print(list_a)
