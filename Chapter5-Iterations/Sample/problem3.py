# Write a Python program that count how many numbers between 100 and 999 exists 
# whose total sum of its digit is less than 15 and bigger than 10 (including 10 and 15).

count = 0

for i in range(100, 999):
    result = 0
    for digit in str(i):
        result = result + int(digit)
    
    if result >= 10 and result <= 15:
        # print(i)
        count = count + 1

print("There is %d numbers whose meet the requirement" %count)

