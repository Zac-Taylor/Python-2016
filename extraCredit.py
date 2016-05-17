numA = 0
numB = 0
numC = 0
numF = 0
total = 0
count = 0

grade = float(input("Enter Your score or -1 to end: "))
while grade != -1:
    if grade >= 90:
        numA = numA + 1
    elif grade >= 80:
        numB = numB + 1
    elif grade >= 70:
        numC = numC + 1
    else:
        numF = numF + 1
    total = total + grade
    count = count + 1
    grade = float(input("Enter Your score or -1 to end: "))

print("The # of As student's:",numA)
print("The # of Bs student's:",numB)
print("The # of Cs student's:",numC)
print("The # of Fs student's:",numF)
print("Average midterm score is: ",total/count)
        
    
        
