# messing with Dict


car = {
    "make" : "ford",
    "model" : "mondeo",
    "year" : 2006,
    "owner" : {
        "name" : "Brendan",
        "driver-number" : 123
    }
}

print(car["owner"]['name'])