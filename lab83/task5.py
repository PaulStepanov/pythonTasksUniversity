list={1: 2, 'a': 3, -1: 1, 3: 'a'}
result=[]


for key in list.keys():
    try :
        if str(list[key]).isdigit() and str(abs(key)).isdigit():
            result.append(key+list[key])
    except ValueError:
        pass
    except TypeError:
        pass
print(result)