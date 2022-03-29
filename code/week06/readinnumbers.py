# Read in 2 numbers and multiply them
# Author: Brendan Heeney

num1 = int(input("enter a number "))
num2 = int(input ("and another "))

answer = num1 * num2

print(f"answer is {answer}")


# Improve the above by adding error handling

try:
    num1 = int(input("enter a number "))
except ValueError:
    num1 = int(input("no strings a number please "))


num2 = int(input ("and another "))

answer = num1 * num2

print(f"answer is {answer}")