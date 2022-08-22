#Problem3
#- Design and implement a function which receives two input parameters 1) a list of integer
#numbers and 2) a number. The function will find any occurrence of the given input
#number in the list and remove the number from the list and finally will return the new list. 

#assumption1: The solution needs to keep the original order of the numbers in the list
#list = [1,2,3,6,9,4,5,5,0,0,-1] remove all 0
# newList = [1,2,3,6,9,4,5,5,-1] order is the same
# newList = [1,3,2,9,6,4,5,5,-1]

def removeAllOccurences(numbers, item):
    
    newList=[]
    for element in numbers:
        if element!=item:
            newList.append(element)
    #print(newList)
    return newList

def main():
    result = removeAllOccurences([1,2,3,6,9,4,5,5,0,0,-1], 0)
    print(result)
    
main()

    
