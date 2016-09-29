# Даны натуральные числа N1, N2 и строки S1, S2. Необходимо сформиро-вать
# из этих строк новую, содержащую первые N1 символов строки S1 и последние N2
# символов строки S2 (в указанном порядке).
# (Например, 2, 3, "холод", "робот" → "хобот")


while True:
    n1 = input('input h1\n >')
    n2 = input('input h2\n >')

    try:
        n2 = int(n2)
        n1 = int(n1)
    except ValueError:
        print('well,now enter a number ')
        break

    str1 = input('str1 \n >')
    str2 = input('str2 \n >')

    if n2 >= len(str2):
        n2 = 0
    else:
        n2 = len(str2) - n2

    print(str1[0:n1] + str2[n2:len(str2)])
