'''
Problem1
-   Write a Python program which checks whether a file is an HTML file or not. An HTML file is a file with an .html extension.
'''
word = "Python Programming.html"
if word.endswith("html"):
    print("it is an html file")
else:
    print("it is NOT an html file")


'''
Problem2
-   Write a Python program which checks whether a sentence starts with the word Python.
'''
word = "Python Programming.html"
if word.startswith("Python"):
    print("The word starts with Python")
else:
    print("The word does not start with Python")



'''
Problem3
-   A word is given, do the following:
o   Check if the word only contains numbers
o   Check if the word only contains alphabets
o   Check if the word only contains numbers and alphabets
'''

word1 = "1245"
word2 = "vancouver"
word3 = "vancouver2022"

if word1.isdigit():
    print("%s only contains numbers" %(word1))
else:
    print("%s Does not only contain numbers" %(word1))


if word2.isalpha():
    print("%s only contains alphabets" %(word2))
else:
    print("%s Does not only contain alphabets" %(word2))


if word3.isalnum():
    print("%s only contains alphabets and numbers" %(word3))
else:
    print("%s Does not only contain alphabets and numbers" %(word3))



'''
Problem4
-   A word is given, do the following:
o   Check if the word only contains lower case alphabets
o   Check if the word only contains upper case alphabets
'''
word1 = "college"
word2 = "COLLEGE"


if word1.islower():
    print("%s only contains lower cases" %(word1))
else:
    print("%s Does not only contain lower cases" %(word1))


if word2.isupper():
    print("%s only contains upper cases" %(word2))
else:
    print("%s Does not only contain upper cases" %(word2))
    

'''
Problem5
-   A word is given, write a Python program which finds number of non-overlapping AA substring in the word.
'''
word1 = "AAAAABBAA"
count = word1.count("AA")
print("There are %d %s in %s" %(count, "AA", word1))
