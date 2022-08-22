#Problem1
#-	Design and implement a function which takes 2 operands (numbers) and one operator (plus, minus, multiplication and division) 
#and applies the operator on the operands and returns and prints the result. 
#Note: If operand1 is a non-zero number and the operand2 is zero, then the program should not perform 
#the division operand and should print the operation is not possible because one number is zero (this is only for division operator) 
#and return -1. 

def addition(num1, num2):
    result = num1+num2
    return result

def subtraction(num1, num2):
    return num1-num2

def mulipication(num1, num2):
    result = num1*num2
    return result

def division(num1, num2):
    if num2==0:
        print("Num2 is zero therefore the division operation cannot be done")
        return -1
    else:
        return num1/num2
    
def calculator(number1, number2, operator):
    if operator=="+":
        result = addition(number1, number2)
    elif operator=="-":
        result = subtraction(number1, number2)
    elif operator=="*":
        result = mulipication(number1, number2)
    elif operator=="/":
        result = division(number1, number2)
    else:
        print("The operator is invalid")
        return
    
    print("%f %s %f = %f" %(number1, operator, number2, result))
    
def main():
    calculator(3.4, 5.6, "+")
    calculator(6.4, -3.6, "-")
    calculator(1.4, -2.6, "*")
    calculator(8.4, -1.6, "/")
    calculator(8.4, 0, "/")
 
main()