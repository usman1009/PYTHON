list = []
n=int(input("enter number of elements:"))
for i in range(0,n):
    elem=int(input())
    list.append(elem)
    print("list=",list)

    
for i in range(0,n):
    if (list[i]>100):
        list[i]="over"
        print(list)
