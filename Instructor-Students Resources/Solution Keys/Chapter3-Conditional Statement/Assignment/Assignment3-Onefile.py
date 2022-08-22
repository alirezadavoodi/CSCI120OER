#Assignment 3 - Problem1
#- Write a Python program which receives the user’s age from the input and checks whether
#the user is able to take a Driver licence test and informs the user with a proper message.
#Note: Suppose, the user is eligible to take a Driver license test if s/he is greater than 18
#years also.

print("Problem1 ===============================")
age = int(input("Please enter your age: "))
if age>18:
    print("The user is eligible to take the driver test")
else:
    print("The user is not eligible to take the driver test")


#Assignment 3 - Problem2
#- Write a Python program which prompts (asks) the user to enter a number between 0 and
#10. If the user entered a number that is less than 0 or greater than 10, the number is
#invalid. If the number is valid, then the program prints as many “Hello” word as the
#number the user had entered. For instance if the user entered 3 then the program should
#print Hello 3 times: Hello Hello Hello.

print("Problem2 ===============================")
number = int(input("Enter a number between 0 and 10: "))
if number<0 or number>10:
    print("The number is invalid")
else:
    print("Hello"*number)
             


#Assignment 3 - Problem3
#- Write a Python program which asks the user to enter two numbers called number1 and
#number2 and then prints the number that is bigger. For instance if the user has entered 10
#and 15, the program prints the bigger number that 15. Do not use the max function for
#this question. Use if-else to find the maximum of the 2 numbers.

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

if number1>number2:
    print("%d which is number 1 is bigger" %(number1))
elif number1==number2:
    print("number 1 and number 2 are equal")
else:
    #print("%d which is number 2 is bigger" %(number2))


#Assignment 3 - Problem4
#- Write a Python program which asks the user to enter a number, if the number is divisible
#by 6 and 7, the program prints “The number X is divisible by 6 and 7” and if the number
#is neither divisible by 6 nor by 7, then it prints “The number X is not divisible by 6 and
#7”.

number = int(input("Please entr a number: "))
if number%6 == 0 and number%7==0:
    print("The number %d is divisible by 6 and 7" %(number))
elif not number%6==0 and not number%7==0:
    print("The number %d is neither divisible by 6 nor 7" %(number))
else:
    print("The number %d is not divisible by 6 or is not divisible  7" %(number))


#Assignment 3 - Problem5
#- Write a Python program which asks the user to enter a number, if the number is divisible
#by 6 or 7, the program prints “The number X is divisible by 6 or 7” and if the number is
#neither divisible by 6 nor by 7, then it prints “The number X is not divisible by 6 and 7”.

number = int(input("Please entr a number: "))
if number%6==0 or number%7==0:
    print("The number %d is divisible by 6 or 7" %(number))
else:
    print("The number %d is neither divisible by 6 nor by 7")
    
#De-Morgan law
#not (number%6==0 or number%7==0:) -> not number%6==0 and not number%7==0


#Assignment 3 - Problem6
#- Write a Python program which prompts(asks) the user to enter three numbers A and B
#and X and calculates and prints the result of the following math function:
#o A^X+X^B: ^ means power

numberA = int(input("Please enter number A: "))
numberB = int(input("Please enter number B: "))
numberX = int(input("Please enter number X: "))

##A^X
ax = numberA**numberX

##X^B
xb = numberX**numberB

result = ax + xb

print("(a=%d, b=%d, x=%d and result is %d" %(numberA, numberB, numberX, result))



#Assignment 3 - Problem7
#- Write a program which ask the user to enter a GPA (like 76) and checks for following
#letter grade based on the table below and prints the proper message:
#o For instance if the user entered 70, then the program should print “You are
#Average (C+)”

#A 86–100 Message: “Your are GREAT (A)”
#B 73–85 Message: “Your are GOOD (B)”

#C+ 67-72 #Message: “Your are AVERAGE (C+)”

#C 60–66 #Message: “You need to practice more (C)”
#C- 50–59 #Message: “You need to try harder (C-)”
#F (fail) 0–4
#Message: “Unfortunately you failed (F)”

gpa = float(input("Please enter your GPA: "))

if gpa>=86 and gpa<=100:
    print("Your are GREAT (A)")
elif gpa>=73 and gpa<86:
    print("Your are GOOD (B)")
elif gpa>=67 and gpa<73:
    print("Your are AVERAGE (C+))")
elif gpa>=60 and gpa<67:
    print("You need to practice more (C)")
elif gpa>=50 and gpa<60:
    print("You need to try harder (C-)")
else:
    print("Unfortunately you failed (F)")
    
    