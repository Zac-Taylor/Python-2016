#Zachary Taylor's code IST 282

#Read income and marital status

income = float(input("Please enter your income: "))
maritalStatus =input("Please enter s for single, m for married: ")

#Compute taxes due

if maritalStatus == "s":
    if income >= 0 and income < 8000 :
        tax1 = income * 0.1 + income
    elif income >= 8000 and income < 32000:
        tax1 = (800 + .15) * income + income
    else:
        tax1 = (4400 + .25) * income + income

else:
    if income >= 0 and income < 16000:
        tax1 = .1 * income + income
    elif income >= 16000 and income < 64000:
        tax1 = (1600 +.15 ) * income + income    
    else:
        tax1 = (8800 + .25) * income + income


#Printing the results
print (format (tax1,'.2f'))

