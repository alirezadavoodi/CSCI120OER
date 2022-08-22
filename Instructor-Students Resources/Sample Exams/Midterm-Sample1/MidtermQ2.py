#Problem2: Design and Programming (15 points)
#- Imagine a PolynomialEquation is a mathematical equation with only one base factor. For
#instance the followings are examples of PolynomialEquations with one base factor, which is
#“x”:
#o Note: The ^ operator is the power operation. For instance, 2^3 = 2*2*2 = 8
#Some examples of PolynomialEquations
#o 5*x^4 – 3*x^2 + 6
#o 10*x^5 + 8*x^4 + x^2 + 5
#o 2*x^2
#o 4*x^3 + 5
#o 10
#- Also, suppose each PolynomialEquation is composed of one or more
#SinglePolynomialFactors. Each SinglePolynomialFactor is composed of three following
#properties (data):
#o coefficient
#o baseFactor
#o exponent
#- Examples:
#o -3*x^7: Is a SinglePolynomialFactor with (coefficient=-3, baseFactor = ‘x’,
#exponent=7)
#o 5: Is a SinglePolynomialFactor (coefficient=5, baseFactor = ‘x’, exponent=0)
#o 4*x: Is a SinglePolynomialFactor with (coefficient=4, baseFactor = ‘x’, exponent=1)
#- Let’s look at one more example to make sure you understand what a PolynomialEquation and
#a SinglePolynomialFactor is. For example, look the following table which shows some
#PolynomialEquations and their SinglePolynomialFactors.
#PolynomialEquation SinglePolynomialFactors
#5*x^4 – 3*x^2 + 6
#5*x^4
#– 3*x^2
#6
#10*x^5 + 8*x^4 + x^2 + 5
#10*x^5
#8*x^4
#x^2
#438

#PolynomialEquation: 10*x^5 + 8*x^4 + x^2 + 5
#SinglePolynomialFactor: 10*x^5    8*x^4   x^2   5


#PolynomialEquation is a list of SinglePolynomialFactor

#Approach 1
#SinglePolynomialFactor's data structure:
#dictionary : 10*x^5
#{"coefficient":10, "baseFactor":"x", "exponent":5}
#PolynomialEquation is a list of dictionary


def checkSingleFactorEquality(singleFactor1, singleFactor2):
    #dictionary data:
    
    if singleFactor1==singleFactor2:
        return True
    else:
        return False
    

def PolynomialEquationsEquality(polynomialFactor1, polynomialFactor2):
    
    if polynomialFactor1==polynomialFactor2:
        return True
    else:
        return False


#Approach 2
#tuple : 10*x^5
#(10, "x", 5)
#PolynomialEquation is a list of tuple


#Approach 3:
#String: "10*x^5"
#PolynomialEquation is a list of String



