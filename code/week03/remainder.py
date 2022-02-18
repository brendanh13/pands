# program that checks for remainder only

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

remainder = x%y # % gives the remainder
print("{} divided by {} has remainder {}".format( x, y, remainder))