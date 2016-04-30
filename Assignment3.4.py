a= 0
b= 0

while a < 0  or b<= a:
    a = int(input("Enter the number for A: "))
    b = int(input("Enter the number for B: "))

print ("The sum of the even numbers between the two numbers is:",sum([x for x in range(a, b+1) if x % 2 == 0]))
