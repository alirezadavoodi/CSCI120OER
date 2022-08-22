# Write a Python program which prompts(asks) the user to enter three numbers A and B
# and X and only if A is greater than B and less than X, then calculates and prints the result
# of the following math function otherwise prints 0.
# A^X+X^B
# ^ means exponent: 2^3 means 2*2*2 = 8

numberA = int(input("Please enter number A: "))
numberB = int(input("Please enter number B: "))
numberX = int(input("Please enter number X: "))

if numberA > numberB and numberA < numberX:
    ax = numberA**numberX
    xb = numberX**numberB
    result = ax + xb
    print("the result is: %d" %result)