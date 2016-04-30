
values=[]

inputUser = input("How many numbers do you want to enter: ")
userNum = int(inputUser)

for loop in range(userNum):
    values.append(float(input("Enter your number: ")))

print("The minumim number is",min(values),"and the sum is:",sum(values))
