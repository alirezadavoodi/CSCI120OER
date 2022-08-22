#Sample Problem 1
 #-	Write a Python program that asks the user to enter numbers until the user enters 0. 
 #The program checks whether the user has entered the number in ascending order or not.
 
number1 = int(input("enter a number: "))
if number1==0:
 print("The user has not entered any number!")
else:
 number2 = int(input("enter a number: "))
 if number2==0:
  print("The user entered the numbers ascendingly!")
 else:
  
  flag = True #shows whether the numbers have been entered ascendingly
  while number2!=0:
   if number2 < number1:
    flag = False
   
   number1 = number2
   number2 = int(input("enter a number: "))
  
  if flag:
   print("The user entered the numbers ascendingly!")
  else:
   print("The user has not entered the numbers ascendingly!")
 
 
   
 
 