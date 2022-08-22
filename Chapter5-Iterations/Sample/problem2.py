# Write a Python program that finds all prime numbers between 3 and 200. 

for num in range(3, 200):
    # we should check whether the num is prime
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    
    if prime:
        print("the number is prime %d" %num)