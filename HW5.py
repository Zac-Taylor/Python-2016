<<<<<<< HEAD
class Pizza():
        def __init__(self,brand,size,numT):
                self._brandName = brand
                self._size = size
                self._numTopping = numT
        
        def set_brandName(self,brand):
                self._brandName = brand
        def set_size(self,size):
                self._size = size
        def set_numTopping(self,numT):
                self._numTopping = numT
                
        def get_brandName(self):
                return set._brandName
        def get_size(self):
                return set._size
        def get_numTopping(self):
                return self._numTopping
        
        def calculateCost(self):
                cost = 0
                if self._brandName =="Pizza Hut":
                        if self._size =="Small":
                                cost = 10 + (1*self._numTopping)
                        else:
                                cost = 14 + (3 *self._numTopping)
                else:
                        if self._size =="Small":
                                cost = 12 + (2 *self._numTopping)
                        else:
                                cost = 16 + (3 *self._numTopping)
                return float(cost)
        
        def __str__(self):
                return self._brandName + ";" + self._size +" "\
                       "Cost is: $" + str(self.calculateCost())
        
def main():
        p1 = Pizza("Pizza Hut","Small",3)
        p2 = Pizza("Dominos","Large",2)
        print(p1)
        print(p2)
        
main()
        
=======
class Pizza():
    def __init__(self,brand,size, numT):
        self._brandName = brand
        self._size = size
        self._numTopping = numT

    def set_brandName(self, brand):
        self._brandName = brand
    def set_size (self, size):
      self._size = size
    def set_numTopping (self, numT):
        self._numTopping = numT

    def get_brandName(self):
      return self_brandName
    def get_size(self):
        return self._size
    def get_numTopping(self):
      return self.numTopping

    def calculateCost(self):
      cost = 0
      if self._brandName == "Pizza Hut":
            if self._size =="Small":
                cost = 10 + (1 * self._numTopping)
            elif self._size == "Large":
                cost = 14 + (3 * self._numTopping)
              
      if self._brandName == "Dominos":
            if self._size == "Small":
                cost = 12 + (2 * self._numTopping)
            elif self._size == "Large":
                cost = 16 + (3 * self._numTopping)              
      return float(cost)

    def __str__(self):
      return self._brandName + "; " + self._size + " "\
            "Cost is: $" + str(self.calculateCost())

    def main():
        p1 = Pizza("Pizza Hut","Small",3)
        p2 = Pizza("Dominos","Large",2)
        print("Your pizza is:", p1)
        print("Your pizza is:", p2)
 
    main()
      

    

    
        
>>>>>>> 75b00b4c2e3cc254b35589927ee27c73a9cd581a
