from math import sqrt
score = [98, 100, 68, 97, 72, 89, 99, 83, 75, 82, 87, 89, 81, 85, 93]

def find_num_score(score):
        total = 0
        for a in score:
                total +=1
        return total

def find_sum(score):
        sum = 0
        for b in score:
                sum+=b
        return sum

def find_average(score):
        total = 0
        for a in score:
                total +=1
        sum = 0
        for b in score:
                sum+=b
                
        average = sum/total
        return average

def find_median(score):
         total = 0
         srt = sorted(score)
         for a in score:
                total +=1
        

         mid = total//2     
         if total %2:
                median = srt[mid]
         else:
                med = (srt[mid] + srt[mid-1]) / 2
                median = med
         return median
       

def find_lowest(score):
        lowest = score[0]
        for n in score:
                if n < lowest:
                        lowest = n
        return lowest

def find_highest(score):
        highest = score[0]
        for i in range(1, len(score)) :
                if score[i] > highest :
                        highest = score[i]
        return highest

def find_stDev(score, average):
        total = 0
        for a in score:
                total +=1
                
        sumation = score[0]
        for i in range(total):
                diff = score[i] - average
                sumation = sumation + (diff **2)
                variance = sumation /total
                stDev = sqrt(variance)
        return stDev

def main():
        sum = 0
        total = 0
        lowest = 0.0
        highest = 0.0
        median = 0
        stDev = 0
        sum = find_sum(score)
        total = find_num_score(score)
        average = find_average(score)
        lowest = find_lowest (score)
        highest = find_highest(score)
        median = find_median (score)
        stDev = find_stDev (score, average)
        print ("The number of scores: ", total)
        print ("The sum of scores: ", sum)
        print ("The average score is: ", average)
        print ("The median score is: ", median)
        print ("The lowest score is: ", lowest)
        print ("The highest score is: ", highest)
        print ("The standard dev is: ", stDev)
main()
                
                
        
        
        
        


