#Problem1
#-	Write a Python program which asks the user to enter a password and checks if the password is valid or not. A valid password:
#o	contains only alphabets (letters)
#o	has at least 6 characters
#o	is combination of upper-case and lower-case letters.

password = input("Enter a password: ")
containsOnlyAlpgabet = False
atleast6Characters = False
combinationOfUpperAndLower = False


containsOnlyAlpgabet = password.isalpha()
if len(password)>=6:
    atleast6Characters=True
    
if not password.isupper() and not password.islower():
    combinationOfUpperAndLower = True
    
if containsOnlyAlpgabet and atleast6Characters and combinationOfUpperAndLower:
    print("Password is valid")
else:
    print("Password is Not valid")
