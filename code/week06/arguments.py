# Flexible Arguments
# Author: Brendan Heeney

def flex1(*args):
    print (type(args))
    for x in args:
        print (x)

flex1(1, 2, 3, "hi", [])

# Keyword Arguments

def flex2(**kwargs):
    print(type(kwargs))

flex2(age = 23, title = "Hi")


def flex2(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print (f"{key} is {value}")

flex2(age = 23, title = "Hi")

# Function for Average of List of Arguments

def ave(*args):
    sumOfNumbers = sum(args)
    length = len (args)
    return sumOfNumbers/length, sumOfNumbers

average, sumof = ave(3,4,5,6)
print ("average is", average, "sum is", sumof)

print(ave(2,3,4))