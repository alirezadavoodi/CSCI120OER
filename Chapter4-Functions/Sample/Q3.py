#Problem3
#Design and implement a function with one parameter which is an integer and finds the next prime number which is bigger than the given input parameter and returns it. 
#Reuse (call) the function you have defined for Problem 3.

def isPrime(number):

    for i in range(2, number):
        if number%i == 0:
            print("%d is not Prime" %(number))
            return False
    print("%d is prime" %(number))
    return True


def nextPrime(number):
    
    temp = number+1
    while not isPrime(temp):
        temp = temp + 1
    
    print("%d is a number bigger than %d and is prime" %(temp, number))
    return temp

def main():
    nextPrime(3401)
    
main()