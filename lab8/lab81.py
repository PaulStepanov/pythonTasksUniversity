
s=input('s:\n')
s0=input('s0:\n')
res=''
n=s.find(s0)
while ~n:
    res+=s[n:len(s0)]
    n=s.find(s0)
