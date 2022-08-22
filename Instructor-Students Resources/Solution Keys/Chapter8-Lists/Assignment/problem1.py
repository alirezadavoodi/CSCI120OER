# Implement a function which receives a list and returns True if the list is already sorted ascendingly 
# and returns 0 if the list is not sorted ascendingly.

def isSorted(myList):
    sortedList = sorted(myList)

    if myList == sortedList:
        print("The list is already sorted!")
        return True
    else:
        print("The list is not sorted!")
        return False

print(isSorted([2, 5, 8, 9, 10]))
print(isSorted([4, 2, 6, 8]))
