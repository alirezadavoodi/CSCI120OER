'' '
Problem1
-	Write a function which receives two string and checks whether one of them is substring of the other one.
' '' 
 
def checkSubstring (word, subCheck):
if subCheck
in word:
print ("%s is sub-string of %s" % (subCheck, word)) 
  else
: 
print ("%s is Not sub-string of %s" % (subCheck, word)) 
 
return True 
 
'' '
Problem2
-	Write a python function which receives a string as input and find the maximum character in the string and returns it.
' '' 
 
def findMaxCharacter (word):
maxChar = 'a' 
    for
    letter
  in word:
if letter
   >maxChar: 
maxChar = letter 
 print ("The max character in the word %s is %s" % (word, maxChar)) 
 
 
'' '
Problem3
-	Write a function which receives a string and a character as its input parameter.
The function finds how many time the given character has been repeated in the string and returns it.
' '' 
 
def countRepeatingCharacter (word, letter):
count = 0 
	for char in
       word:
if char == letter
: 
count = count + 1 
 print ("Letter %s has been repeated %d times in %s" % (letter, count, word)) 
 
'' '
Problem4
-	Write a function which receives a string and checks whether the string is palindrome (it is the same as itb s reversed)
' '' 
 def isPalindrom (word):
reversedWord =
  "" 
 for
  letter
in word:
reversedWord =
    letter +
    reversedWord 
 
print ("Reversed is: %s" % (reversedWord)) 
 if word
  == reversedWord:
print ("The string is Palindrom") 
    else
   : 
print ("The string is NOT Palindrom") 
 '' '
Problem5
-	Write a function which receives a string and finds the index of the first substring starts with a given letter. 
If there is no such substring it should return -1.
' '' 
 
def findFirstIndexOf (word, letter):
index = -0 
      found = False 
      for char
       in
     word:
if char == letter
     :
print ("Index found is %d" % (index)) 
 return index 
     else
     : 
index = index + 1 
 
print ("The letter does not exist") 
 return -1 
 
 
 
def main ():
checkSubstring ("Vancouver", "oukv") 
	 
findMaxCharacter ("Vancouver") 
	 
countRepeatingCharacter ("Vancouver", "v") 
	 
isPalindrom ("baba") 
	 
findFirstIndexOf ("vancouver", "b") 
 
main ()
