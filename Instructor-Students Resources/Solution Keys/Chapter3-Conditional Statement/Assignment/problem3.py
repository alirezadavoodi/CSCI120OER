# Write a Python program which asks the user to enter two numbers called number1 and number2 
# and then prints the number that is bigger. For instance if the user has entered 10 and 15, 
# the program prints the bigger number that 15. Do not use the max function for this question. 
# Use if-else to find the maximum of the 2 numbers.

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

if number1 > number2:
    print("number1 is greater than number2")
elif number1 == number2:
    print("two number is equal")
else:
    print("number2 is greater than number1")