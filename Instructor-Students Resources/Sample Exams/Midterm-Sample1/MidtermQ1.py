#Problem1: Coding (10 points)
#Suppose a list of positive numbers is given like the following list (remember this is only an example
#and the list could be any list of positive numbers)
#exampleList:
#15 19 10 11 8 7 3 3 1
#We would like to know the “prime visibility” of each index of the list. The “prime visibility” of a
#given index shows how many numbers in the list with indexes lower than the given index are prime.
#For instance, in the examplList, the “prime visibility” of the index 4 is 2 because there are 2 numbers
#(19 and 11) before index 4 that are prime.
#To solve this problem, design and implement a function called primeVisibility with two parameters:
#1- The list of numbers
#2- The index
#The function finds and returns the “prime visibility” of the given index.

def isPrime(number):
    
    for i in range(2, number):
        if number%i==0:
            return False
    return True

def primeVisibility(listOfNumbers, index):
    
    primeCounter = 0
    for i in range(0,index):
        if isPrime(listOfNumbers[i]):
            primeCounter = primeCounter + 1
    return primeCounter

def main():
    
    numbers = [15, 19, 10, 11, 8, 7, 3, 3, 1]
    
    for i in range(len(numbers)):
        pv = primeVisibility(numbers, i)
        print("Prime Visibility for index %d is %d" %(i, pv))
        
    dict1 = {"2":1, "3":4}
    dict2 = {"2":1, "3":5}
    
    if dict1 == dict2:
        print("equal")
    else:
        print("not equal")


 
main()
