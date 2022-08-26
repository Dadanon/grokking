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


myArr = [random.randint(1, 1000000) for i in range(1000000)]
timeStart1 = datetime.now()
# selectionSort(myArr)
print(f"My algo: {datetime.now() - timeStart1}")
timeStart2 = datetime.now()
myArr.sort()
print(f"Built-in: {datetime.now() - timeStart2}")
