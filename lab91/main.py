# 1
def nod(a, b):
    a = abs(a)
    b = abs(b)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


# 2
def nod_up(*arg):
    x = 0
    for i in range(len(arg)):
        x = nod(x, arg[i])
    return x


# 3
def prime_divisor(n):
    # Импортируем из модуля math функцию sqrt
    from math import sqrt

    a = [True for i in range(n)]  # всем значениям присваиваем true

    for i in range(2, int(sqrt(n))):
        if a[i]:
            for j in range(i * i, n, i):
                a[j] = False  # всем значениям массива присваивается false

    b = [i for i in range(2, len(a)) if a[i]]

    for x in b:
        if n % x == 0:
            yield x


# 4
def task(func):
    def inside(*args):
        x = args[0]
        for i in range(1, len(args)):
            x = func(x, args[i])
        return x

    return inside