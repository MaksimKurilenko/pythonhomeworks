def unique_elements(list_a):
    new_list = []

    def flatten_list(lst):
        i = 0
        while i < len(lst):
            if type(lst[i]) is list:
                lst[i : i + 1] = lst[i]
            else:
                if lst[i] not in new_list:
                    new_list.append(lst[i])
                i += 1

    flatten_list(list_a)
    return new_list


# example:
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))
