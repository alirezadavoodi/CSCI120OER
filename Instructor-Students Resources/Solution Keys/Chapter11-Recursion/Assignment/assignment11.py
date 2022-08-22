'''
Problem1
-   Write a function which receives an integer (n) and calculate the total sum of 1 until n recursively. For instance function(5) = 5+4+3+2+1 = 15
'''

def totalSum(n):
    if n==0:
        return 0
    else:
        return n+totalSum(n-1)

'''
Problem2
-   Define and implement a function that receive an integer and return the sum of all digits of the number. For instance, for number 3415 the function should return 3+4+1+5 = 13
'''
def totalDigitSum(num):
    if num<10:
        return num
    else:
        return (num%10) + totalDigitSum(num//10)

'''
Problem3
-   Define and implement a function that print the Fibonacci series for an input number n. The following image shows the Fibonacci function.
'''
 
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
 
''' 
Problem4
-   Define and implement a function which receives a list of integers and calculate the sum of all elements of the list recursively. 
'''

def listTotalSum(myList):
    if len(myList)==0:
        return 0
    elif len(myList)==1:
        return myList[0];
    else:
        return myList[0]+listTotalSum(myList[1:len(myList)])

'''
Problem5
-   Define and implement a function which receives a list of integers and find the maximum element of the list recursively.
'''
def findMaxRecursive(myList):
    if len(myList)>0:
        if len(myList)==1:
            return myList[0];
        else:
            return max(myList[0], findMaxRecursive(myList[1:len(myList)]))


def main():
    print(totalSum(5))
    print(totalDigitSum(123))
    print(fibo(1))
    print(fibo(16))
    print(listTotalSum([3,4,1,3]))
    print(listTotalSum([4]))
    print(listTotalSum([3,4]))
    print(findMaxRecursive([3,4,1,8]))
    print(findMaxRecursive([1]))
    print(findMaxRecursive([1,2]))
    
main()
