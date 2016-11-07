list = []
array=(3, 4.1, 2)
for i in range(len(array)):
    for j in range(len(array)):
        tpl = ()
        if array[i] < array[j]:
            tpl += (array[i],)
            tpl += (array[j],)
            list.append(tpl)
print(list)