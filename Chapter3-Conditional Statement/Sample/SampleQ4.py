 #Problem4
#-	Write a Python program which asks the student to enter a work email address for Columbia College and checks whether the email address is valid or not. 
#-       A valid Columbia College email address has the following pattern:
#-	[username]@columbiacollege.ca
#-	The username is the student id of the student and only contains digits.

email = input("Enter an email: ")
COLLEGE_NAME = "columbiacollege.ca"

containsOneAtSign = False
containsOneDot = False
containsCCDomain = False

atSingCount = email.count("@")
dotSignCount = email.count(".")
ccCount = email.count(COLLEGE_NAME) 

if atSingCount==1:
    containsOneAtSign = True

if dotSignCount==1:
    containsOneDot = True
    
if ccCount==1:
 containsCCDomain = True

atSignIndex = email.find("@")

username = email[:atSignIndex]

isUsernameValid = username.isdigit()

if containsOneAtSign and containsOneDot and containsCCDomain and isUsernameValid:
 print("The email is valid")
else:
 print("The email is Not valid")