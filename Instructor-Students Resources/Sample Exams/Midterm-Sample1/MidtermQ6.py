#Problem6: (20 points)
#Answer the following questions:
#Question1: Convert the following code to use a for-loop instead of while-loop to generate exact
#same results:
    
def function():
    print("with while loop")
    word = input("Enter a word [enter exit to terminate]")
    count = 0
    while word!="exit" and count<10:
        print(word)
        count = count + 1
    return


def function_for():
    print("with for loop")
    word = input("Enter a word [enter exit to terminate]")
    
    if word!="exit":
        for i in range(0,10):
            print(word)
            
    return

#function()
#function_for()   

#Question2: The following snippet of code receives an input and then checks whether the input is a
#number. The issue with the following code is that if the user enters a negative number (like -10), the
#code would not work. Make some changes in this code to also work with negative numbers as well as
#positive numbers.

def function():
    print("function")
    number = input ("enter a number: ")
    if number.isdigit():
        return True
    else:
        return False

def function2():
    print("function2")
    number = input ("enter a number: ")
    isNegative = False
    if number[0]=="-":
        isNegative = True
        number = number[1:len(number)]
    
    if number.isdigit():        
        if isNegative:
            num = int(number)*(-1)
            print(num)
            return True
        else:
            num = int(number)
            print(num)
            return True
    else:
        return False
    
#print(function())
#print(function2())

#Question3: The following snippet of code, remove vowels from a string (word) and prints the result,
#which is equivalent to the word without its vowel letters. Do you think this function will work as
#expected? If yes please explain and if no, please fix the issue(s) to generate the expected answer.


word = ["h","o","p","e"," ","t", "o", " ","s", "e", "e", " ","y", "o", "u", " ","a", "l", "l"," ","i", "n", " ","t","h","e"," ","c","o","l","l","e","g","e"," ","s","o","o","n"]
newWord = []
for i in range(len(word)):
    letter = word[i]
    #if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        #word.remove(letter)
    if letter!="a" and letter!="e" and letter!="i" and letter!="o" and letter!="u":
        newWord.append(letter)

#print("After removing the vowels the result is %s" %(word))
print("After removing the vowels the result is %s" %(newWord))


for letter in word:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        word.remove(letter)
print("After removing the vowels the result is %s" %(word))      


#Question4:
#- The following python code would not run and gives some compiles errors.
#- Look at the code and detect what the errors are and fix them.
#- After you fixed it, what is the output of this program?

sideLength = 4  #global variable
def main():
    sideLength = 5  #local variable
    volume = cubeVolume(sideLength)
    print("The volume is: %d " %volume)


def cubeVolume(sideLength):
    volume = 3**sideLength
    print(volume)
    return volume
    
main()

