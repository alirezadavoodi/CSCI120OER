#Problem2
#-	 Design and implement a function which receives a number as its input parameter and checks whether the number is a prime number or not. 
         #If it is a prime number the algorithm returns true and if not the algorithm will return false. 
#-	Prime number: https://simple.wikipedia.org/wiki/Prime_number

def isPrime(number):
         
         for i in range(2, number):
                  if number%i == 0:
                           print("%d is not Prime" %(number))
                           return False
         print("%d is prime" %(number))
         return True

def main():
         isPrime(97)
         isPrime(111)

main()