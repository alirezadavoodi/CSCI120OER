
# Introduction to Computer Science and Programming 1
# Assignment 2

# Note: There is a lot of room to improve these code in terms of input validation and other checks. But it is not required to be done for this assignment.
# Note: The following solutions are one way to answer the questions in the assignments. You might have different solutions. As long as they generate correct resutls it would be fine for this assignment.

# Problem 1

print("Problem1--------------------------------------------")
# approach1
print("5+10-15 is %d" % (5 + 10 - 15))
# approach2
a = 5 + 10 - 15
print("5+10-15 is %d" % a)

# approach1
print("5 to the power of 5 is %d" % (5**5))
# approach2
a = 5**5
print("5 to the power of 5 is %d" % a)

# approach1
print("abs(-5)*6+4*3 is %d" % (abs(-5) * 6 + 4 * 3))
# approach2
a = abs(-5) * 6 + 4 * 3
print("abs(-5)*6+4*3 is %d" % a)

# approach1
print("15/4//5 is %d" % (15 / 4 // 5))
# approach2
a = 15 / 4 // 5
print("15/4//5 is %d" % a)


print("Problem2--------------------------------------------")
# Calculates and prints the maximum of the numbers: 12, -1, 0, 34, 18, 24, 9, 99, 101, -101
max = max(12, -1, 0, 34, 18, 24, 9, 99, 101, -101)
print("max(12, -1, 0, 34, 18, 24, 9, 99, 101, -101)=%d" % max)

# Calculates and prints the minimum of the numbers: 12, -1, 0, 34, 18, 24, 9, 99, 101, -101
min = min(12, -1, 0, 34, 18, 24, 9, 99, 101, -101)
print("min(12, -1, 0, 34, 18, 24, 9, 99, 101, -101)=%d" % min)

# Rounds the number 12.13456 to 2 decimal digits and prints the result
rounded = round(12.13456, 2)
print("round(12.13456, 2) = %.2f" % 12.13456)

# Rounds the number 12.683212 to 1 decimal digits and prints the result
rounded = round(12.683212, 1)
print("round(12.683212, 1) = %.1f" % 12.683212)

# Calculates the floor division of 40 over 7
floorDivision = 40 // 7
print("40//7 = %d" % floorDivision)


# Coverts the floating point 12.455 to an integer and prints it
number = int(12.455)
print("int(12.455) = %d" % number)

print("Problem3--------------------------------------------")
# prints * for 500 times with no space between the *
stars = 500 * "*"
print("* for 500 times is %s" % stars)

# Converts the number 152 to string “152”
string = str(152)
print("String of 152 is %s" % string)

# Converts the floating point 145.34 to string “145.34”
string = str(145.34)
print("String of 145.34 is %s" % string)

# Converts the string “456” to number 456
number = int("456")
print("int of the string 456 is %d" % number)

# Converts your name to lower case and prints it. For instance if your name is “Ali” the program should convert to lowercase and print “ali”.
name = "Ali"
lowerCaseName = name.lower()
print("lowercase of %s is %s" % (name, lowerCaseName))


print("Problem4--------------------------------------------")
# Write a Python program that prompts (ask) the user to enter his/her name and age.
# The Python code receives the age from the input (user) and prints the following message:
# (for example, if the user has entered James and 21)
# Hi James, your age is 21 years.

name = str(input("Hi User! Please enter your name:"))
ageString = str(input("Please also enter your age:"))
age = int(ageString)
print("Hi %s, your age is %d" % (name, age))


print("Problem5--------------------------------------------")
# Write a Python program which asks the user to enter two numbers called number1 and number2 and then prints the number that is
# bigger. For instance if the user has entered 10 and 15, the program prints the bigger number that 15.

number1 = int(str(input("Please enter a number: ")))
number2 = int(str(input("Please enter a number: ")))
print("The bigger number is %d" % max(number1, number2))


print("Problem6--------------------------------------------")
# Write a Python program which prompts(asks) the user to enter three numbers A and B and X and calculates
# and prints the result of the following math function:
# A^X+X^B
A = int(str(input("Please enter a number A: ")))
B = int(str(input("Please enter a number B: ")))
X = int(str(input("Please enter a number X: ")))

f = A**X + X**B
print("The result of A**X+X**B for A=%d B=%d X=%d is %d" % (A, B, X, f))
