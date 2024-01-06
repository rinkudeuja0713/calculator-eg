#prompt a user to enter a number and check if odd/even
msg =input("enter a number: ")
num = int(msg)

if num % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")


