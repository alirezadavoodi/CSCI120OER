
def main():
    #calculateTotalSumAndAverage()
    #sumOfDigits(123)
    #sumOfDigits(5901)
    #findNextPrime(10)
    #floorDivision(20,4)
    #reverseNumber()
    #findNumbersWithConditions(10,40)
    #convertToBinary(1024)
    #findDistance()
    #drawMultipicationTable(4)
    #checkReverse("abba")
    #checkReverse("aBba")
    checkIfStatementIsValid("(a+b)*(a/d-(a/b))")
    checkIfStatementIsValid("(a+b)*(a/d-a/b))")
    
#Assignment 5 - Problem1
#- Design and implement a function with no input parameters. The function keeps receiving
#a number from input (user) and adds the numbers together. The application keeps doing it
#until the user enter 0. Then the application will stop and print the total sum and average
#of the numbers the user had entered.

def calculateTotalSumAndAverage():
    totalSum = 0
    count = 0
    number = int(input("Enter a positive or negative number: "))
    
    while number!=0:
        totalSum = totalSum + number
        count = count + 1
        number = int(input("Enter a positive or negative number: "))
        
    if count>0:
        ave = totalSum/count
        print("The total sum is %d and average is %f" %(totalSum, ave))
    else:
        print("No valid number has been entered!")

    


#Assignment 5 - Problem2
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



#Assignment 5 - Problem3
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


#Assignment 5 - Problem4
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



#Assignment 5 - Problem5
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
    

#Assignment 5 - Problem6
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



#Assignment 5 - Problem7
#- Write a function with a parameter which is a positive number in base 10 (any positive,
#non-decimal number, like 452), and converts it to binary and prints the results. (Please
#research yourself on how to convert a number in base 10 to a binary number). The
#function does not return anything.

def convertToBinary(number):
    #5 -> 101
    #5//2 = 2
    #5%2 = 1*
    
    #2//2 = 1
    #2%2 = 0*
    
    #1//2=0
    #1%2 = 1*
    
    binaryString = ""
    copy = number
    while number!=0:
        div = number//2
        rem = number%2
        number = div
        binaryString = str(rem) + binaryString
    
    print("Binary of %d is %s" %(copy, binaryString))


#Assignment 5 - Problem8
#- Write a function with no input parameter which keeps asking the user to enter positive
#numbers until the user enters an invalid input. (An invalid input is an input which
#includes at least one alphabet, like 123d4). The program should print the Max and Min of
#the numbers the user had entered as well as the distance between the Max and Min.
#(Remember to calculate the absolute distance). The function does not return anything.

def findDistance():
    
    inputNumber = input("Enter a number: ")
    if inputNumber.isdigit():
        maximum = int(inputNumber)
        minimum = int(inputNumber)
    while inputNumber.isdigit():        
        if int(inputNumber)>=maximum:
            maximum = int(inputNumber)
        if int(inputNumber)<=minimum:
            minimum = int(inputNumber)
            
        inputNumber = input("Enter a number: ")
    
    print("Max=%d and Min=%d and distance is %d" %(maximum, minimum, maximum-minimum))    

#Assignment 5 - Problem9
#- Write a function with a parameter called A (which is between 1 and 10) and prints the
#multiplication table for 1 to A.
#• Note: Do not need to draw the horizontal and vertical lines.
#• Example for A = 10


def drawMultipicationTable(number):
    print("%7s" %(""), end="")
    for i in range(1, number+1):
        print("%7d" %(i), end="")
    print()
    
    for i in range(1, number+1):
        print("%7d" %(i), end="")
        for j in range(1,number+1):
            print("%7d" %(i*j), end="")
        print()
    

#Assignment 5 - Problem 10
#Write a function with one input parameter which is a string and does the following:
#• Checks whether the input string and the its reverse is the same (like BaBa), if yes
#it return 1 and if false, it returns 0. It considers case-sensitivity which means
#(Baba and BaBa are not the same)

def checkReverse(word):
    reversedWord = ""
    for i in range(len(word)-1, -1, -1):
        reversedWord = reversedWord + word[i]
    
    if word==reversedWord:
        print("the %s is the same as its reverse which is %s" %(word, reversedWord))
    else:
        print("the %s is not the same as its reverse which is %s" %(word, reversedWord))


#Assignment 5 - Problem11
#Write A function with an input parameter which is a string arithmetic statement which
#contains only alphabet variables and binary operations including +, -, *, / and % and
#checks whether the statement is a valid arithmetic statement or not. If the statement is
#valid, the function returns true, otherwise returns false.
#• The statement might contain parenthesis as well. For instance:
#• a+b*a+c/c%y
#• (a+b)*(a/d-(a/b))
#• You can make this assumption that the variable names contain only one alphabet
#(like a, b, c) and cannot have more than one alphabets (like ab, temp, sum, …)
#• Remember from the lecture that 2 conditions should be satisfied in order an
#arithmetic operation is considered valid. Search in your lecture notes for it if you
#don’t remember it.

def checkRule1(statement):
    closeP = 0
    openP = 0
    for character in statement:
        if character=="(":
            openP = openP + 1
        elif character==")":
            closeP = closeP + 1
    
    if openP==closeP:
        return True
    else:
        return False
    
def checkRule2(statement):
    closeP = 0
    openP = 0
    
    for i in range(len(statement)):
        if statement[i]==closeP:
            closeP = closeP + 1
        if statement[i]==openP:
            openP = openP+1
        
        if closeP>openP:
            return False
    
    return True
    
def checkIfStatementIsValid(statement):
    if checkRule1(statement) and checkRule2(statement):
        print("The statement is valid")
    else:
        print("The statement is not valid")
main()