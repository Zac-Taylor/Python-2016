import statistics

class ComputeScore(object):
    
    #Do Not Change any instance variables
    def __init__(self,s): 
        self._scoreL = s # _scoreL points to the list of scores
        self._mean = 0  # mean value
        self._median = 0  # median value
        self._highest = 0 # highest score
        self._stDev = 0  # population standard deviation

        """
        construct is about to call a few methods to compute mean, median
        highest, and standard deviation and set the values of _mean, _median,
        _highest, and _stDev, based upon the computation results. 

        """
        # call the methods below
        self.find_stDev()
        self.find_median()
        self.find_highest()
        self.find_mean()
		
        
    
   
    def find_stDev(self):
        self._stDev = statistics.pstdev(self._scoreL)

    def find_median(self):
        self._median = statistics.median(self._scoreL)

    def find_highest(self):
        self._highest = max(self._scoreL)

    def find_mean(self):
        self._mean = statistics.mean(self._scoreL)
		

    def get_median(self):
        return self._median

    def get_highest(self):
        return self._highest

    def get_mean(self):
        return self._mean
    
       
    def __str__(self):
        return "stand dev: " + str(self._stDev) + "\n" +\
               "median: " + str(self.get_median()) + "\n" +\
               "highest: " + str(self.get_highest()) + "\n" +\
               "mean: " + str(self.get_mean()) +"\n"
     




    	
# Do not change anything in main fucntion!    
def main(): 
    midScore = [100, 80, 90, 99, 100, 79]

    c1 = ComputeScore(midScore)

    print(c1)
    

main()    

