# Write a function which receives a list and returns a number. 
# In the list, all numbers have been repeated twice except one number that is repeated once. 
# The function should return the number that is repeated once and return it.

def findSingleItem(list):

    numberDictionary = { }

    for number in list:
        if number in numberDictionary:
            numberDictionary.pop(number)
        else:
            numberDictionary[number] = 1

    print(numberDictionary)

    return sorted(numberDictionary)[0]

result = findSingleItem([1,1,2,3,3,4,4])
print(result)



