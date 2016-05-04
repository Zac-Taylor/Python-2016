sum = 0.0
count = 0

inputStr=input("Enter an integer or empty string to end: ")

while inputStr != "":
    value = int(inputStr)
    sum = sum + value
    count = count + 1
    inputStr=input("Enter an integer or empty string to end: ")
average = sum/count
print("Sum is: ",sum)
print("Average is: ", average)

    
