a=input("enter the line")
l=a.split(" ")
s=set(l)
for i in s:
    c=l.count(i)
    print(i,'occurs',c,'times')
