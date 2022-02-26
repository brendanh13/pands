# lab question 3 - queue with random numbers

import random
queue = []

numberOfRandom = 10
rangeOfRandom = 100

for n in range(0,numberOfRandom):
    queue.append(random.randint(0,rangeOfRandom))

print("queue is {}.".format(queue))


while len(queue) != 0:

    currentNumber = queue.pop(0)
    print("current number is {} and the queue is {}".format(currentNumber,queue))


print("the queue is now empty")