class computer:

    def __init__(self):
        self.__maxprice = 900 

    
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))


    def setMaxPrice(self,price):
        self.__maxprice = price


mycomputer = computer()
mycomputer.__maxprice = 500
mycomputer.sell()
print()

mycomputer.setMaxPrice(500)
mycomputer.sell()