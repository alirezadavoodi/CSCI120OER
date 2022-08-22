#Problem5
#- Write a function which has no input parameter but returns a dictionary. The function lets
#the user enter names as long as the user enters 0. The user can enter a same name over
#and over. At the end the function will print and return a dictionary which shows all the
#names the user has entered and how many times each name is repeated.
#- For example:
#Ali : 3
#Peter: 4
#Jack: 1
#Allison:2

def createNameDictionary():
    
    name = input("Enter a name [Enter 0 to stop]: ")
    
    dict = {}
    while name!= "0":
        
        if name.lower() in dict:
            dict[name.lower()] = dict[name.lower()]+1
        else:
            dict[name.lower()] = 1
            
        name = input("Enter a name [Enter 0 to stop]: ")
    
    print(dict)
    return dict

def main():
    result = createNameDictionary()

main()