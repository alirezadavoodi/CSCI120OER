'''
Problem1
-   Write a function which receives a list of string and concatenates all string in the list and returns it. (recursive function)
'''

def concatinatesRecursive(strings):
    if len(strings)==0:
        return ""
    elif len(strings)==1:
        return strings[0]
    else:
        return strings[0]+concatinatesRecursive(strings[1:len(strings)])

'''
Problem2
-   Write a recursive function that receives a string and calculates all permutation of the given input string and prints them.
'''
#ref: https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
def permutations(string):
    if len(string) == 1:
        return string

    recursive_perms = []
    for c in string:
        for perm in permutations(string.replace(c,'',1)):
            recursive_perms.append(c+perm)

    return set(recursive_perms)

'''
Problem3
-   Write a recursive function that receive a number n as its input parameter and prints the following pattern. For instance, if n = 4
*
**
***
****
'''

def starTriangle(n):
    if n==0:
        return
    elif n==1:
        print("*")
    else:
        starTriangle(n-1)
        print("*"*n)
        
'''
Problem4 
-   Write a recursive function which receives an integer, n, and calculates Log n2 and returns it.
'''
def logn(n):
    if n < 2:
        return 0
    return 1 + logn(n//2)


def main():
    print(concatinatesRecursive(["A", "B", "C", "D", "E"]))
    print(permutations("ABCD"))
    starTriangle(5)
    print(logn(20))
    
main()
