odds = 0
userInput = input("Please enter a number:")

while userInput != (""):
    numbers = int(userInput)
    if numbers > 0 and numbers % 2 ==1:
        odds= odds + 1
    print("There were" ,odds,"values")
    userInput = input("Please enter a number:")
    
    
    
        
    
