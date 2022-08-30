from datetime import datetime
import random
import timeit


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_sort_plus(array):
    if len(array) < 2:
        return array
    if len(array) == 3:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort_plus(less) + [pivot] + quick_sort_plus(greater)
    else:
        middle = len(array) // 2
        pivot1 = array[0]
        pivot2 = array[-1]
        less1 = [i for i in array[1:middle] if i <= pivot1]
        greater1 = [i for i in array[1:middle] if i > pivot1]
        less2 = [i for i in array[middle:-1] if i <= pivot2]
        greater2 = [i for i in array[middle:-1] if i > pivot2]
        return quick_sort_plus(less1) + [pivot1] + quick_sort_plus(greater1) + \
               quick_sort_plus(less2) + [pivot2] + quick_sort_plus(greater2)


arr = [random.randint(1, 1000000) for i in range(50000)]

#time_now = datetime.now()
#quick_sort(arr)
#print(f"Time is: {datetime.now() - time_now}")
#time_now_2 = datetime.now()
#quick_sort_plus(arr)
#print("Time plus is: ")
# print(timeit.timeit("quick_sort(arr)", number=1000, globals=globals()))
print(timeit.timeit("quick_sort_plus(arr)", number=20, globals=globals()))
