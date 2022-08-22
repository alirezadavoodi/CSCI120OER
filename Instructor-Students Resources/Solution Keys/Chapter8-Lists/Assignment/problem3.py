# Write a function which takes no input parameter and allow the user to enter words as many as 
# the user wants until the user enters an empty word. When the user enters a word, the function 
# will add the word to a list which was originally empty. Before the function adds the word 
# to the list, it should check whether the same word had been already added to the list or not. 
# If not, then the word is added to the list and if yes, the word should not be added to the list. 
# The function will eventually return the list of words.
# Note: Only use List to solve this problem

def makeWordList():
    list = []
    value = input("Please enter the word: ")
    while not value == "":
        if not value in list:
            list.append(value)
        value = input("Please enter the word: ")
    print(list)

makeWordList()
