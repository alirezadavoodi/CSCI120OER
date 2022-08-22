#Problem4
#-	Write a Python program that calculates the following mathematical function without using exponent operator (**) and calculate the value of the function for x=5, y= -2
#o	F(x,y) = x^6+(x-y)^10

x = 5
y = -2

#x^6 x*x*x...*x

pow1 = 1
for i in range(6):
    pow1 = pow1 * x

#(x-y)^10

pow2 = 1
for i in range(10):
    pow2 = pow2 * (x-y)
    
fxy = pow1 + pow2

# 5^6 + (5+2)^10
print("F(x,y) = x^6+(x-y)^10 for x=5 and y=-2 is %d" %(fxy))

print("F(x,y) = x^6+(x-y)^10 for x=5 and y=-2 is %d" %(5**6 + 7**10))