#Zachary Taylor's code IST 282
income = float(input("Please enter your income: "))

if income == 50000 :
    print("Your income tax is ", income * .01)
elif income > 50000 and income < 75000:
    print("Your income tax is ", income * .02)
elif income > 75000 and income < 1000000:
    print("Your income tax is ", income * .03)
elif income >1000000 and income < 250000:
    print("Your income tax is ", income * .04)
elif income > 250000 and income < 500000:
    print("Your income tax is ", income * .05)
else:
    print("Your income tax is ", income * .06)
    
