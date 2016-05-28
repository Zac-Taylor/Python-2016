#def find_num_score(score):
    #for loop

#def find_sum(score): do one problem at a time
 #    use loop


#def main():
    #sum = 0
    #num_score = 0 #number of midterm grades
    
average = 0.0
lowest = 0.0
highest = 0.0
median = 0.0
score = [98, 100, 68, 97, 72, 89, 99, 83, 75, 82, 87, 89, 81, 85, 93]
count = 0
    

    # function calls/invocations
   # num_score = find_num_score(score) #call by reference
    #sum = find_sum(score)
    
    #average = find_average(num_score,sum) # call by value 
sum = 0
num_score = 0

inputStr = input(" Enter score value")

while inputStr != "":
    value = int(inputStr)
    sum = sum +value
    num_score = num_score + 1
    inputStr = input ("Enter score value")

average = sum/num_score
    #median = find_median (score)

    #lowest = find_lowest (score)
#lowest = int(input("Enter grade or empty string to end: "))
#count = 1
#inputStr = input("Enter grade or empty string to end: ")

#while inputStr != "":
    #value = int(inputStr)
   # if value < lowest:
      #  lowest = value
   # count = count + 1
   # inputStr = input("Enter grade or empty string to end: ")
    #highest = find_highest(score)

    #stDev = find_stDev(score)
  
    #print (" *********** Display the computation result ***********")

print ("The number of scores: ", num_score)
print ("The sum of scores: ", sum)
print ("The average score is: ", average)
    #print ("The median score is: ", median)
    #print ("The lowest score is: ", lowest)
    #print ("The higest score is: ", highest)
    #print ("The standard dev is: ", stDev)
  
#main()
