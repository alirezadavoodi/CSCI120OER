# Write a Python function which receives 3 lists as its input parameters and combines the lists 
# and remove repeated numbers from the combined list and return the combined list. For instance, 
# if the input is [1,2,3,4,2,3] and [3,4,6,7] and [-1,0,23,4] the result is [1,2,3,4,6,7,-1,0,23]
# Note, the order the lists are combined together does not matter. 

def combineLists(list1, list2, list3):

    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    setunion = set1.union(set2).union(set3)

    list = []
    for item in setunion:
        list.append(item)
    return list

result = combineLists(
    [1,2,3,4,2,3],
    [3,4,6,7],
    [-1,0,23,4]
)

print(result)
