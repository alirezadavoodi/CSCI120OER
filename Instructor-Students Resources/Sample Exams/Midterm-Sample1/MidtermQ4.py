#Consider the following flowchart and answer the following questions:
    #This flowchart shows an algorithm to convert a positive number in base 10 and any base between
    #2 and 10.
    #- First look at the flowchart and try to get some sense of what it does.
    #- Question1: There is one box which is yellow. You need to add one line of code there in order
    #the algorithm completes and works properly. What is that line? If you feel more than one line
    #is needed, feel free to add them there.
    #- Question2: What is the output of this flowchart if the user enter number =1456 and factor =
    #5?
    #- Question3: Do you see any other error in this flowchart to print the correct answer? If yes,
    #what is it, otherwise, you can write “no other error”.
    #- Question4: Write a Python code for this flowchart that exactly follows the flowchart steps
    #and components.
    
    #start
    
print("Start")
number = int(input("Enter a positive number"))
if number>0:
        factor = int(input("Enter a positive number"))
        lower = 2
        upper = 10
        if factor<lower or factor>upper:
                print("End")
        else:
                temp1 = number
                output = ""
                while temp1!=0:
                        temp1 = number//factor
                        temp2 = number%factor
                        #empty line
                        number = temp1
                        output = str(temp2)+output
                print(output)
                print("end") 
else:
        #end
        print("End")