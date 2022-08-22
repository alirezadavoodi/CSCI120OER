# Write a program which ask the user to enter a GPA (like 76) and checks for following
# letter grade based on the table below and prints the proper message:
# For instance if the user entered 70, then the program should print “You are
# Average (C+)”

# A 86–100 Message: “Your are GREAT (A)”
# B 73–85 Message: “Your are GOOD (B)”
# C+ 67-72 Message: “Your are AVERAGE (C+)”
# C 60–66 Message: “You need to practice more (C)”
# C- 50–59 Message: “You need to try harder (C-)”
# F (fail) 0–49 Message: “Unfortunately you failed (F)”


gpa = float(input("Please enter your GPA: "))

if gpa >= 86 and gpa <= 100:
    print("You are GREAT (A)")
elif gpa >= 73 and gpa <=85:
    print("You are GOOD (B)")
elif gpa >= 67 and gpa <= 72:
    print("You are AVERAGE (C+)")
elif gpa >= 60 and gpa <= 66:
    print("You need to practice more (C)")
elif gpa >= 50 and gpa <= 59:
    print("You need to try harder (C-)")
else:
    print("Unfortunately you failed (F)")