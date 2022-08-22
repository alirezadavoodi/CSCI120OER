
def main():
    
    print(calcAverageSTD([1,1,1,2,2,1,1,1]))
    
    print(calcPointDistance((2,3),(3,2)))
    
    print(convertTupleToList((4,5,1,2)))
    
    print(getTopStudents([("Bryan", "Hinton", 80), ("Adam", "Juarez", 76), ("Veronica", "Morley", 83), ("Harvir", "Sandhu", 75), ("Reis", "Wheeler", 83)]))
    
    print(createTuple(5))

'''
Problem1
-   Write a function which receives a list of number and calculate the average and standard deviation (std) of the numbers and returns both the average and std. 
'''

def calcAverageSTD(numbers):
    count = len(numbers)
    if count>0:
        totalSum = 0
        for num in numbers:
            totalSum = totalSum + num
        ave = totalSum/count
        
        totalSum = 0
        from math import sqrt
        for num in numbers:
            totalSum = totalSum + (num-ave)**2
        sqrtTotalSum = sqrt(totalSum)
        std = sqrtTotalSum/count #or count-1
        return(ave,std)
        
    else:
        print("The list is empty!")

'''
Problem2
Write a function which receives 2 points in the a cartesian coordination system and calculate the distance between two numbers:
Note: The image below shows the formula.
'''

def calcPointDistance(point1, point2):
    from math import sqrt
    distance = sqrt((point1[0] - point2[0])**2+(point1[1] - point2[1])**2)
    return distance
 
'''
Problem3
-   Write a function that receives a tuple of Integers as its input parameters and converts the tuple to a list and returns it.
'''

def convertTupleToList(intTuple):
    myList = []
    for item in intTuple:
        myList.append(item)
    return myList

'''
Problem4
-   The following table is given (as a sample data). Write a python function that receives such a table 
and returns a tuple containing the first name, last name and grade of the students who have received the maximum grade.

Firstname   Lastname    Grade
Bryan   Hinton  80
Adam    Juarez  76
Veronica    Morley  83
Harvir  Sandhu  75
Reis    Wheeler 83
'''

def getTopStudents(listOfTuples):
    maxGrade = 0
    for student in listOfTuples:
        if maxGrade<student[2]:
           maxGrade= student[2]
    
    topStudents = []
    for student in listOfTuples:
        if student[2]==maxGrade:
            topStudents.append(student)
    
    return topStudents

'''
#Problem 5:
#Write a function with one input parameter which is a number called size. The function
#then asks the user to enter as many words as the size. Then the function will find the
#followings and returns it as a tuple:
#- The first item in the tuple is the size
#- The second item in the tuple is the number of words whose length is less than 5
#- The third item in the tuple is the number of words which only contains upper case letters.
#- The fourth item in the tuples is the number of words which contains at least one letter in
#the word
'''

def createTuple(size):
    
    firstItem = size
    secondItem = 0
    thirdItem = 0
    forthItem = 0
    
    print("You are going to enter %d word" %(size))
    for i in range(size):
        word = input("Enter a word: ")
        
        if len(word)<5:
            secondItem = secondItem + 1
        if word.isupper():
            thirdItem = thirdItem + 1
        if word.isalnum():
            forthItem = forthItem + 1
    
    return (firstItem, secondItem, thirdItem, forthItem)



main()
