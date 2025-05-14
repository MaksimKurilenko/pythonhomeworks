A = [38, 27, 43, 3, 9, 82, 10, 11, 192, 34]


def merge_sort(A):
    if len(A) <= 1:
        return A
    left = merge_sort(A[: len(A)//2])
    right = merge_sort(A[len(A)//2:])

    sorted_list = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1
    return sorted_list


# example
B = merge_sort(A)
print(B)
