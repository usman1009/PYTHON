list1 = input("enter the elements:")
list1 = list1.split(",")
list1 = list(map(int,list1))
list2 = input("enter the elements:")
list2 = list2.split(",")
list2 = list(map(int,list2))

if len(list1) == len(list2):
    print('length of lists are same',len(list1))
else:
    print('different lengths are below:\n')
    print('length of list1:',len(list1))
    print('length of list2:',len(list2))

if sum(list1) == sum(list2):
    print('sum of lists are same',sum(list1))
else:
    print('different sums are below:\n')
    print('sum of list1:',sum(list1))
    print('sum of list2:',sum(list2))

set1=set(list1)
set2=set(list2)
if len(set1.intersection(set2)) > 0:
    print('common elements in both sets are:',set1.intersection(set2))
else:
    print("both sets has no common elements")
    

