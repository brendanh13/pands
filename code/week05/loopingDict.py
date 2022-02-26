# Loops with Dict


car = {
    "make" : "fiat",
    "model" : "punto",
    "price" : 10000,
    "year" : 2020,
    "tags" : ["Pre-Owned","Best Buy","Dealer"]
}

#print(car)

#for key in car:
 #   print(key, 'has value', car[key])


for key, value in car.items():
    print(key, ' has a value ', value)