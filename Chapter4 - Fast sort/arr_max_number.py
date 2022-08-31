def max(a, b):
    if a >= b:
        return a
    else:
        return b


def arr_max_number(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], arr_max_number(arr[1:]))


arr = [1, 3, 6, 4, 87, 70, 105, 33]
print(arr_max_number(arr))
