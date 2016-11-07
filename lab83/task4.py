array=[1, 3, 4, 7, 9]
m=3
result_list = []
for i in range(len(array)):
    list = []
    a = i % m
    for j in range(len(array)):
        if array[j] % m == a:
            list.append(array[j])
    if list in result_list or len(list) == 0:
        continue
    else:
        result_list.append(list)
print(result_list)
