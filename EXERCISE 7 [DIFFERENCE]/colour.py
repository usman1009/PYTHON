a=input("enter some colors:")
b=input("enetr some colors:")
set1=set(a.split())
set2=set(b.split())
if (len(set1-set2))>0:
    print('colors that present in list1 and not in list2')
    print(set1-set2)
else:
    print('colors in list1 is also present in list2')
