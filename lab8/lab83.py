# Даны две строки S1 и S2. Необходимо сформировать из этих строк новую строку,
# поочередно включающую символы из исходных. (Например, "порма", "ргам" → "программа").

from  InsertIntoString import insertIntoString

s1 = input('s1:\n >')
s2 = input('s2:\n >')
s1Count = 0
for i in range(len(s2)):
    s1 = insertIntoString(s1, s2[i], s1Count)
    s1Count += 2
print(s1)
