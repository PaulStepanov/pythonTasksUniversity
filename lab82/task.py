x=int(input('x: \n'))
y=int(input('y:\n'))

while x != 0 and y != 0:
    if x > y:
        x %= y
    else:
        y %= x

print (x+y)