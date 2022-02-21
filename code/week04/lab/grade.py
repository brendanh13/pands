# This is Week 4 - Lab 1

# Topic is if, elif, else:

# Author: Brendan Heeney

# This program reads in a students % grade 
# and prints out corresponding grade


percentage = float(input("enter the percetage: "))


if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40: 
    print ("Fail")
elif percentage < 50: # between 40 and 49
 print ("Pass")
elif percentage < 60: # between 50 and 59
 print ("Merit1")
elif percentage < 70: # between 60 and 69
 print ("Merit2")
else: 
 print ("Distinction")