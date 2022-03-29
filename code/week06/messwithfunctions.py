#Messing with Functions
# Author: Brendan Heeney

def cube(number):
    print(number)
    return number ** 3

num = 7
answer = cube(num)
print ("cube of", num ," is", answer)


def topower(number, power = 3): #adding a second argument to the function
    #print(number)              # power = 3 is called a default value
    return number ** power

answer = topower(7,3)
print (answer)