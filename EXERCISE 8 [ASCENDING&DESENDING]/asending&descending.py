n=int(input("enter num of values to insert:"))
d={}
for i in range(n):
    key=input("enter the key:")
    value=input("enter the value:")
    d[key]=value
print('before sorting:',d)
print('after sorting:',sorted(d.items()))
print('after sorting decending:',sorted(d.items(),reverse=True))
