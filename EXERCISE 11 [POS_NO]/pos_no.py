list1=input("enter the numbers seperated by comma's:")
list1=list1.split(",")
list1=list(map(int,list1))
pos_no=[num for num in list1 if num>0]
print('the list is:',list1)
print('the list of positive number',pos_no)

