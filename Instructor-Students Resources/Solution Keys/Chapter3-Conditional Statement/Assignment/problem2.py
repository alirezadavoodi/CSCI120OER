# Write a Python program which prompts (asks) the user to enter a number between 0 and 10. 
# If the user entered a number that is less than 0 or greater than 10, the number is invalid. 
# If the number is valid, then the program prints as many “Hello” word as the number the user had entered. 
# For instance if the user entered 3 then the program should print Hello 3 times: Hello Hello Hello.

number = int(input("Enter a number between 0 and 10: "))

if number < 0 or number > 10:
    print("The number is invalid")
else:
    print("Hello "*number)