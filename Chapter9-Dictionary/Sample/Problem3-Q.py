#Problem3
#- Write a function which receives a list of integers which may contains repeated numbers.
#The function remove the repeated numbers and keeps the distinct numbers. The function
#should return the list of distinct numbers.

#list = [1,2,4,2,1,5] -> [1, 2, 4, 5]

def keepDistinctNumbers(numbers):
    mySet = set(numbers)
    newList = []
    for item in mySet:
        newList.append(item)
    
    return newList

def main():
    print([1,2,4,2,1,5])
    result = keepDistinctNumbers([1,2,4,2,1,5])
    print(result)
    
main()
    