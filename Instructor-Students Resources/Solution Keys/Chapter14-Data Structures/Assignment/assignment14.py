#Problem1
'''
-   Problem1.1: Write a function which receives a list of integers and a number and does liner search to find the number. The function returns True if it finds the number, otherwise it will return False.
-   Problem1.2: Write a function which receives a list of integers and a number and does a binary search to find the number. The function returns if it finds the number, otherwise it will return False.
-   Problem1.3: Slightly change your implementation in problem 1.1 and problem 1.2 to count any time your algorithm makes a comparison. How many comparisons is made in each of the above algorithms (Linear search and binary search)
-   Problem1.4: Try the Problem 1.3 for several lists with different sizes and compare the results.

'''
#ref: https://www.programiz.com/dsa/merge-sort
def linearSearch(myList, number):
    
    comparisionCounter=0
    for i in range(0, len(myList)):
        if myList[i]==number:
            comparisionCounter=comparisionCounter+1
            return (i,comparisionCounter)
        else:
            comparisionCounter=comparisionCounter+1
            
    return (-1,comparisionCounter)
    

#reference: https://www.geeksforgeeks.org/python-program-for-binary-search/    

def binarySearch(arr, low, high, x, comparisionCounter):
    
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            comparisionCounter = comparisionCounter+1
            return (mid,comparisionCounter)
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            comparisionCounter = comparisionCounter+1
            return binarySearch(arr, low, mid - 1, x, comparisionCounter)
 
        # Else the element can only be present in right subarray
        else:
            comparisionCounter = comparisionCounter+1
            return binarySearch(arr, mid + 1, high, x, comparisionCounter)
 
    else:
        # Element is not present in the array
        return (-1,comparisionCounter)
        
def search(myList, number):
    print("Linear Search:" )
    print(linearSearch(myList, number))
    
    
    print("Binary Search:" )
    comparisionCounter = 0
    myList = sorted(myList)
    print("========")
    print(myList)
    print("========")
    print(binarySearch(myList, 0, len(myList)-1, number, comparisionCounter))


'''
Problem2
-   Problem2.1: Write a function which receives a list of integers and does bubble sort to sort the list The function returns the sorted list.
-   Problem2.2: Write a function which receives a list of integers and does merge sort to sort the list The function returns the sorted list.
-   Problem2.3: Slightly change your implementation in problem 2.1 and problem 2.2 to count any time your algorithm makes a comparison. How many comparisons is made in each of the above algorithms (Bubble sort and Merge sort)
-   Problem2.4: Try the Problem 2.3 for several lists with different sizes and compare the results.
'''

def bubbleSort(myList):
    counter = 0
    length = len(myList) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            counter = counter+1
            if myList[i] > myList[i+1]:
                sorted = False
                myList[i], myList[i+1] = myList[i+1], myList[i]
            
    return (myList,counter)



def mergeSort(array, counter):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L, counter)
        mergeSort(M, counter)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            counter = counter+1
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            counter = counter + 1
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            counter = counter + 1
            array[k] = M[j]
            j += 1
            k += 1
            
        return counter

'''
Problem3
For each of the following scenarios, specify what data structure would you use to implement the scenario.

1.  People staying in the line to submit their passport applications
2.  You need to show the results of a live car racing event on the TV. At each time the result shows the rank of participants.
3.  You are putting your books in a box. When you add a book to the box you do not touch it anymore.
'''

#1: list
#2: Priority list
#3: Stack
    
def main():
    search([ 2, 3, 4, 10, 40 ], 2)
    search([ 2, 3, 4, 10, 5, 40 ], 3)
    search([ 2, 3, 4, 10, 40, 5 ], 10)
    search([ 2, 3, 4, 10, 5, 40 ], 40)
    search([ 2, 3, 4, 10, 5, 40 ], 50)

    my_list = [12, 5, 13, 8, 9, 65, 1]
    print(bubbleSort(my_list))
    
    my_list = [12, 5, 13, 8, 9, 65, 1]
    counter = 0
    print(mergeSort(my_list, counter))
    print(my_list)
    #print(counter)
    
    


        
main()