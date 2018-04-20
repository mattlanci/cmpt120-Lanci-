#Matthew Lanci
#CMPT120
#Lab 9


productNames = [ "Ultrasonic range finder"
                  , "Servo motor"
                  , "Servo controller"
                  , "Microcontroller Board"
                  , "Laser range finder"
                  , "Lithium polymer battery"
                  ]
productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]
products =  [ ("Ultrasonic range finder", 2.50, 4), ("Servo motor", 14.99, 10
              ),("Servo controller", 44.95, 5), ("Microcontroller Board", 34.95
              , 7), ("Laser range finder", 149,99, 2), ("Lithium Polymer Battery"
              , 8.99, 8)
              ]
class Product:
    def __init__ (self, name, price, productquantity):
        
        self.name = name
        self.price = price
        self.productquantity = productquantity

    def stock(self, amount):
        if self.productquantity >= amount:
            return True
        return False

    def cost(self, count):
        return self.price * count

    def remainder(self, count):
        self.productquantity = self.productquantity - count
        return self.productquantity
        
Finder = Product(products[0][0],products[0][1],products[0][2])
Motor = Product(products[1][0],products[1][1],products[1][2])
Controller = Product(products[2][0],products[2][1],products[2][2])
Board = Product(products[3][0],products[3][1],products[3][2])
lazer = Product(products[4][0],products[4][1],products[4][2])
battery = Product(products[5][0],products[5][1],products[5][2])
prodList = [Finder,Motor,Controller,Board,lazer,battery]

 def printStock():
   print()
   print("Available Products")
   print("------------------")
   for i in range(0,len(productNames)):
       if productQuantities[i] > 0:
           print(str(i)+")",productNames[i], "$", productPrices[i])
print()
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if prodList[i].productquantity > 0:
            print(str(i)+")",prodList[i].name, "$", prodList[i].price)
    print()

 def main():
   cash = float(input("How much money do you have? $"))
   while cash > 0:
    cash = float(input("How much money do you have? $ "))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you want to buy: ").split(" ")
       if vals[0] == "quit": break
       if vals[0] == "quit":
           break
        prodId = int(vals[0])
        count = int(vals[1])
       if productQuantities[prodId] >= count:
       if cash >= productPrices[prodId]:
                productQuantities[prodId] -= count
                cash -= productPrices[prodId] * count
                print("You bought", count, productNames[prodId]+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else: print("Sorry, you cannot afford that product.")
       else: print("Sorry, we are sold out of", productNames[prodId])
       if prodList[prodId].stock(count):
            if cash >= prodList[prodId].price:
                prodList[prodId].remainder(count)
                cash -= prodList[prodId].cost(count)
                print("You bought", count, prodList[prodId].name+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
       else:
           print("Sorry, we are sold out of", prodList[prodId].name)
