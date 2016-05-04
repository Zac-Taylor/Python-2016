smallest= 0
count = 0

smallest = int(input("Enter an integer or empty string to end: "))
count = 1
inputStr=input("Enter an integer or empty string to end: ")

while inputStr != "":
    value = int(inputStr)
    if value < smallest:
        smallest = value
    count = count + 1
    inputStr=input("Enter an integer or empty string to end: ")
print("the smallest is: ",smallest)
print("the count is: ",count)

    

