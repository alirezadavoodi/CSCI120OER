'''
Problem1
-   Write a function that receives a tuple of integers and calculate the average of the numbers in the tuple.
'''

def tupleAverage(numberTuples):
    length = len(numberTuples)
    if length>0:
        totalSum = sum(numberTuples)
        average = totalSum/length
        print("The average is %f" %(average))
        return average
    else:
        print("Tuple is empty")
        return

'''
Problem2
-   Define and implement function that could solve mathematical equation in the following format and find the value of x in the equation. 
-   Format: ax + b = c
-   Example: 2x – 5 = 8
'''

def solveEquation(equation):
    if len(equation)==3:
        a=equation[0]
        b=equation[1]
        c=equation[2]
        if a!=0:
            x = (c-b) / a
            print("The result is %f" %(x))
            return x
        else:
            print("Format not suppoerted")
            return
    else:
        print("Format not suppoerted")
        return

'''
Problem3
-   Write a function that could receive an input parameter with the information shown in table (on the left) and calculate the table on the right and returns it.
'''
 
def calculateFrequency(listOfTuples):
    dictOfTuple = dict()
    for t in listOfTuples:
        if t in dictOfTuple:
            dictOfTuple[t]=dictOfTuple[t]+1
        else:
            dictOfTuple[t]=1
            
    print(dictOfTuple)
    return dictOfTuple
        

'''
Problem4
-   Define and implement a function that receives the width and length of a rectangle and carucates the area and perimeter of the rectangle and return both area and perimeter of the rectangle and print them.
'''
def calcRectangle(width, length):
    area = width*length
    perimeter= 2*(width+length)
    print((area, perimeter))
    return (area, perimeter)


def main():
    avg = tupleAverage((2,3,4,5,6,7,8))
    solveEquation((2,-5,8))
    calculateFrequency([("a","b","c"), ("a", "b"), ("a","b","c"), ("b", "c"), ("a","b"), ("a","b","c"), ("c"), ("a","b","c"),("a","b","c"), ("a","b"),("b","c")])
    calcRectangle(5,6)
    
main()
