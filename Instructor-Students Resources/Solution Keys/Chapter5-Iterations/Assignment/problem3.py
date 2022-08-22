# Write a python program which asks the user to enter a positive number that is 
# greater than 30 called, “num2” and then does the following:
# 1) Print all numbers between 1 and “num2” that are divisible by 2 and 3.
# 2) Print all numbers between 1 and “num2” that are either divisible by 6 or 7.
# 3) Print all numbers between 1 and “num3” that is not divisible by 5.

number = int(input("Please enter a number greater than 30: "))

if number <= 30:
    print("You entered invalid number")
else:
    
    print("Divisible numbers on 2 and 3")
    for i in range(1, number):
        if i % 2 == 0 and i % 3 == 0:
            print(i)

    print("Divisible numbers on 6 or 7")
    for i in range(1, number):
        if i % 6 == 0 or i % 7 == 0:
            print(i)

    print("Non-Divislbe numbers on 5")
    for i in range(1, number):
        if i % 5 != 0:
            print(i)
