
word1 = "a1234"
word2 = "1234"
word3 = "abcde"
word4 = "1234"
word5 = "AaBb"

counter = 0

if word1.isalnum():
    counter = counter+5
if word2.isalnum():
    counter = counter+3
if word3.isalpha():
    counter = counter*8
if word4.isdigit():
    counter = counter+1
else:
    #counter = counter*10
    print()
if word5.isalpha:
    counter = counter-2

print(counter)
if counter==638:
    print("Successful")
    

num1 = 10
num2 = 5
num3 = 6
num4 = 7

print("1===============================")
if num1 % 4 == 0:
    print("*")
    print("*")
elif num2 % 3 == 1:
    print("*")
    print("*")
    print("*")
if num3 // 2 == 0 or num4 % 7 == 1:
    print("*")
else:
    print("*")
    print("*")

print("2===============================")

if num1 % 4 == 0 and num2 % 5 == 0:
    print("*")
    print("*")
elif num2 % 3 == 2:
    print("*")
    print("*")
    print("*")
if num3 // 2 == 0 or num4 % 7 == 1:
    print("*")
else:
    print("*")
    print("*")
    
print("3===============================")
    
    
if num1 % 4 == 0 and num2 % 5 == 0:
    print("*")
    print("*")
elif num2 % 3 == 2:
    print("*")
    print("*")
    print("*")
elif num3 // 2 == 0 or num4 % 7 == 1:
    print("*")
else:
    print("*")
    print("*")

print("4===============================")
    
if num1 % 4 == 0:
    print("*")
    print("*")
elif num2 % 3 == 1:
    print("*")
    print("*")
    print("*")
#if num3 // 2 == 0 or num4 % 7 == 1:
else:
    print("*")

    


num1 = 10
num2 = 5
num3 = 6
num4 = 7


if num1 % 2 == 0 and num2 // 2 == 2 and num3 % 4 == 2 and num4 == 7:
    print("S")
elif num1 % 5 == 0:
    print("F")
    
if num1 % 2 ==1:
    if num2 // 2 == 1:
        if num3 % 4 == 3:
            print("S1")
            
if num1 % 2 ==1:
    if num2 // 2 == 1:
        print("S2")
    elif num2 // 2 == 0:
        print("F3")
else:
    print("S4")


if num1 % 2 ==1:
    if num2 // 2 == 1:
        if num3 % 4 == 3:
            print("S5")
        else:
            print("F6")

if num1 % 2 == 1 or num2 // 2 == 1:
    if num3 % 4 == 3 and num4 == 7:
        print("S7")
    else:
        print("F8")