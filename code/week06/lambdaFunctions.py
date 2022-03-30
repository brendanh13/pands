# Anonymous Functions
# Author: Brendan Heeney

def doubler (num):
    return num * 2

def tripler (num):
    return num * 3

#var = doubler(10)
#print (var)

fun = tripler

var = fun(10)
print (var)


# Using Lambda - function without a name

# Format for Lambda; lambda then the argument(s) followed by a colon followed by what is returned

isMax = False
if isMax:
    fun = lambda num : num * 2
else:
    fun = lambda num : num * 3

var = fun(10)
print (var)

# Sorted

list = [22, 13, 45, 6, 1000]
print (list)
newList = sorted(list)
print(newList)

# Another Lambda Example

data = [{'first': 'Annie', 'YOB': '2019'}, {'first': 'Brendan', 'YOB': '1985'}, {'first': 'Kate', 'YOB': '2021'}, {'first': 'Aoife', 'YOB': '1985'}]

newData = sorted(data, key = lambda item : item['YOB'])
for item in newData:
    print (item)