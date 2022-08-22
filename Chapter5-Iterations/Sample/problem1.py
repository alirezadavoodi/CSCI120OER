# Write a Python program that asks the user to enter numbers until the user enters 0. 
# The program checks whether the user has entered the number in ascending order or not. 


number = int(input("Enter a number: "))
previous = number

while number != 0:
    number = int(input("Enter a number: "))

    if number >= previous:
        print("You are in ascending order")
    else: 
        print("You are in descending order")
    previous = number
