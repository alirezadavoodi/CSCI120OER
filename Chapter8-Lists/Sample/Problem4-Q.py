#Problem4
#- Implement a function which receives a list of numbers as an input parameter. The
#function will find a sub-list from the list which is sorted and its length is greater than 4
#and return the sub-list. If there are more than 1 sub-list, the function can return only one
#of them. If there is no such sub-list in the list, the function will return None.

list1 = [1,3,2,9,6,4,3,2,5,5,-1]

def function(list1):
    if len(list1)>=4:
        while True:
            for size in range(4, len(list1)):
                for startIndex in range(len(list1)-size):
                    subList = list1[startIndex:startIndex+size]
                    if subList==sorted(subList) or subList==sorted(subList, reverse=True):
                        return subList
            
            return None            
        
    else:
        return None

print(function(list1))
    
