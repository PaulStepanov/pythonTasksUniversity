list=['a',1,-2,1.2]
result=[]
for x in list:
    try:
        value=int(x)
        if value > 0:
            result.append(x)
    except ValueError:
        pass
print(result)