def arr_elements_count(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    else:
        return 1 + arr_elements_count(arr[1:])


arr = [1, 3, 5, 2, 6, 77]
print(arr_elements_count(arr))