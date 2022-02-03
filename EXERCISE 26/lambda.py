a=int(input("enter the side of square:\t"))
l=int(input("enter the length of rectangle:\t"))
b=int(input("enter the base of rectangle:\t"))
b1=int(input("enter the base of triangle:\t"))
h=int(input("enter the height of triangle:\t"))
s=lambda a: a*a
r=lambda l,b:l*b
t=lambda b1,h:(1/2)*b1*h
print("the area of square is:\t",s(a))
print("the area of rectangle is:\t",r(l,b))
print("the area of triangle is:\t",t(b1,h))







