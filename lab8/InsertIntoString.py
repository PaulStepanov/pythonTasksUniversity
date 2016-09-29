# insert insetring after index of string

def insertIntoString(string,insetring,index):
    str1 = string[0:index + 1]
    str2 = string[index + 1:len(string)]
    que = (str1, str2)
    return insetring.join(que)
