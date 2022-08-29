from datetime import datetime
import random


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append((arr.pop(smallest)))
    return newArr


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


myArr = [random.randint(1, 100000) for i in range(1000000)]
timeStart1 = datetime.now()
# selectionSort(myArr)
print(f"Selection sort: {datetime.now() - timeStart1}")
timeStart2 = datetime.now()
quick_sort(myArr)
print(f"Fast sort: {datetime.now() - timeStart2}")
