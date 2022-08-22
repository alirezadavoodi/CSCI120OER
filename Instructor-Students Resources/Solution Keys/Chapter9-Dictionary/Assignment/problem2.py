# Write a function which lets the user enter English words. 
# The user can keep entering English words as long as the user has not entered the word “exit”. 
# Once the user enters “exit” the function will return and print the list of all distinct words 
# starts with English alphabets. Like:
# A: Ali, apple, …
# B: Bob, book
# … until Z

def createDictionary():

    wordDictionary = {"A":[], "B":[], "C":[], "D":[], "E":[], "F":[], "G":[], "H":[], "I":[], "J":[], "K":[], "L":[], "M":[], "N":[], "O":[], "P":[], "Q":[], "R":[], "S":[], "T":[], "U":[], "V":[], "W":[], "X":[], "Y":[], "Z":[]}
    word = input("Enter a word [Enter exit to terminate]: ")

    while word != "exit":
        if len(word) > 0:
            firstLetter = word[0].upper()
            if firstLetter in wordDictionary:
                if not word in wordDictionary[firstLetter]:
                    wordDictionary[firstLetter].append(word)
            else:
                wordDictionary[firstLetter] = []
        word = input("Enter a word [Enter exit to terminate]: ")

    return wordDictionary


print(createDictionary())