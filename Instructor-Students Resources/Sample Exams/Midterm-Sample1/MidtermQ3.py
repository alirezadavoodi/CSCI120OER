#Problem3: Programming (15 points)
#- Create a function called, convert. This function receives a string parameter called word which
#only contains digits (the string represents a positive number) and returns a list of numbers.
#This is how the function works:
#- This function calculates the number of times each digit has repeated in the input string and
#then generates a number based on that using the following formula and adds it to a list. For
#instance, if the digit x has been repeated n times, then the function will calculate n*10+x and
#adds it to the list. (See the example)
#Example input: “6743672316”
#In the above string:
#- 6 is repeated 3 times. Then the corresponding number to be added to the list is 3*10+6 = 36
#- 7 is repeated 2 times: The number to be added to the list 2*10+7 = 27
#- 4 is repeated once: The number to be added to the list is 1*10+4 = 14
#- 3 is repeated 2 times: The number to be added to the list is 2*10+3 = 23
#- 2 is repeated once: The number to be added to the list is 1*10+2 = 12
#- 1 is repeated once: The number to be added to the list is 1*10+1 = 11
#Then the functions convert returns the following list: [36,27,14,23,12,11]
#Note: The order of the numbers in the list is not important.

#"6743672316"
#formula: n*10+x

def convert1(word):    #first approach
    wordList = []
    
    for i in range(0,10):
        n = word.count(str(i))
        if n>0:
            formula = n*10+i
            wordList.append(formula)
        
    return wordList



def convert2(word):    #second approach
    dict = {}
    
    for character in word:
        
        if character in dict:
            dict[character] = dict[character] + 1
        else:
            dict[character] = 1
      
    wordList = []      
    for character in dict:
        n = dict[character]
        formula = n*10+int(character)
        wordList.append(formula)
    
    return wordList
        
    

def main():
    wordList = convert1("6743672316")
    print(wordList)
    
    wordList = convert2("6743672316")
    print(wordList)
    
main()