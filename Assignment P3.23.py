#Zachary Taylor's code IST 282
income = float(input("Please enter your income: "))

if income == 50000:
     print ("The tax payable would be: " ,income *0.01)
elif income <= 75000:
     print ("The tax payable would be: " ,income *0.02)
elif income <= 100000:
     print ("The tax payable would be: " ,income *0.03)
elif income <= 250000:
     print ("The tax payable would be: " ,income *0.04)
elif income <= 5000000:
     print ("The tax payable would be: " ,income *0.05)
else:
    print ("The tax payable would be: " ,income *0.06)
