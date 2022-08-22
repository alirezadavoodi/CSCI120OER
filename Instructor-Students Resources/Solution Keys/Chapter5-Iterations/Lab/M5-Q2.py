#Sample Problem2
#-	Write a Python program that finds all prime numbers between 3 and 200. 

#7 -> 1 and 7 
#7%2 ==0 ?
#7%3 ==0 ?
#7%4 ==0 ?
#7%5 ==0 ?
#7%6 ==0 ?

for number in range(3,201):
    
    isPrime = True
    for item in range(2,number):        
        if number % item == 0:
            isPrime = False
    if isPrime==True:
        print("%d is prime" %(number))
