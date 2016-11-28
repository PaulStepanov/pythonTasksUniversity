L=['a',1,-2,1.2]
print('1:',[x for x in L if type(x)==int and x%2==0])
print('2: ',[L[i] for i in range(len(L)) if i%2==0])
print('3: ',[x for x in L if type(x)!=str and x>0 ])
L=[1,3,9,7,4,11,14]
m=3
print('4: ',[{x for x in L if x%m==y} for y in {x%m for x in L} ])
L={1:2,'a':3,-1:1,3:'a'}
print('5: ',[x+L[x] for x in L if type(x)!=str and type(L[x])!=str])
L=[3,4.1,2]
print('6: ',[(x,y) for x in L for y in L if x<y])
L=['a',1,-2,1.2]
print('7: ',{L[i]:L[i+1] for i in range(len(L)-1) if i%2==0})



