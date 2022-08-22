class Student:
    #define class student here
    def __init__(self, admissionYear, profile, courses):
        self._admissionYear = admissionYear
        self._profile = profile
        
    #add methods here (if needed)

class profile:
    #define class student here
    

class course:
    #define class course here
    
    
class Menu:
    #define class Menu here
    def printMenu(self, portal):
        self._portal = portal
        #write you menu here
        
    def applySelection(self, selection):
        if selection==1:
            Report.printEnrollmentCertificate(self._portal)
        elif selection==2:
            Report.printGPA(self._portal)
        elif selection==3:
            Report.printRanking(self._portal)
        elif selection==4:
            Report.showMyProfile(self._portal)
        elif selection==0:
            return
            
    
class Report:
    def printEnrollmentCertificate(portal):
        #step1: prompt the user for the student ID
        #step2: from portal find the student with the given student id
        #step3: print the enrollment certificate
        
    
    def printGPA(portal):
        #step1: prompt the user for the student ID
        #step2: from portal find the student with the given student id
        #step3: print the GPA in the format defined in the question
        
    
    def printRanking(portal):
        #similar to the above two methods
        
    
    def showMyProfile(portal):
        #similar to the above methods
        
    
class Portal:
    
    def __init__(self):
        self._students = []
        
    
    def addStudent(self, student):
        self._students.append(student)
    
    
def main():
    
    #Step1: create a portal object:
    portal = Portal()
    
    #Step2: create objects of students based on the information given on the problem description
    
    student1 = Student(......)
    student2 = Student(......)
    student3 = Student(......)
    student4 = Student(......)
    student5 = Student(......)
    
    #Step3: add the students to the portal
    portal.addStudent(student1)
    portal.addStudent(student2)
    portal.addStudent(student3)
    portal.addStudent(student4)
    portal.addStudent(student5)
    
    
    #Step4: create the menu:
    menu = Menu(portal)
    
    #Step5: Print the menu and get the user selection
    selection = menu.printMenu()
    while selection!=0:
        menu.applySelection(selection)
        selection = menu.printMenu()
    
    
main()