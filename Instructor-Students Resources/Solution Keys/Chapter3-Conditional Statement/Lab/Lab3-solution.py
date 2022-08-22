#Lab3

#Problem1
#-  Write a Python program that accepts both positive numbers and negative numbers. This program will prompt the user to enter a number and then checks it whether it is valid or not. A valid number:
#o  Only contains digits
#o  Does not start with digit 0
#o  If it is negative the first character is –
#o  If it is positive there is no + sign before the first digit

stringNumber = input("Please enter a positive or negetive number: ")

if stringNumber=="0":
    print("Input number is not accepted")
else:
    firstCharacter = stringNumber[0]
    if firstCharacter=="+":  #positive number
        print("Input number is not accepted")
    elif firstCharacter=="-":  
        #negative number 
        unsignedNumber = stringNumber[1:len(stringNumber)]
    elif (firstCharacter!="-" and firstCharacter!="+"):
        #positive number with no sign
        unsignedNumber = stringNumber
        
    if unsignedNumber.isdigit():
        print("It is a valid number")
    else:
        print("It is a wrong number")


#Problem2
#-  Write a python program which receives three positive numbers from the user and checks whether there is a perpendicular triangle whose side’s lengths are the numbers the user has entered. 

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

from math import sqrt
VERY_LITTLe_NUMBER = 0.000001
condition1 = abs(num1-sqrt(num2**2+num3**2)) <= VERY_LITTLe_NUMBER
condition2 = abs(num2-sqrt(num1**2+num3**2)) <= VERY_LITTLe_NUMBER
condition3 = abs(num3-sqrt(num1**2+num2**2)) <= VERY_LITTLe_NUMBER

if condition1 or condition2 or condition3:
    print("The entered number can form a perpendicular triangle")
else:
    print("The entered number can NOT form a perpendicular triangle")


#Problem3
#-  Write a python program which receives a word from the user and checks whether the input word is an acceptable name for a variable in Python. (No need to check the Camel Case format).
#-  An acceptable variable name 1- only contains digits and alphabet and underscore 2-It does not start with a number 3- It has at least one character

identifier = input("Please enter the potential name for the identifier: ")

notValid1 = len(identifier)==0
notValid2 = not notValid1 and (identifier[0] in "0123456789")
notValid3 = not notValid2 and not identifier.isalnum() and ("_" not in identifier)

if notValid1 or notValid2 or notValid3:
    print("Not a valid variable name in Python")
else:
    print("It is a valid name for a variable or constant in Python")
    
    
#Note: This solution does not check whether the format of the name is camelCase or not for variable and all UPPER_CASE for constants

#Problem4
#-  Write a python program which receives a word from the user and checks whether the input word is an acceptable name for a constant in Python. 
#-  An acceptable constant name in Python is all upper case and could contain an underscrore.





#Problem5
#-  The table below shows the provincial tax bracket in British Columbia, Canada in 2022. Prompt the user to enter a number that represents the total salary of a person and calculates how much tax s/he will pay in his highest tax bracket. 


