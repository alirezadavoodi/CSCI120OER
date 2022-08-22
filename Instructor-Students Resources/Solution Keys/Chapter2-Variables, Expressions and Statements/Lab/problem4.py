# Write a Python program that prompts (ask) the user to enter his/her first-name and 
# last-name. The Python program, the concatenate the first-name to last-name and print the following message:
# Hi [first-name last-name], I hope you are doing well!

firstName = input("enter your first name: ")
lastName = input("enter your last name: ")

print("Hi %s %s, I hope you are doing well!" %(firstName, lastName))