#HW5 part a example kind


class Pizza():   #create class then constructor
    def __init__(self, brand, size, numT, price, ):   #constructor
        self._brandName = brand    #attribute
        self._size = size
        self._numTopping = numT
        self._price = price

        self.calculate_cost()



    #get methods 1 for each attribute same for set method; encapsulation

    def get_brandName(self):
        return self._brandName

    def get_size(self):
        return self._brandName

    def get_numT(self):
        return self._numT

    def get_price(self):
        return self._price



    #set method
    def set_brandName(self, name):
        self._brandName = name

    def set_size(self, size):
        self._size = size

    def set_numT(self, toppings):
        self._numT = toppings

        def set_price(self, cost):
            self._price = cost

       

    def __str__(self):
        return self._brandName + " " + self._size + \
        " " + str(self._numTopping) + " " + str(self._price)

    def calculate_cost(self):
        if self._brandName == "Pizza Hut":
            if  self._size == "small":
                cost = 10 + (1 * self._numTopping)
            else:
                cost = 16 + (3 * self._numTopping)
        else:
            if  self._size == "small":
                self._price = 12 + (2 * self._numTopping)
            else:
                self._price = 16 + (3 * self._numTopping)
                
    
        

        

    

    

def main():
    print ("first line")

    p1 = Pizza("Pizza Hut", "small", 3, 12.50) #create object type: pizza p1 is refernce var

    p2 = Pizza("Dominos", "large", 5, 13.99)

    print(p1)
    print(p2)

    
main()
    
    
    
