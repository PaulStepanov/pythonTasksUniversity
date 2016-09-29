n1 = input('input h1\n');
n2 = input('input h2\n слава украине');
str1 = input('str1');
str2 = input('str2');
if int(n2) >= len(str2):
    n2 = -1
print(str1[0:int(n1)] + str2[int(n2) + 1:len(str2)]);
