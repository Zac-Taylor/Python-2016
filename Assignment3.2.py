
values=[]

inputUser = input("How many numbers do you want to enter: ")
userNum = int(inputUser)

for loop in range(userNum):
    values.append(float(input("Enter your number: ")))

print(sum(values)/len(values), sum(values))
