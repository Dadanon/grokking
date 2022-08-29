from datetime import datetime
from random import randint


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


arr = [randint(1, 1000000) for i in range(1000000)]
time_now = datetime.now()
quick_sort(arr)
print(f"Time is: {datetime.now() - time_now}")
time_now_2 = datetime.now()
arr.sort()
print(f"Time is: {datetime.now() - time_now_2}")
