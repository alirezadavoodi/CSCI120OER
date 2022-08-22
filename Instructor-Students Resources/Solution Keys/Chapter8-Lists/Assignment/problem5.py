# Write a Python function which receives 2 lists as its input parameters and checks whether one of 
# the list is included in another input list. A list A is considered to be included in List B, if all elements in A are elements in B.

def isSubset(list1, list2):
    for item1 in list1:
        if not item1 in list2:
            return False
    return True

def checkSubset(list1, list2):
    if isSubset(list1, list2) or isSubset(list2, list1):
        return True
    else:
        return False

print(checkSubset([1, 2, 3, 7], [1, 2, 3, 4, 5, 6]))