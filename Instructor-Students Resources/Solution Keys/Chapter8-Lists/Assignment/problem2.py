# Write a function which receives a list and returns True if the list is “Partially sorted” 
# and returns False if the list is not “Partially Sorted”. A list is “Partially sorted” 
# if and only if there exists an item in the list which if removed, 
# the list will become a sorted list. For instance the following list is “Partially sorted”:
# [1,2,5,10,6,8,9] This is partially sorted because it is not originally sorted but 
# if we remove 10 from the list, then the list is sorted. 

def isSortedAsc(myList):
    sortedList = sorted(myList)
    if myList == sortedList:
        return True
    else:
        return False

def isSortedDesc(myList):
    sortedList = sorted(myList).reverse()
    if myList == sortedList:
        return True
    else:
        return False


def isPartiallySorted(myList):
    if isSortedAsc(myList) or isSortedDesc(myList):
        return False
    else:
        for i in range(len(myList)):
            newList = myList[:i] + myList[i+1:]
            if isSortedAsc(newList) or isSortedDesc(newList):
                print("Refine list is: ", end="")
                print(newList)
                return True
        return False


print(isPartiallySorted([2, 5, 8, 9, 10]))
print(isPartiallySorted([2, 5, 8, 80, 9, 10]))