balance=float(input("Please enter your balance: "))

principle= input("Please enter your current principle: ")
currentPrinciple = float(principle)/100

years=int(input("Please enter amount of years: "))

#Converting Years into months
months = (1/12) * 1/years

firstMonthBalance = (balance * currentPrinciple * months) + balance
print(firstMonthBalance)

secondMonthBalance = (firstMonthBalance * currentPrinciple * months) + firstMonthBalance
print(secondMonthBalance)

thirdMonthBalance = (secondMonthBalance * currentPrinciple * months) + secondMonthBalance
print(thirdMonthBalance)
   
   

    
    
