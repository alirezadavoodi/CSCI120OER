#Problem2
#-	Write a program which asks the user to enter a temperature value in Celsius and base on the following rules generates some outputs:
#o	If the temperature is greater than 35 degree: then prints: “It is to too warm, stay home” 
#o	If the temperature is greater than 30 but less than 35, then prints: “It is really a summer day”
#o	If the temperature is between 20 and 30 degree, then prints: “Good weather out there”
#o	If the temperature between 10 and 20, there print: “Nice weather to go for running 
#o	Otherwise prints “It is a bit cold”

temprature = int(input("Please enter a temprature: "))

if temprature>35:
    print("It is to too warm, stay home")
elif temprature<=35 and temprature>30:
    print("It is really a summer day")
elif temprature>20 and temprature<=30:
    print("Good weather out there")
elif temprature<=20 and temprature>10:
    print("Nice weather to go for running")
else:
    print("It is a bit cold")
    
