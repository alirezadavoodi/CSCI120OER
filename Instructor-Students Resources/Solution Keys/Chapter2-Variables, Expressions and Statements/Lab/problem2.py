# Write a Python program which asks the user to enter four numbers called X1, X2, X3 and X4 and 
# calculates the following:
# Maximum (X1, X2, X3, X4) – Minimum (X1, X2, X3, X4) + X1^X2 + abs(X3-X4)

x1 = int(input("enter the number for x1: "))
x2 = int(input("enter the number for x2: "))
x3 = int(input("enter the number for x3: "))
x4 = int(input("enter the number for x4: "))


result = max(x1, x2, x3, x4) - min(x1, x2, x3, x4) + pow(x1, x2) + abs(x3-x4)
print("the result is: %d" %result)