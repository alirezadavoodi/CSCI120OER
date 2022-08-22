# Write a python program which prints the following multiplication table. 
# (You do not need to draw the vertical and horizontal lines).

for i in range(1, 11):
    for j in range(1, 11):
        value = i * j
        print("%4d" %value, end="")
    print("")