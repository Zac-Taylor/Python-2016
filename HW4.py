def find_num_score(score):
    return 83


def main():
    sum = 0
    num_score = 0 #number of midterm grades
    
    average = 0.0
    lowest = 0.0
    highest = 0.0
    median = 0.0
    variance = 0.0
    score = [98, 100, 68, 97, 72, 89, 99, 83, 75, 82, 87, 89, 81, 85, 93]

    # function calls/invocations
    
    #num_score = find_num_score(score) #call by reference
    for i in score:
        num_score+= 1
    #sum = find_sum(score)
    for x in score:
        sum+=x
    
    #average = find_average(num_score,sum) # call by value 
    average = sum/num_score
    
    #median = find_median (score)
    srt= sorted(score)
    mid = num_score//2
    if num_score %2:
        median = srt[mid]
    else:
        med = (srt[mid] + srt[mid-1]) / 2
        median = med
    #lowest = find_lowest (score)
    lowest = score[0]
    for n in score:
        if n < lowest:
            lowest = n
    #highest = find_highest(score)
    highest = score[0]
    for m in score:
        if m > highest:
            highest = m
    #grades_variance(score)
    variance = 0
    for scores in score:
        variance += (average - scores) ** 2
    variance /= num_score
    variance

    #stDev = find_stDev(score)
    stDev = variance**(.5)
  
    print (" *********** Display the computation result ***********")

    print ("The number of scores: ", num_score)
    print ("The sum of scores: ", sum)
    print ("The average score is: ", average)
    print ("The median score is: ", median)
    print ("The lowest score is: ", lowest)
    print ("The higest score is: ", highest)
    print ("The standard dev is: ", stDev)
  
main()
