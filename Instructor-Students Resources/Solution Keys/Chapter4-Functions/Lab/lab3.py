
def addition(num1, num2):
    result = num1 + num2
    return result


def subtraction(num1, num2):
    return num1 - num2


def multipication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Division by Zero error")
        return


def calculator(number1, number2, operator):
    if operator == '+':
        result = addition(number1, number2)
        print("%d %s %d = %d" % (number1, operator, number2, result))
        return result
    elif operator == '-':
        result = subtraction(number1, number2)
        print("%d %s %d = %d" % (number1, operator, number2, result))
        return result
    elif operator == '*':
        result = multipication(number1, number2)
        print("%d %s %d = %d" % (number1, operator, number2, result))
        return result
    elif operator == '\\':
        result = division(number1, number2)
        if number2 != 0:
            print("%d %s %d = %d" % (number1, operator, number2, result))
            return result
        return
    else:
        print("The operator is not supported")
        return


def testCalculator():
    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))
    operator = input("Enter the operator(+,-,\\,*)")
    calculator(number1, number2, operator)

    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))
    operator = input("Enter the operator(+,-,\\,*)")
    calculator(number1, number2, operator)

    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))
    operator = input("Enter the operator(+,-,\\,*)")
    calculator(number1, number2, operator)

    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))
    operator = input("Enter the operator(+,-,\\,*)")
    calculator(number1, number2, operator)

# ==========================================


def checkPrime(number):
    if number == 0 or number == 1:
        print("The %d is not prime" % (number))
        return False
    if number < 0:
        print("It does not support negative number")
        return
    for item in range(2, (number // 2) + 1):
        if number % item == 0:
            print("The %d is not prime" % (number))
            return False
    print("The %d is prime" % (number))
    return True


def testPrime():
    checkPrime(0)
    checkPrime(1)
    checkPrime(2)
    checkPrime(20)
    checkPrime(67)
    checkPrime(-67)


def main():
    # testCalculator()
    testPrime()


main()
