list = []
n=int(input("enter number of elements:"))
for i in range(0,n):
    elem=int(input())
    list.append(elem)
    print(list)
print("list = ", list)

for ev in list:
    if (ev % 2 == 0):
        list.remove(ev)
    
print("List Items after removing even Items = ", list)
