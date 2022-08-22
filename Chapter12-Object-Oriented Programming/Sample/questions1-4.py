#Problem 0
#-	Create a Cricle class and initialize it with radius. Make two instance methods 
#getArea and getCircumference inside this class. Implement the methods.

class Circle:
    
    PI = 3.14
    def __init__(self, r):
        self._radius = r
        
    
    def getArea(self):
        return Circle.PI*self._radius*self._radius
    
    def getCircumference(self):
        return 2*Circle.PI*self._radius
    
    
    
class TestCircle:
    def test():
        print("hello")
        circle1 = Circle(10)
        circle2 = Circle(5)
        
        area1 = circle1.getArea()
        circ1 = circle1.getCircumference()
        print("Circle1: Area=%f Circ=%f" %(area1, circ1))
        
        area2 = circle2.getArea()
        circ2 = circle2.getCircumference()
        print("Circle2: Area=%f Circ=%f" %(area2, circ2))
 

#Problem1:
#-	Create a Temprature class. Make two class/static methods :
#1. convertFahrenheit - It will take Celsius and will convert and print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
#-	Write a test class for this one and test it (Look at problem 3 and 4 for example)


class Temprature:
    
    #class method
    def convertFahrenheit(celsius):
        fahrenheit = (celsius* 9 / 5) + 32
        return fahrenheit
    
    #class method
    def convertCelsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

class TestTemprature:
    def test():
        
        fahrenheit = Temprature.convertFahrenheit(20)
        print("fahrenheit=%f" %(fahrenheit))
        celsius = Temprature.convertCelsius(50)
        print("celsius=%f" %(celsius))
        
        

        #Problem2:
        #-	Create a Student class and initialize it with coursesGrades, name and id number. Make methods to :
        #1. Display - It should display name and id number of the student.
        #2. AddCourseGrade – It adds the grades of the courses to the list of courses. 
        #3. getAverage – it calculates the average (GPA) of the student based on the grades of the student.

class Student:
         
    def __init__(self, coursesGrades, name, studentId):
        self._coursesGrades = coursesGrades
        self._name = name
        self._studentId = studentId
        
    def __init__(self, name, studentId):
        self._coursesGrades = []
        self._name = name
        self._studentId = studentId  
        
    
    def display(self):
        print("Name is %s and Id is %s" %(self._name, self._studentId))
        
    def addCourseGrade(self, newGrade):
        self._coursesGrades.append(newGrade)
        
    def getAverage(self):
        
        total = sum(self._coursesGrades)
        if len(self._coursesGrades)>0:
            average = total / len(self._coursesGrades)
            print("Average = %f" %(average))
            return average
        else:
            print("No course to report")
            return 
    
class TestStudent:
    
    def test():
        student1 = Student("Ali", "778811")
        student1.getAverage()
        
        student1.addCourseGrade(60)
        student1.addCourseGrade(73)
        student1.addCourseGrade(81)
        
        student1.getAverage()
        
        student1.display()
        
        #student2 = Student([60,73,81, 90], "James", "778822")
        #student2.getAverage()
        #student2.addCourseGrade(100)
        #student2.display()
        

def main():
    #TestCircle.test()
    #TestTemprature.test()
    TestStudent.test()
    
    
    
main()
        
        
        
        