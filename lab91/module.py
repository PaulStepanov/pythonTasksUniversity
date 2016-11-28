import main

# _____1_____
print("Number 1:")
print(main.nod(5, 10))

# _____2_____
print("Number 2:")
print(main.nod_up(6, 9, 12, 15))

# _____3_____
print("Number 3:")
a = main.prime_divisor(30)
for i in a:
    print(i)

# _____4_____
print("Number 4:")


@main.task
def summ(x, y):
    return x * y


print(summ(0, 8, 12, 24))
