#Problem2
#- Write a function, which receives a list of integers which may or may not contains
#repeated numbers. The algorithm should return how many each item is repeated and also
#print the results.

def calculateNumbersDictionary(numbers):
    dict = {}
    
    for element in numbers:
        if element in dict:
            dict[element] = dict[element]+1
        else:
            dict[element] = 1
    
    return dict

def main():
    #dictionaryOfNumbers = calculateNumbersDictionary([2,3,3,4,1,0,1,0,0,3,-1,-2,-1])
    dictionaryOfNumbers = calculateNumbersDictionary([2])
    print(dictionaryOfNumbers)
    
main()