# Write a Python program which asks the user to enter three number and 
# finds the absolute distance between the biggest and smallest entered numbers.

firstNumber = int(input("enter first number: "))
secondNumber = int(input("enter second number: "))
thirdNumber = int(input("enter third number: "))

minValue = min(firstNumber, secondNumber, thirdNumber)
maxValue = max(firstNumber, secondNumber, thirdNumber)

result = abs(maxValue - minValue)
print("the result value is %d" %result)