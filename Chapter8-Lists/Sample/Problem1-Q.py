#Question1
#Write a function which take a list of number as an input parameter and find the second
#maximum of the list. The second maximum is a number which is bigger than or equal to
#all numbers but smaller than the maximum of the list. 

def findSecondMaximum(myList):
    firstMaximum = max(myList)
    print(myList)
    myList.remove(firstMaximum)
    while firstMaximum in myList:
        myList.remove(firstMaximum)
    
    print(myList)
    secondMaximum = max(myList)
    print("First Maximum is %d and Second Maximum is %d" %(firstMaximum, secondMaximum))

def main():
    list1 = [1,2,3,4,4,5,6,7,8,8,8]
    findSecondMaximum(list1)
    
main()