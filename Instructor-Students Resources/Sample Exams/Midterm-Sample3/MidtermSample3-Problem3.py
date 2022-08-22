 #Problem3
#-	Write a Python program which prompts the user to enter 4 words. The program need calculate the total sum of the input words that are positive numbers. 

word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
word3 = input("Enter word3: ")
word4 = input("Enter word4: ")

totalSum = 0
if word1.isdigit():
    totalSum = totalSum + int(word1)

if word2.isdigit():
    totalSum = totalSum + int(word2)
    
if word3.isdigit():
    totalSum = totalSum + int(word3)
    
if word4.isdigit():
    totalSum = totalSum + int(word4)
    
print("Total sum is %d" %(totalSum))
    