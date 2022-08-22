#Write a python program which receives a word with length 7 from input and insert a star
#character, *, between each alphabet of the word. For instance if the user entered “alireza”
#then your program should change it to a*l*i*r*e*z*a* and prints it.

#word = input("Please enter a word with length 7: ")

#CHAR = "*"
#newWord = word[0]+CHAR+word[1]+CHAR+word[2]+CHAR+word[3]+CHAR+word[4]+CHAR+word[5]+CHAR+word[6]+CHAR

#print("word is %s and new word is %s" %(word, newWord))

if "alirez a".isalpha():
    print("yes")
else:
    print("no")
    

word1 = "a1234"
word2 = "1234"
word3 = "abcde"
word4 = "-1234"
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
if word5.isalpha:
     counter = counter-2

print(counter)

