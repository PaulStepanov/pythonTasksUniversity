# insert insertString into string  after assigned index

def insertIntoString(string, insertString, index):
    str1 = string[0:index + 1]
    str2 = string[index + 1:len(string)]
    que = (str1, str2)
    return insertString.join(que)
