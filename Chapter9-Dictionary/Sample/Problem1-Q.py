 #Problem1
#- Implement a function which receives a list of integers (numbers) as input. The list might
#have repeated numbers. The function will return the number that is repeated the most.
#You can make this assumption that only one number is repeated the most and other
#numbers are either not repeated or repeated less number of times.
#- Hint: Use a dictionary
#- Example: for this list [1,4,5,6,1,2,4,5,6,5] the function returns 5 because it is the only numbers repeated 3
#times (the most)

def findMostRepeatedNumber(numbers):
    
    dict = {}
    
    for item in numbers:
        if item in dict:
            dict[item] = dict[item]+1
        else:
            dict[item] = 1
    
    maximum = 0
    mostRepeatedNumber = -1
    for key in dict:
        value = dict[key]
        if value>=maximum:
            maximum = value
            mostRepeatedNumber = key
    
    print("number %d has been repeated %d times" %(mostRepeatedNumber, maximum))
    return mostRepeatedNumber

def main():
    #result = findMostRepeatedNumber([1,4,5,6,1,2,4,5,6,5])
    result = findMostRepeatedNumber([1,4,5,6,6,1,2,4,5,6,6,5])

main()