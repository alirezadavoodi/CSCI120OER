#Problem4
#- Imagine, each student is represented by the following properties:
#o firstName
#o lastName
#o address
#o Year of birth
#o gpa
#Write a function which receives a list of students as its input parameter and return the
#student who has the highest average.
#- Hint: Use a dictionary (the properties are the keys and the values are the values of the properties, for
#instance, “FirstName”:”Ali”). And the define a list of dictionaries and each dictionary represents a student.

def findStundetWithHighestGPA(students):
    
    highestGPA = 0
    studentWithHighestGPA = None
    
    for student in students:
        if student["gpa"]>=highestGPA:
            highestGPA = student["gpa"]
            studentWithHighestGPA = student
    
    return studentWithHighestGPA

def main():
    listOfStudents = []
    student1 = {"firstName":"Peter", "lastName":"Brown", "address":"Vancouver", "birthYear":2000, "gpa":78}
    listOfStudents.append(student1)
    
    student2 = {"firstName":"Sarah", "lastName":"Jones", "address":"Burnaby", "birthYear":1999, "gpa":80}
    listOfStudents.append(student2)
    
    student3 = {"firstName":"Philippe", "lastName":"Jackson", "address":"Vancouver", "birthYear":1998, "gpa":81}
    listOfStudents.append(student3)
    
    student4 = {"firstName":"Mary", "lastName":"Moh", "address":"Surrey", "birthYear":2000, "gpa":79}
    listOfStudents.append(student4)
    
    student = findStundetWithHighestGPA(listOfStudents)
    print(student)
    
main()