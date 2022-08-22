import random

class Account:
    def __init__(self):
        self.username = ["Student1", "Student2",
                         "Student3", "Student4", "Student5"]
        self.passoword = ["111111", "222222", "333333", "444444", "555555"]
        self.numberofStudents = 5

    def addUsername(self, newUsername):
        self.username.append(newUsername)
        self.numberofStudents = self.numberofStudents + 1

    def addPassword(self, newPassword):
        self.username.append(newPassword)

    def getUsername(self):
        return self.username

    def getPasswords(self):
        return self.passoword

    def getNumberOfStudents(self):
        return self.numberofStudents


class Course:
    def __init__(self, name, code, unit):
        self._courseName = name
        self._courseCode = code
        self._courseUnit = unit

    def getCourseName(self):
        return self._courseName

    def getCourseCode(self):
        return self._courseCode

    def getCourseUnit(self):
        return self._courseUnit

    def printTakenCourses(self):
        print(f"{self._courseCode} : {self._courseName}\n")


class TakenCourse(Course):
    # implements class TakenCourse
    def __init__(self, collegeCourse, semester, grade=0):
        self.name = collegeCourse.getCourseName()
        self.code = collegeCourse.getCourseCode()
        self.unit = collegeCourse.getCourseUnit()
        super().__init__(self.name, self.code, self.unit)

        self._semester = semester
        self._grade = grade

    def printCourse(self):
        print("Course Name: %s || Course Code: %s || Course Unit %d " %
              (self._courseName, self._courseCode, self._courseUnit))
        self._semester.printSemester()
        print("Grade %d \n" % (self._grade))


class CollegeCourse(Course):
    # implements and complete class CollegeCourse
    def __init__(self, name, code, unit):
        self.name = name
        self.code = code
        self.unit = unit
        super().__init__(name, code, unit)
        self._courseUnit = unit

    def printCourse(self):
        print(f"{self.code}:{self.name}:{self.unit} units ", end=' ')


class Student:
    # implements class student here
    def __init__(self, studentProfile, admissionYear=2018):
        self._admissionYear = admissionYear
        # Suppose each student starts in semester 1 of the admission year
        self._admissionSemester = 1
        self._generalTranscript = GeneralTranscript()
        self._semesterTranscript = CurrentSemesterTranscript()
        self._studentProfile = studentProfile

    def getAdmissionYear(self):
        return self._admissionYear

    def registerCourse(self, collegeCourse, semester, grade=0):

        courseRegistrationYear = semester.getYear()
        courseRegistrationSemester = semester.getSemesterNo()

        course = TakenCourse(collegeCourse, semester, grade)

        if semester.isCurrentSemester():
            self._semesterTranscript.addCourse(course)
            self._generalTranscript.addCourse(course)
        else:
            self._generalTranscript.addCourse(course)

    def getGTranscript(self):
        return self._generalTranscript

    def getSTranscript(self):
        return self._semesterTranscript


class StudentProfile:
    # implements class student here
    def __init__(self, firstName, lastName, gender, country, address, age, stuId, semester, courses):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.country = country
        self.age = age
        self.stuId = stuId
        self.address = address
        self.courses = courses
        self.semester = semester

    def printPrfile(self, admYear, overallGPA, coursesTaken):
        print(f"Name: Mr. {self.firstName} {self.lastName} \nStudentID: {self.stuId}\nGender: {self.gender} \nAddress: {self.address}\nCountry of Origin: {self.country}\nAge: {self.age} \nYear of Admission: {admYear} \nOverall GPA: {overallGPA} \nCourses Taken So far: {coursesTaken}")


class Transcript:
    # implements class transcript here
    def __init__(self):
        self._allTakenCourses = []

    def addCourse(self, takenCourse):
        self._allTakenCourses.append(takenCourse)
        # complete this method

    def printTranscript(self):
        for c in self._allTakenCourses:
            c.printCourse()


class GeneralTranscript(Transcript, TakenCourse):
    # implements class GeneralTranscript here
    def __init__(self):
        super().__init__()

    def printGeneralTranscript(self, name, code, _grade):
        print(f"{name} : {code}: {_grade}")


class CurrentSemesterTranscript(Transcript):
    # implements class CurrentSemesterTranscript here
    def __init__(self):
        super().__init__()

    def printCurrentTranscript(self, name, code, grade):
        print(f"Here is your current semester transcript: \n {code} : {name} : {grade}")


class Manager:
    def __init__(self, firstName, lastName, title):
        self.firstName = firstName
        self.lastName = lastName
        self.title = title


class Semester:
    # implements class Semester here
    def __init__(self, semesterNo, year):
        self._semesterNo = semesterNo
        self._year = year
        self._setIfCurrentSemester()

    def getYear(self):
        return self._year

    def getSemesterNo(self):
        return self._semesterNo

    # checks whether the semester object is representing current semester or not. Suppose, current semester is year = 2019, semester = 2
    def _setIfCurrentSemester(self):
        currentSemester = 2
        currentYear = 2019

        if (self._semesterNo == currentSemester) and (self._year == currentYear):
            self._isCurrentSemester = True
        else:
            self._isCurrentSemester = False

    def isCurrentSemester(self):
        return self._isCurrentSemester

    def printSemester(self):
        print("Year: %d Semester%d isCurrent %d" %
              (self._year, self._semesterNo, self._isCurrentSemester))


class Menu():
    def __init__(self):
        print("*"*50 + "\n" "Please enter your account to login:\n"+"*"*50+"\n" +
              "Not registered yet? Type 'Register' in Username and press enter to start the registration process\n"+"-"*20+"\n")
        self.username = input("Username: ")

        if self.username == "Register":
            print("*"*50 + "\n" + "Welcome to Columbia College!" +
                  "\n" + "*"*50 + "\n")
            self.firstName = input("Please enter your first name: ")
            self.lastName = input("Please enter your last name: ")
            self.gender = input("Please enter your gender [M/F/O]:")
            self.country = input("Please enter your country of Origin: ")
            self.yearAdmission = input("Please enter year of admission: ")
            print()
            self.age = input("Please enter your age: ")
            self.newUsername = input(
                "Please enter a username[at least 6 character]: ")
            self.newPassword = input(
                "Please enter a password[at least 6 character with at least one digit]: ")
            self.stuID = random.randint(10000000, 99999999)
            account = Account()
            account.addUsername(self.newPassword)
            account.addPassword(self.newPassword)
        else:
            self.password = input("Password: ")

    def showCorrect(self):
        print("*"*50 + "\n" + "Welcome to Columbia College!\n" + "*"*50)

    def showWrong(self):
        print("*"*50 + "\n" + "Your account does not exist. Please try again\n" + "*"*50)

    def showMainMenu(self):
        print("*"*50+"\n"+"Select from the options:\n"+"*"*50+"\n")
        print("-[1] Print my enrolment certificate\n"+"-[2] Print my courses\n"+"-[3] Print my transcript\n"+"-[4] Print my GPA\n"+"-[5] Print my ranking among all students in the college\n" +
              "-[6] List all available courses\n"+"-[7] List all students\n"+"-[8] Show My Profile\n"+"-[9] Logout\n"+"-[10] Exit\n"+"*"*50+"\n")
        self.menuOption = input(
"Enter the number corresponding to each item to proceed: ")

    def printEnrolmentCertificate(self, firstName, lastName, stuId, admYear, semester, course, address):
        print("Dear Sir/Madam,\n" + f"This is to certify that Mr. {firstName} {lastName} with student id {stuId} is a student at semester {semester} at Columbia College. He was admitted to our college in {admYear} and had taken {course} courses so far. Currently he resides at {address}.\n" +
              "If you have any question, please don't hesitate to contact us.\n"+"Thanks,\n"+"[Manager:Peter Smith]\n")

    def printTakenCourses(self, firstName, lastName):
        print(f"Hi Mr. {firstName} {lastName},\n" +
              "You have taken following courses so far:\n")
    def printInvalidOption(self):
        print("Please select valid option!!\n")

    def printGeneralGreeting(self, firstName, lastName):
        print(f"Hi Mr. {firstName} {lastName},\n"+"Here is your general transcript:\n")

    def printcurrentGreeting(self, firstName, lastName):
        print(f"Hi Mr. {firstName} {lastName},\n" +
              "Here is your current semester transcript:\n")

    def getNewUserName(self):
        return self.username

    def getNewPassward(self):
        return self.password

    def printStudents(self, firstName, lastName, stuId):
        print(f"{firstName} {lastName}:{stuId}\n")


class Portal:

    # _currentSemester = Semester(2019, 2)  # Static/class property. Suppose the current semester is second semester 2019
    def __init__(self):
        self._collegeCourses = [CollegeCourse("Python", 101, 3)]
        self._registeredStudents = [
            "student1", "student2", "student3", "student4", "student5"]

    # use this method to register a student

    def registerStudent(self, student):
        self._registeredStudents.append(student)

    def addCourse(self, collegeCourse):
        self._collegeCourses.append(collegeCourse)
    # class this method to add some random courses to a student - You don't need to understand how this method works. Just call it and it will add some courses
    # to the student and to different semesters

    def addRandomCoursesToStudent(self, student):
        for course in self._collegeCourses:
            rand = random.uniform(0, 1)
            admissionYear = student.getAdmissionYear()
            currentSemester = Portal.getCurrentSemester()

            if currentSemester.getYear() == admissionYear:
                numberOfSemesterBetweenCurrentSemesterAndAdmission = currentSemester.getSemesterNo()
            else:
                numberOfSemesterBetweenCurrentSemesterAndAdmission = 2 * \
                    (currentSemester.getYear() - admissionYear) + \
                    currentSemester.getSemesterNo()

            randomSemster = random.randint(
                1, numberOfSemesterBetweenCurrentSemesterAndAdmission - 1)

            year = randomSemster // 2
            semesterNo = (randomSemster % 2) + 1
            semester = Semester(semesterNo, student.getAdmissionYear() + year)

            randomGrade = random.randint(30, 100)

            if rand <= .5:
                student.registerCourse(course, semester, randomGrade)

    # static/class method
    def getCurrentSemester():
        # Static/class property. Suppose the current semester is second semester 2019
        currentSemester = Semester(2, 2019)
        return currentSemester


class PortalManager:
    def __init__(self):
        self._portal = Portal()

    def createATestPortal(self):

        # create all courses offered
        self._createAllCollegeCourses()
        # self._portal.printAllCollegeCourses()

        # create a sample student
        sampleStudentProfile = StudentProfile(
            "Peter", "Sand", "M", "Ireland", "Vancouver", 21, 8012321, 2, 5)
        sampleStudent1 = Student(sampleStudentProfile, 2019)
        student1Courses = [Course("Python", "CSCI101", 3), Course("Obeject-oriented Programming", "CSCI102", 2), Course("Problem Solving", "CSCI201", 1), Course("Project Management", "CSCI202", 3), Course("Java Programming", "CSCI301", 3)]
        student1Transcript = [TakenCourse(student1Courses[0], 1, 80), TakenCourse(student1Courses[1], 2, 76), TakenCourse(student1Courses[2], 3, 67), TakenCourse(student1Courses[3], 1, 82), TakenCourse(student1Courses[4], 2, 73)]
        student1CurrentCourses = [TakenCourse(student1Courses[2], 3, 67)]

        sampleStudentProfile2 = StudentProfile("Sheila", "Rogers", "F", "India", "Surrey", 19, 8014525, 2, 8)
        sampleStudent2 = Student(sampleStudentProfile2, 2018)
        student2Courses = [Course("Python", "CSCI101", 3), Course("Obeject-oriented Programming", "CSCI102", 2), Course("Problem Solving", "CSCI201", 1), Course("Project Management", "CSCI202", 3),
                           Course("Java Programming", "CSCI301", 3), Course("WebDevelopment", "CSCI302", 2), Course("Android Programming", "CSCI401", 2), Course("iOSApplication", "CSCI402", 3)]
        student2Transcript = [TakenCourse(student2Courses[0], 1, 65), TakenCourse(student2Courses[1], 2, 67), TakenCourse(student2Courses[2], 2, 85), TakenCourse(
            student2Courses[3], 3, 56), TakenCourse(student2Courses[4], 3, 75), TakenCourse(student2Courses[5], 4, 76), TakenCourse(student2Courses[6], 4, 80), TakenCourse(student2Courses[7], 5, 74)]
        student2CurrentCourses = [TakenCourse(student2Courses[7], 5, 74)]

        sampleStudentProfile3 = StudentProfile(
            "Edward", "Richards", "M", "China", "Burnaby", 20, 8011111, 2, 4)
        sampleStudent3 = Student(sampleStudentProfile3, 2019)
        student3Courses = [Course("Problem Solving", "CSCI201", 1), Course(
            "Project Management", "CSCI202", 3), Course("No Course", "/", 0), Course("WebDevelopment", "CSCI302", 2)]
        student3Transcript = [TakenCourse(student3Courses[0], 1, 78), TakenCourse(
            student3Courses[1], 1, 87), TakenCourse(student3Courses[2], 2, 0), TakenCourse(student3Courses[3], 3, 82)]
        student3CurrentCourses = [ TakenCourse(student3Courses[3], 3, 82)]


        sampleStudentProfile4 = StudentProfile(
            "Souzan", "Robson", "F", "India", "Vancouver", 20, 8033344, 2, 5)
        sampleStudent4 = Student(sampleStudentProfile4, 2019)
        student4Courses = [Course("Project Management", "CSCI202", 3), Course("Java Programming", "CSCI301", 3), Course(
            "WebDevelopment", "CSCI302", 2), Course("Android Programming", "CSCI401", 2), Course("iOSApplication", "CSCI402", 3)]
        student4Transcript = [TakenCourse(student4Courses[0], 1, 89), TakenCourse(student4Courses[1], 1, 87), TakenCourse(
            student4Courses[2], 2, 71), TakenCourse(student4Courses[3], 2, 69), TakenCourse(student4Courses[4], 3, 73)]
        student4CurrentCourses = [ TakenCourse(student4Courses[4], 3, 73)]

        sampleStudentProfile5 = StudentProfile(
            "Jeff", "Cooper", "M", "England", "Vancouver", 21, 8012322, 2, 7)
        sampleStudent5 = Student(sampleStudentProfile5, 2018)
        student5Courses = [Course("WebDevelopment", "CSCI302", 2), Course("Android Programming", "CSCI401", 2), Course(
            "iOSApplication", "CSCI402", 3), Course("Project Management", "CSCI202", 3), Course("Java Programming", "CSCI301", 3)]
        student5Transcript = [TakenCourse(student5Courses[0], 1, 78), TakenCourse(student5Courses[1], 2, 56), TakenCourse(
            student5Courses[2], 2, 89), TakenCourse(student5Courses[3], 3, 66), TakenCourse(student5Courses[4], 3, 77)]
        student5CurrentCourses = [TakenCourse(student5Courses[4], 3, 77)]

         


        # register the sample student
        self._portal.registerStudent(sampleStudent1)
        self._portal.registerStudent(sampleStudent2)
        self._portal.registerStudent(sampleStudent3)
        self._portal.registerStudent(sampleStudent4)
        self._portal.registerStudent(sampleStudent5)

        # add some random courses with grades to the student

        return {"Student1": [sampleStudentProfile, sampleStudent1, student1Courses, student1Transcript,student1CurrentCourses], "Student2": [sampleStudentProfile2, sampleStudent2, student2Courses, student2Transcript,student2CurrentCourses], "Student3": [sampleStudentProfile3, sampleStudent3, student3Courses, student3Transcript,student3CurrentCourses], "Student4": [sampleStudentProfile4, sampleStudent4, student4Courses, student4Transcript,student4CurrentCourses], "Student5": [sampleStudentProfile5, sampleStudent5, student5Courses, student5Transcript,student5CurrentCourses]}

    # create college courses

    def _createAllCollegeCourses(self):
        python = CollegeCourse("Python", "CSCI101", 3)
        objectOrientedProgramming = CollegeCourse(
            "Obeject-oriented Programming", "CSCI102", 2)
        problemSolving = CollegeCourse("Problem Solving", "CSCI201", 1)
        projectManagement = CollegeCourse("Project Management", "CSCI202", 3)
        javaProgramming = CollegeCourse("Java Programming", "CSCI301", 3)
        webDevelopment = CollegeCourse("Web Development", "CSCI302", 2)
        androidProgramming = CollegeCourse("Android Programming", "CSCI401", 2)
        iOSApplication = CollegeCourse("iOS Application", "CSCI402", 3)
        availableCoursesList = [CollegeCourse("Python", "CSCI101", 3), CollegeCourse("Obeject-oriented Programming", "CSCI102", 2), CollegeCourse("Problem Solving", "CSCI201", 1), CollegeCourse(
            "Project Management", "CSCI202", 3), CollegeCourse("Java Programming", "CSCI301", 3), CollegeCourse("Web Development", "CSCI302", 2), CollegeCourse("Android Programming", "CSCI401", 2), CollegeCourse("iOS Application", "CSCI402", 3)]

        self._portal.addCourse(python)
        self._portal.addCourse(objectOrientedProgramming)
        self._portal.addCourse(problemSolving)
        self._portal.addCourse(projectManagement)
        self._portal.addCourse(javaProgramming)
        self._portal.addCourse(webDevelopment)
        self._portal.addCourse(androidProgramming)
        self._portal.addCourse(iOSApplication)
        return availableCoursesList


def main():
    portalManager = PortalManager()
    allUserDict = portalManager.createATestPortal()
    account = Account()
    portal = Portal()
    checkUser = False
    login = True
    while login:

        while not checkUser:
            account = Account()
            portal = Portal()
            menu = Menu()
            if menu.getNewUserName() == "Register":
                if len(menu.newUsername) < 6:
                    print("Enterred username is invalid. Enter valid username!!")
                    print()
                    continue
                elif len(menu.newPassword) < 7 and menu.newPassword.isalnum():
                    print("Enter valid new password!!")
                    print()
                    continue
                else:
                    print(
                        f"Thanks, your account and profile has been created successfully. Welcome Abroad {menu.firstName}")
                    account.addUsername(menu.newUsername)
                    account.addPassword(menu.newPassword)
                    portal.registerStudent(menu.newUsername)
                    continue
            userName = account.getUsername()
            passWord = account.getPasswords()
            i = 0
            for j in range(0, len(userName)):
                if menu.getNewUserName() == userName[j]:
                    checkUser = True
                    i = j
            if not checkUser:
                menu.showWrong()
                continue
            if(menu.getNewPassward() == passWord[i]):
                checkUser = True
            else:
                menu.showWrong()
                checkUser = False
                
        sum = 0
        for obj in allUserDict[menu.username][3]:
                sum = (sum+obj._grade)
        overallGPA = sum/len(allUserDict[menu.username][3])
        overallCurrentGPA = 0
        menu.showCorrect()
        menu.showMainMenu()
        if int(menu.menuOption) > 10 or int(menu.menuOption) < 1:
            menu.printInvalidOption()
        if int(menu.menuOption) == 9:
            checkUser = False
            continue
        elif int(menu.menuOption) == 10:
            break
        elif int(menu.menuOption) == 1:
            menu.printEnrolmentCertificate(allUserDict[menu.username][0].firstName, allUserDict[menu.username][0].lastName, allUserDict[menu.username][0].stuId, allUserDict[menu.username][1].getAdmissionYear(
            ), allUserDict[menu.username][0].semester, allUserDict[menu.username][0].courses, allUserDict[menu.username][0].address)
        elif int(menu.menuOption) == 2:
            menu.printTakenCourses(allUserDict[menu.username][0].firstName, allUserDict[menu.username][0].lastName)
            for obj in allUserDict[menu.username][2]:
                obj.printTakenCourses()
        elif int(menu.menuOption) == 3:
            menu.printGeneralGreeting(allUserDict[menu.username][0].firstName, allUserDict[menu.username][0].lastName)

            generalTranscript = GeneralTranscript()
            for obj in allUserDict[menu.username][3]:
                generalTranscript.printGeneralTranscript(
                    obj.code, obj.name, obj._grade)
            currentSemesterTranscript = CurrentSemesterTranscript()

            print("\n"+f"YOUR GPA IS:{overallGPA}"+"\n")
           
            for obj in allUserDict[menu.username][4]:
                currentSemesterTranscript.printCurrentTranscript(
                    obj.name, obj.code, obj._grade)
            overallCurrentGPA = 0
            
            sum = 0
            for obj in allUserDict[menu.username][4]:
                sum = (sum+obj._grade)
            overallCurrentGPA = sum/len(allUserDict[menu.username][4])
            print(
                "\n"+f"YOUR Current semester GPA is:{overallCurrentGPA}"+"\n")
        elif int(menu.menuOption) == 4:
            print(f"\nHi, Mr.{allUserDict[menu.username][0].firstName} {allUserDict[menu.username][0].lastName},")
            print(f"YOUR GPA IS:{overallGPA}")
            sum = 0
            for obj in allUserDict[menu.username][4]:
                sum = sum+obj._grade
            overallCurrentGPA = sum/len(allUserDict[menu.username][4])
            print(f"YOUR Current semester GPA is:{overallCurrentGPA}"+"\n")
        elif int(menu.menuOption) == 5:
            overallGPADict = {}
            sum = 0

            for key in allUserDict:
                for obj in allUserDict[key][3]:
                        sum = sum + obj._grade
                overallGPA = sum/len(allUserDict[key][3])
                overallGPADict[key] = overallGPA
                sum = 0
        # average 75.6 72.6 61.75 78.2 73.2

            rank = 1
            for key in overallGPADict:
                if(overallGPADict[menu.username] < overallGPADict[key]):
                    rank = rank + 1
            print(f"Hi Mr. {allUserDict[menu.username][0].firstName} {allUserDict[menu.username][0].lastName},\n"+f"Your overall GPA is {overallGPADict[menu.username]} and therefore your rank is {rank}\n")
        elif int(menu.menuOption) == 6:
            availableCoursesList = portalManager._createAllCollegeCourses()
            print("The following courses are offered in Columbia College:\n")
            pickedCourses = []
            for obj in allUserDict[menu.username][3]:
                pickedCourses.append(obj.code)

            for i in availableCoursesList:
                i.printCourse()
                if(i._courseCode in pickedCourses):
                    print("[Already taken]")
                else:
                    print("[Not taken]")
        elif int(menu.menuOption) == 7:
            print(f"There are {account.getNumberOfStudents()} students in Columbia College as following:\n")
            userNames = account.getUsername()
            for account in userNames:
                menu.printStudents(allUserDict[account][0].firstName,allUserDict[account][0].lastName,allUserDict[account][0].stuId)
        elif int(menu.menuOption) == 8:
            coursesList = []
            for obj in allUserDict[menu.username][3]:
                coursesList.append(obj.code+":"+obj.name)
            allUserDict[menu.username][0].printPrfile(allUserDict[menu.username][1].getAdmissionYear(),overallGPA,coursesList)


main()
