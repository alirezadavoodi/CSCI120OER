#Problem1
#- Write a program and ask the user to enter 4 numbers. Then do the following:
#o Add all those numbers together and print the result
#o Find the number which is the biggest between the 4 numbers
#o Print all numbers in one line (they all to be printed in a single line)

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))
number4 = int(input("Please enter the forth number: "))

totalSum = number1+number2+number3+number4

print("The total sum of %d and %d and %d and %d is %d" %(number1, number2, number3, number4, totalSum))

maximum = max(number1, number2, number3, number4)
print("max(%d,%d,%d,%d)=%d" %(number1, number2, number3, number4, totalSum))

print(number1)
print(number2)
print(number3)
print(number4)

print("%d %d %d %d" %(number1, number2, number3, number4))

print(number1, end=",")
print(number2, end="*")
print(number3, end=",")
print(number4, end="")




