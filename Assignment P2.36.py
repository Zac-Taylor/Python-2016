balance= input("Please enter your current balance:" + " " )
currentBalance =float(balance)

principle= input("Please enter your current principle:" + " ")
currentPrinciple = float(principle)/100

years = input("How many years are on the account?" + " ")
amountYears = float(years)

yearBalance = (currentBalance * amountYears)*1

newBalance = (currentBalance * currentPrinciple)/12

newCurrentBalance = newBalance + currentBalance

realCurrentBalance = (newCurrentBalance * currentPrinciple)/12

secondCurrentBalance= realCurrentBalance + newCurrentBalance

nowBalance = (secondCurrentBalance * currentPrinciple)/12

thirdCurrentBalance = (nowBalance+secondCurrentBalance)

print("Your first month balance is:" + " ",newCurrentBalance)
print("Your second month balance is:" + " ",secondCurrentBalance)
print("Your third month balance is:" + " ",thirdCurrentBalance)
    
    
