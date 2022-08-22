#Problem3
#-	Write a Python program that count how many numbers between 100 and 999 exists whose total sum of its digit is less than 15 and bigger than 10 (including 10 and 15).

#231-> 2+3+1 = 6
#867-> 8+6+7 = 21
#536 -> 5+3+6 = 14

#536 
#536 // 10 = 53  div
#536 % 10 = 6 rem

#53 // 10 = 5
#53 % 10 = 3

#5 // 10 = 0
#5 % 10 = 5

LOWER = 10
UPPER = 15

for number in range(100, 1000):
    
    totalSum = 0
    originalNumber = number
    while number//10 != 0:
        div = number // 10
        rem = number % 10
        
        totalSum = totalSum + rem
        number = div
    
    rem = number % 10
    totalSum = totalSum + rem
    
    if totalSum>=LOWER and totalSum<=UPPER:
        print("Total sum of the digits of number %d is %d" %(originalNumber, totalSum))