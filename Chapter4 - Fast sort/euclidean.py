def GCD(number1, number2):
    if number1 == number2:
        return number1
    if number1 < number2:
        number1, number2 = number2, number1
    if number1 % number2 == 0:
        return number2
    else:
        number1 %= number2
        return GCD(number2, number1)


print(GCD(1680, 640))
