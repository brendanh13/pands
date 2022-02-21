# Checking format of IF statements



if 2 != 2:
    print("i hope this is not displayed")
else:
    print("2 is not equal to 2 is false")


aNumber = 9
if (aNumber % 2) == 0:
    print(aNumber, "is even")
elif (aNumber % 3) == 0:
    print(aNumber, "is divisble by 3")
else:
    print(aNumber,"is not even or divisble by 3")

print("this will always be outputted")