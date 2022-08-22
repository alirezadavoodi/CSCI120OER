# Write a Python program which asks the user to enter a number, if the number is divisible
# by 6 and 7, the program prints “The number X is divisible by 6 and 7” and if the number
# is neither divisible by 6 nor by 7, then it prints “The number X is not divisible by 6 and 7".


number = int(input("Please enter a number: "))

if number%6 == 0 and number%7 == 0:
    print("The number is divisible by 6 and 7")
elif not number%6 == 0 and not number%7 == 0:
    print("The number is not divisible by 6 and 7")
else:
    print("None of the conditions is met")