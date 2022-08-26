from datetime import datetime


def factorial_recursion(number):
    if number >= 1:
        if number == 1:
            return number
        else:
            return number * factorial_recursion(number - 1)


def factorial_iteration(number):
    if number >= 1:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


timeStart1 = datetime.now()
# factorial_recursion(888)
# Recursion breaks at numbers close to 1000
print(f"Recursion: {datetime.now() - timeStart1}")
timeStart2 = datetime.now()
factorial_iteration(88888)
print(f"Iteration: {datetime.now() - timeStart2}")
