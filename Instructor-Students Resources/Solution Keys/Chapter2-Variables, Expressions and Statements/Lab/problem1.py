# Write a Python program which asks the user to enter two numbers called X and Y and calculates the following:
# F(X,Y) = X*Y + Y^2 + abs(X-Y) where ^ is the power operation
# Find A such that the following equation holds: X^2+Y^3-A = 5 

x = int(input("enter the number for the x: "))
y = int(input("enter the number for the y: "))

result = (x*y) + (y*y) + abs(x-y)

#print("print x: %d" %x)
#print("print y: %d" %y)
print("the result is: %d" %result)