#check if a triangle is scalene, isosceles or equilateral
a = int(input("enter the first side of triangle"))
b = int(input("enter the second side of triangle"))
c = int(input("enter the third side of triangle"))

if a == b and b ==c:
    print("this is an equlateral triangle")
elif a !=b and b !=c and a !=c:
    print("this is a scalene triangle")
else:
    print("this is isosceles triangle")
    