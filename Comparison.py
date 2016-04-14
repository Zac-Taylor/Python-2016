from math import sqrt

#Comparing int numbers

num1 = 2
num2 = 4

if num1 * num1 ==num2:
    print("2 times 2 is four")

# Comparing floating-point numbers

x = sqrt(2)
y = 2.0

if x * x ==y:
    print("the square root of 2 times itself is 2")
else:
    print("the square root of 2 times itself is not 2 but %.18f" % (x * x))

EPSILON = 1E-14

if abs(x*x-y)< EPSILON :
    print("the square root of 2 times itself is approximately 2")

#Comparing strings

    s ="120"
    t ="20"

    if s==t:
        comparison = "is the same as"
    else:
        comparison = "is not the same as"
    print("The string '%s' %s the string '%s'. " %(s,comparison, t))

    u ="1" + t

    if s!= u:
        comparison = "not "
    else:
        comparison = ""

    print("The strings '%s' and '%s' are %sidentical." %(s,u, comparison))    
