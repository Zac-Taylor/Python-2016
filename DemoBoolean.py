x = float(input("Enter a decimal number: "))
y = float(input("Enter a Second nummber: "))

if x==y:
    print("They are the same. ")
else:
    print("The first number is smaller")

if -0.01 < x-y and x-y < 0.01 :
    print("The numbers are too close together")

if x==y + 1 or x==y -1:
    print("The numbers are one apart")

if x > 0 and y>0 or x <0 and y <0:
    print("The numbers have the same sign")
else:
    print("The numbers have different signs")
