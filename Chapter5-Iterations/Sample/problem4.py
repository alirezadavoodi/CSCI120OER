# Write a Python program that calculates the following mathematical function without 
# using exponent operator (**) and calculate the value of the function for x=5, y= -2
# F(x,y) = x6+(x-y)10

x = 5
y = -2

x6 = x
xMinusY = (x-y)
xMinusY10 = xMinusY

for i in range(1, 6):
    x6 = x6 * x

for i in range(1, 10):
    xMinusY10 = xMinusY10 * xMinusY

result = x6 + xMinusY10
print("The result is: %d" %result)
