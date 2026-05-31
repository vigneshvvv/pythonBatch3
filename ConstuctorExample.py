class productInformation:
    id = 0
    productName = ""
    price = 0
    category = ""
    __noOfStock = 0
    
    # No args Constructor
    def __int__(self):
        pass

    # All Args constructor
    def __init__(self, id, productName, price, category):
        self.id = id
        self.productName = productName
        self.price = price
        self.category = category

    def display(self):
        print(self.category)  

    def setNoOfStock(self, stock):
        self.__noOfStock = stock

    def getNooFStock(self):
        return self.__noOfStock          

product1 = productInformation(1, "mobile", 20000, "electronics")
product1.setNoOfStock(10)

product1.place = "chennai"
product2 = productInformation(2, "SamsungMobile", 50000, "electronics")

product1.display()

print(product1.place)
print(product2.productName)

        