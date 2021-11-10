#lambda functions to find area of shapes

s=lambda a:a*a
r=lambda l,b:l*b
t=lambda b,h:(b*h)/2

a=int(input("enter the side of square="))
l=int(input("enter the length of rectangle="))
b=int(input("enter the breadth of rectangle="))
b1=int(input("enter the breadth of triangle="))
h=int(input("enter the height of triangle="))

print("area of Square=",s(a))
print("area of Rectangle=",r(l,b))
print("area of Trianglee=",t(b1,h))