number1 = int(input("Enter number: "))

if number1==0:
    print("The user has not entered any number!")
else:
    number2 = int(input("Enter number: "))
    if number2==0:
        print("The numbers have been entered ascedingly")
    else:

        flag = True #where the numbers have been entered ascendingly
        while number2!=0:
            if number2 < number1:
                flag = False 
            number1 = number2
            number2 = int(input("Enter number: "))

        if flag:
            print("The numbers have been entered ascendingly!")
        else:
            print("The numbers have NOT been entered ascendingly!")