#Problem5: (10 points)
#Imagine a table is given as following. This table is called lookup table. The table works as following.
#It assigns a number to some uppercase or lowercase alphabents as shown in the table.
#letter number letter Number
#A 12 e 8
#B 10 f 3
#F 5 i 2
#M 4 m 0
#N 0 n 1
#P 11 p 2
#Q 10 q 3
#W 9 r 4
#Z 9 s 5
#1- Design and implement a function with 2 parameters: 1- a string (a word) 2- a variable that
#represents the above lookup table. The function converts the string to a number and returns it.
#This function replaces each character in the string with its corresponding number from the
#above table. If the character does not exist in the above table, the function replaces it with 0.
#The function will eventually return the number.
#2- Define a main function and call the method you designed in 1. When calling the above
#function in the main method, pass to the function the word “We have missed Vancouver’s
#summer” and the above lookup table. What is the output of the function for the this word,
#“We have missed Vancouver’s summer” ?

dict = {"A": 12, "B":10, "F":5, "M":4, "N":0, "P":11, "Q":10, "W":9, "Z":9, "e":8, "f":3, "i":2, "m":0, "n":1, "p":2, "q":3, "r":4, "s":5}

def convert(word, table):
    
    number = ""
    for character in word:
        if character in table:
            value = table[character]
            number = number + str(value)
        else:
            number = number + "0"
    return number

def main():
    result = convert("We have missed Vancouver’s summer", dict)
    print(result)
    
main()