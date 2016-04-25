#Zachary Taylor's code IST 282

#Read income and marital status

income = float(input("Please enter your income: "))
maritalStatus =input("Please enter s for single, m for married: ")

#Compute taxes due

if maritalStatus == "s":
    if income <= 8000 :
        tax1 = income * 0.1 
    elif income >8000 and income <= 32000:
        tax1 = 800 + (income -8000) *.15
    else:
        tax1 = 4400 +(income -32000)* .25

else:
    if income <= 16000:
        tax1 = income * 0.1
    elif income >16000 and income <= 64000:
        tax1 = 1600 + (income - 16000) *.15     
    else:
        tax1 = 8800 + (income - 64000) *.25


#Printing the results
print (format (tax1,'.2f'))

