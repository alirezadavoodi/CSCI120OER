
##Program8:

#numberString = input("Enter a number:")

##print("is digit: %g" %(numberString.isdigit()))
##print("is alnum: %g" %(numberString.isalnum()))
##print("is numeric: %g" %(numberString.isnumeric()))

#if numberString[0]=="-":
    #isPotentiallyANegativeNumber = True
#else:
    #isPotentiallyANegativeNumber = False

#if isPotentiallyANegativeNumber:
    ##isInputValid = numberString.isdigit() #this is not going to work
    ##-10: valid
    ##-10ab: invalid
    #newNumber = ""
    #for i in range(1, len(numberString)):
        #newNumber = newNumber+numberString[i]
    
    ##-10->10
    ##-10ab-> 10ab
    #isInputValid = newNumber.isdigit()
    
#else:
    #isInputValid = numberString.isdigit()

##str.isalnum()
##Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise. 
##A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().

##str.isdigit()
##Return True if all characters in the string are digits and there is at least one character, False otherwise. 
##Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits. 
##This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. 
##Formally, a digit is a character that has the property 
##value Numeric_Type=Digit or Numeric_Type=Decimal.

##str.isnumeric()
##Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise. 

#if isInputValid:
    #if isPotentiallyANegativeNumber:
        #number = int(newNumber)
        #number = number*(-1)
    #else:
        #number = int(numberString)
    
    #maximum = number
    #minimum = number
    
    #while isInputValid:
        #if number >= maximum:
            #maximum = number
            
        #if number <= minimum:
            #minimum = number
                    
        #numberString = input("Enter a number:") 
        
        #if numberString[0]=="-":
            #isPotentiallyANegativeNumber = True
        #else:
            #isPotentiallyANegativeNumber = False
        
        #if isPotentiallyANegativeNumber:
            #newNumber = ""
            #for i in range(1, len(numberString)):
                #newNumber = newNumber+numberString[i]            
            #isInputValid = newNumber.isdigit()            
        #else:
            #isInputValid = numberString.isdigit()
        
        
        ##isInputValid = numberString.isdigit()
        #if not isInputValid:
            #print("The input is not valid!")
        #else:
            #if isPotentiallyANegativeNumber:
                #number = int(newNumber)
                #number = number*(-1)
            #else:
                #number = int(numberString)                        
            
    #print("Maximum is: %d" %(maximum))
    #print("Minimum is: %d" %(minimum))
    #print("distance is %d" %(maximum-minimum))
            
#else:
    #print("The input is not valid!")
    

#Program9:
#Consider two following mathematical functions:
#• F1(x) = 2^x
#• F2(x) = x^5
#• ^ means exponent. Example: 2^3 = 2*2*2 = 8
#The program should find the positive number (and greater than 2), (let’s call is T) which has
#the following characteristic:
#• For all numbers which are less than T we have F1(x)< F2(x)
#• For all numbers which are less than 100 and greater than or equal T we have F1(x)> F2(x)

x=3
f1x = 2**x
f2x = x**5

while f1x<f2x:
    x = x + 1
    f1x = 2**x
    f2x = x**5
    print("x=%d  f1x=%d  f2x=%d" %(x, f1x, f2x))

t = x
flag = True
for number in range(t, 100):
    f1x = 2**number
    f2x = number**5
    print("x=%d  f1x=%d  f2x=%d" %(number, f1x, f2x))
    
    if f1x<f2x:
        flag = False

if flag:
    print("The number we are looking for is %d " %(t))
else:
    print("There is no such a number")
    




