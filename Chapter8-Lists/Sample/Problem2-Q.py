#Problem2
#- Define and implement a function which does linear search. This function receives two
#input parameters, one is a list of integers and the other one is a number to search for. The
#function returns -1 if the number (the second parameter of the function) does not exist in
#the list or return the index of the number if the number exists in the list.
#- If there are more than one occurrence of the number, the function will return the index of
#the first occurrence 

def linearSearch(numbers, item):
    
    for index in range(len(numbers)):
        if numbers[index] == item:
            return index
    
    return -1

def main():
    myList = [1,2,3,4,5,5,6,7,8,8,-1,10]
    index = linearSearch(myList, 20)
    if index!=-1:
        print("The item is located at index %d" %(index))
    else:
        print("The item does not exist in the list")

main()