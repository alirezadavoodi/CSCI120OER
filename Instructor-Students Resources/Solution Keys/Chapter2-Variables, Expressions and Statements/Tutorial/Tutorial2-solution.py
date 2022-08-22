#problem1

#Write a python program which asks the user to enter a number which represents the value of a circle’s 
#radius and calculates and prints the area and perimeter of the circle.

print("Problem1--------------------------------------------")
radius = float(input("Please enter the radius of the circle: "))

PI = 3.14

area = (radius**2)*PI
perimeter = 2*radius*PI

print(area)
print(perimeter)

print("For circle with radius %.2f , the area is %.2f and the perimeter is %.2f" %(radius, area, perimeter))


#problem2
#-	Write a program which asks the user who is a student about the following information:
#o	firstName
#o	lastName
#o	age
#o	name of the college
#o	studentID
#o	Number of courses the student has taken so far
#o	Admission year to the college
#-	And print an enrollment letter for the student with this format:

#********************************************* 
#program2
#Enrollment Letter for [first name] [last name]
#This is to certify that [first name] [last name], age: [age] years old, has been attending the [college name] college 
#since [Admission year to the college] and taken [Number of courses] courses since then.

#Thanks,
#College Manager

print("Problem2--------------------------------------------")

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
age = input("Please enter your age: ")
collegeName = input("Please enter the college name: ")
studentID = input("Please enter the student ID: ")
numberOfCourses = input("Please enter the number of courses: ")
admissionYear = input("Please enter the admission year: ")
NUMBER_OF_STARS = 50
CHAR = "*"


text = CHAR*NUMBER_OF_STARS+"\n"+"Enrollment Letter for "+firstName+" "+lastName+"\n"+"This is to certify that "+firstName+" "+lastName+", age: "+age+" years old, "+"\n"+"has been attending the "+collegeName+" college since "+admissionYear+" and taken "+numberOfCourses+" since then"+"\n"+"Thanks"+"\n"+"College Manager"

print(text)

#program3
#-	Write a python program which calculates the following mathematical function and prints the result:
#	F(x,y) = x^2 + sqrt(xy) - xlogxy / x+y

print("Problem3--------------------------------------------")
from math import sqrt
from math import log
x = float(input("enter x:"))
y = float(input("enter y:"))
fXY = x**2 + sqrt(x*y) - x* log(x*y) / (x+y)

print("F(%.3f,%.3f)=%.2f" %(x,y,fXY))

#program4
#-	Write a python which asks the user to enter 4 words and calculates the total length of the words 
#that have been entered as well as the max and min length of the words have been entered.
print("Problem4--------------------------------------------")
word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")
word3 = input("Please enter the third word: ")
word4 = input("Please enter the forth word: ")

word1Length = len(word1)
word2Length = len(word2)

word3Length = len(word3)
#word4Length = len(word4)

#totalLength = word1Length + word2Length + word3Length + word4Length
#maximumLength = max(word1Length, word2Length, word3Length, word4Length)
#minimumLength = min(word1Length, word2Length, word3Length, word4Length)

#print("The total length of the words %s, %s, %s and %s is %d and max length is %d and min length is %d" %(word1, word2, word3, word4, totalLength, maximumLength, minimumLength))


#program5
#-	Write a program that takes two input from the user and then exchange their values. 
#For instance if the user 5 for number1 and 10 for number2, 
#then the program exchange their values and number1 will become 10 and the number2 will become 5.

print("Problem5--------------------------------------------")
number1 = int(input("Please enter number1: "))
number2 = int(input("Please enter number2: "))

print("Original number1 and number2 are %d %d " %(number1, number2))
temp = number1
number1 = number2
number2 = temp

print("After exchange it is %d %d" %(number1, number2))