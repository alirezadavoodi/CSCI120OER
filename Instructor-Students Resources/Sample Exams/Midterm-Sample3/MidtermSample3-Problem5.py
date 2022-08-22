 #-	Write a Python program which asks the user to enter four names and counts the number of names which have an “ali” substring in them. 
 #The names are not case sensitive, meaning that if the user enters a name, for instance “Alison”, “aliSon”, “ALISON”, “alison”, … are considered the same 
 #and they all contain “ali” in them.

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
name3 = input("Enter the third name: ")
name4 = input("Enter the forth name: ")

SUBSTRING = "ali"
counter = 0

if name1.lower().find(SUBSTRING)!=-1:
    counter = counter + 1
    
if name2.lower().find(SUBSTRING)!=-1:
    counter = counter + 1
    
if name3.lower().find(SUBSTRING)!=-1:
    counter = counter + 1
    
if name4.lower().find(SUBSTRING)!=-1:
    counter = counter + 1
    
print("counter is %d" %(counter))

