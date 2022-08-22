# Write a Python program which keeps asking the user to enter a name. The program checks the entered name. 
# If the entered name contains any digit, then the program terminates, 
# if the entered name has no digits and only contains alphabets, 
# then converts the name to uppercase and prints it and asks for the next name from the user and repeats.  

while True:
    name = input("Enter a name: ")
    if name.isalpha() == True:
        print(name.upper())
    else:
        break