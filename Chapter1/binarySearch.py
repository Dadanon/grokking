import math


def binary_search(listt, item):
    low = 0
    high = len(listt) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = listt[mid]

        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


def exp_form(number):
    fact = math.factorial(number)
    logo = math.log(fact)
    multi = math.exp(logo % 1)
    power = logo // 1
    return f"{str(multi)[:4]}e^{int(power)}"


arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 7))
print(exp_form(100))
