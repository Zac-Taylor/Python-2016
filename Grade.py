studentGrade = float(input("Please enter your grade: "))

if studentGrade >=90:
    print("You got an A!")
elif studentGrade < 90 and studentGrade > 80:
    print ("You got an B!")
elif studentGrade < 80 and studentGrade > 70 :
    print ("You got an C!")
elif studentGrade < 70 and studentGrade > 60 :
    print ("You got an D")
else :
    print ("YOu ffailed tha class ")
