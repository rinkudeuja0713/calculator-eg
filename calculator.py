#create a calculator for addition, subtraction, multiplication, division
import math
num1 = int(input("enter the first number"))

num2 = int(input("enter the second number"))

action= int(input("select the operation you want to perform\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))


if action == 1:
    print(num1,"+",num2,"=" ,num1+num2)
elif action == 2:
    print(num1, "-", num2, "=",num1-num2)
elif action == 3:
    print(num1, "*", num2, "=",num1*num2)
else:
    print(num1, "/", num2, "=",num1/num2)