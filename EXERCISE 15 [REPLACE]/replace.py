string = input("enter a string:")
strList = list(string)

firstChar = strList[0]
for index, s in enumerate(strList):
     if s == firstChar and index !=0:
          strList[index] = '$'

newStr = ''
for i in strList:
     newStr += i
print('string you entered:',string)
print('modified string:',newStr)
