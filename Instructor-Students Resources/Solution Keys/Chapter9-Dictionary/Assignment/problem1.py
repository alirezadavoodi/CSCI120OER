# Write a function which has no input parameter. 
# The function asks the user to enter numbers. 
# The user can enter repeated numbers but if the user entered a number which was already entered, 
# the function will provide an error message to the user and ask the user to enter another one. 
# The user can enter numbers as long as s/he has not entered 0. Once a 0 is entered, the function 
# returns the sum of all distinct numbers the user had entered. 

def totalSumOfDistinctNumber():

    number = int(input("Please enter a number [Enter 0 to terminate]: "))

    numbersSet = set()

    while number != 0:

        if number in numbersSet:
            number = int(input("The number exists, please enter another one [Enter 0 to terminate]: "))
        else:
            numbersSet.add(number)
            number = int(input("Please enter a number [Enter 0 to terminate]: "))

    totalSum = sum(numbersSet)
    return totalSum

sumValue = totalSumOfDistinctNumber()
print("The sum is: %d" %sumValue)