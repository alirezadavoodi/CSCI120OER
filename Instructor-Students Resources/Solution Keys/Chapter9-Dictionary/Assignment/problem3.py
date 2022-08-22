# Design and implement a function which has one input parameter which is a number which is greater than 50, 
# called num. Then the function will create a dictionary whose keys are 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9.
#  Then the function calculates the values for each of the above keys. 
#  The value for a key is all the numbers between 2 and input “num” that are divisible by the key. 
#  The function eventually will print the result. 
# Hint: Use a dictionary whose values are lists.
# Example:
# num = 20
# 2: [2,4,6,8,10,12,14,16,18,20]
# 3: [3,6,9,12,15,18]
# 4: [4,8,12,16,20]
# 5: [5,10,15,20]
# 6: [6,12,18]
# 7: [7, 14]
# 8: [8, 16]
# 9: [9, 18]

def createDictionary(number):
    if number > 50:

        numbersDictionary = { 
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
        }

        for i in range(2, number + 1):
            if i % 2 == 0:
                numbersDictionary[2].append(i)
            if i % 3 == 0:
                numbersDictionary[3].append(i)
            if i % 4 == 0:
                numbersDictionary[4].append(i)
            if i % 5 == 0:
                numbersDictionary[5].append(i)
            if i % 6 == 0:
                numbersDictionary[6].append(i)
            if i % 7 == 0:
                numbersDictionary[7].append(i)
            if i % 8 == 0:
                numbersDictionary[8].append(i)
            if i % 9 == 0:
                numbersDictionary[9].append(i)
        
        return numbersDictionary
            
    else:
        return None

result = createDictionary(51)
for key in result:
    print("%d: " %key, end = "")
    print(result[key])