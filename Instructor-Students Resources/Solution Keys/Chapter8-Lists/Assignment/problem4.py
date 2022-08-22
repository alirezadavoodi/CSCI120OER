# Write a python function which receives 2 mathematical equations and adds these two equations 
# and prints and retunes the result. The mathematical equations that are inputs of this function 
# have the following format / specifications:
# The maximum degree of the equation is 10.
# The equation can have only 2 variables: X and Y.
# The syntax of the equation is like: Example: X^4+ 5X^2 + Y^3+Y^2+1
# Only use lists to solve this problem


def sum(xList1, yList1, xList2, yList2):
    if len(xList1) != 10 or len(yList1) != 10 or len(xList2) != 10 or len(yList2) != 10:
        print("Invalid list length")
    else:
        for i in range(0, len(xList1)):
            if i == 0:
                print("%d" %(xList1[i] + yList1[i] + xList2[i] + yList2[i]), end=" ")
            else:
                print("+ %dX^%d + %dY^%d" %(xList1[i] + xList2[i], i, yList1[i] + yList2[i], i), end = " ")
        print("")

sum(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
)
