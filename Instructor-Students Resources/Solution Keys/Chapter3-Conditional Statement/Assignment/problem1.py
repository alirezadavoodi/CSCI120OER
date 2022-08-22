# Write a Python program which receives the user’s age from the input and checks whether
# the user is able to take a Driver licence test and informs the user with a proper message.
# Note: Suppose, the user is eligible to take a Driver license test if s/he is greater than 18
# years also.

age = int(input("Please enter your age: "))

if age > 18: 
    print("The user is eligible to take the driver test")
else: 
    print("The user is not eligible to take the driver test")