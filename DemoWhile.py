#Create constant variables

RATE = 5.0
INITIAL_BALANCE = 1000.0
TARGET = 2 * INITIAL_BALANCE

#Initializing variables used with the while loop

balance=INITIAL_BALANCE
year=0

#Count the years required for the investment to double

while balance < TARGET :
    year =year + 1
    interest = balance * RATE /100
    balance = balance + interest

    #print the result
print("The investment doubled after",year,"year.")
