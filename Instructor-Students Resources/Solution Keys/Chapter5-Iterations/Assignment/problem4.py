# Write a python program which keeps asking the user to enter a positive or a negative number until the user enters 0. 
# Once the user enters 0, the program calculates the sum and average of all the numbers the user had entered
# and prints the sum and average and terminates.

sum = 0
count = 0

while True:
    number = int(input("Please enter a number: "))

    if number == 0:
        break
    else:
        sum = sum + number
        count = count + 1

average = float(sum/count)
print("Sum is: %d" %sum)
print("The Average is: %.2f" %average)