# messing with while loops


# simple counter controlled loop

count = 0 # initialize the variable
while count < 10:
    print(count)
    count += 1



count = 10
while count >= 0:
    print(count)
    count -= 1
print("BLAST OFF")


# sentinel controlled loop


val = input("enter something (q to quit): ")
while val != 'q':
    print("you said: " + val)
    val = input("(q to quit):")
print ("goodbye")
