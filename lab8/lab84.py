# Даны строка S, символ C и строка S0. Необходимо после каждого
# вхождения символа C в строку S вставить строку S0.
# (Например, "пример", ’р’, "сла" → "прслаимерсла").

from  InsertIntoString import insertIntoString

s = input('s:\n >')
c = input('sc:\n >')
s0 = input('s0:\n >')

indexes = []
index = s.find(c)
while ~index:
    indexes.append(index)
    index = s.find(c, index + 1, len(s))
res = s

# reverse array to prevent increase of string
# during inserting elements
indexes.reverse()
for i in indexes:
    res = insertIntoString(res, s0, i)
print(res)
