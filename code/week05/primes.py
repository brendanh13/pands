# generate primes

# Author= Brendan Heeney

primes = []
upto = 100000


for candidate in range (2,upto):
    #print(candidate)
    isPrime = True
    for divisor in primes:  #only need to check if divisable by prime
    #for divisor in range(2, candidate):    #if divisable by an int, it is not a prime number
        if (candidate % divisor == 0):
            isPrime = False     #so there is no reason to keep checking
            break
    
    if isPrime:
        primes.append(candidate)

print(primes)