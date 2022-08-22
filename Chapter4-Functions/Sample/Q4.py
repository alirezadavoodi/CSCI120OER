#Problem4
#-	Design and implement a function which receives a number as its first input parameter and a format (which is either SHAPE1 or SHAPE2 or SHAPE3) as the second input 
#parameter and prints the following patterns. See the examples below:

#-	Example: number: 5 format: SHAPE1
#*****
#***
#*

#-	Example: number: 5 format: SHAPE2
#*****
#****
#***
#**
#*

#-	Example: number: 5 format: SHAPE3
#*
#**
#***
#****
#*****

def drawShape1(number):
    for i in range(number, 0, -2):
        print("*"*i)
        
def drawShape2(number):
    for i in range(number, 0, -1):
        print("*"*i)    

def drawShape3(number):
    for i in range(1, number+1):
        print("*"*i)
        
def drawShape(number, shapeFormat):
    
    if shapeFormat=="SHAPE1":
        drawShape1(number)
    elif shapeFormat=="SHAPE2":
        drawShape2(number)
    elif shapeFormat=="SHAPE3":
        drawShape3(number)
    else:
        print("Shape is not supported")
        
def main():
    drawShape(6, "SHAPE1")
    drawShape(6, "SHAPE2")
    drawShape(6, "SHAPE3")
    
main()