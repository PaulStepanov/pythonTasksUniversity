list = [2,'a',5,1,-1,9,10]
result=[]
for x in list:
    try:
        value=int(x)
        if value % 2 == 0:
            result.append(x)
    except ValueError:
        pass

print(result)