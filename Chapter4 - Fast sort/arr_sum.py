def arr_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + arr_sum(arr[1:])


arr = []
print(arr_sum(arr))