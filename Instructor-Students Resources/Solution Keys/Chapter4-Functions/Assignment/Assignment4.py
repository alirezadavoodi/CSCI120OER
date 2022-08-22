
def main():
    #sumOfDigits(123)
    #sumOfDigits(5901)
    #findNextPrime(10)
    #floorDivision(20,4)
    #reverseNumber()
    #findNumbersWithConditions(10,40)
    
#Problem1
#- Design and implement a function with an input parameter which is a positive number and
#prints and returns the sum of the number’s digits. For instance if the number is 123 the
#algorithm returns 6 which is the result of 1+2+3.

def sumOfDigits(number):
    #123 -> 1+2+# = 6
    #123//10 = 12
    #123%10 = 3
    
    #12//10 = 1
    #12%10 = 2
    
    #1//10 = 0
    #1%10 = 1
    
    copy = number
    totalSum = 0
    while number>0:
        dev = number//10
        rem = number%10
        totalSum = totalSum + rem
        number = dev
       
    print("sum of %d is %d" %(copy, totalSum))



#Problem2
#- Design and implement a function with one parameter which is an integer and finds the
#next prime number which is bigger than the given input parameter and returns it.

def isPrime(number):
    totalDivisibility = 0
    
    for i in range(2, number):
        if number%i==0:
            totalDivisibility = totalDivisibility + 1
    if totalDivisibility>0:
        return False
    else:
        return True
    
def findNextPrime(number):
    copy = number
    number = number + 1
    while not isPrime(number):
        number = number + 1
    print("The next prime number bigger than %d is %d" %(copy, number))


#Problem3
#- Design and implement a function with two input parameters, A and B. The functions then
#calculates the result of the floor division of A over B (A//B). You are not allowed to use
#the floor division operator. Look at
#here: https://simple.wikipedia.org/wiki/Division_(mathematics)
#- For instance the function for 20 and 6 will return 3.

#A = 20 B = 6 -> A//B = 3
def floorDivision(a, b):
    if b!=0:
        copy = a
        counter = 0
        while a>=b:
            a = a-b
            counter = counter + 1
        print("%d//%d = %d" %(copy, b, counter))
    else:
        print("Division by Zero error")



#Problem4
#- Design and implement a function with no input parameter which reads a number from
#input (like 123). Only non-decimal numbers are valid (floating points are not valid). The
#number entered by the user should not be divisible by 10 and if the user enters a number
#that is divisible by 10 (like 560), it is considered invalid and the application should keep
#asking until the user enters a valid input. Once the user enters a valid input, the program
#calculates the reverse of the input number (for 153, the reverse is 351) and prints the
#result and returns the results.


def reverseNumber():
    number = int(input("Enter a number that is not divisible by 10: "))
    
    while number%10==0 and number!=0:
        print("The number is invalid")
        number = int(input("Enter a number that is not divisible by 10: "))
    
    #approach 1: conveting into string
    
    stringNumber = str(number) 
    #-123 -> "-123"
    #123 -> "123" ->  "3"+ "2" + "1" = "321" -> 321
    if number>0:
        reversedString = ""
        for index in range(len(stringNumber)-1, -1, -1):
            reversedString = reversedString + stringNumber[index]
        reversedNumber = int(reversedString)
        print("reverse of %d is %d " %(number, reversedNumber))
        return reversedNumber
        
    elif number<0:
        #-123 -> "-123" -> "-321" -> 321
        reversedString = "-"
        for index in range(len(stringNumber)-1, 0, -1):
            reversedString = reversedString + stringNumber[index]
        reversedNumber = int(reversedString)
        print("reverse of %d is %d " %(number, reversedNumber))
        return reversedNumber
    else:  #number is 0
        print("reverse of 0 is 0")
        return 0
    

#Problem5
#- Write a function called printSubLists which receives two number A and B as its
#parameters:

#- First prints all numbers between A and B (A and B not included), which are divisible to
#both 3 and 5.
#- Then prints all numbers between A and B (A included by B not included), which are
#divisible by either 6 or 7.
#- Finally prints all numbers between A and B (A and B both included), which are not
#divisible by 3.
#- Hint: Design a function for each sub problem and then call them inside the printSubLists
#function.

def findDivisileBoth3And5(a, b):
    for number in range(a+1,b):
        if number%3==0 and number%5==0:
            print("number %d is divisible by 3 and 5" %(number))
            

def findDivisibleEither6or7(a,b):
    for number in range(a,b):
        if number%6==0 or number%7==0:
            print("number %d is either divisible by 6 or 7" %(number))
            
def findDivisibleBy3(a,b):
    for number in range(a,b+1):
        if number%3!=0:
            print("number %d is not divisible by 3" %(number))

def findNumbersWithConditions(a,b):
    findDivisileBoth3And5(a,b)
    findDivisibleEither6or7(a,b)
    findDivisibleBy3(a,b)


main()