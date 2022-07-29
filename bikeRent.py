class bikeShop:

    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,q):

        if q<=0:
            print("enter the +ve value ")
        elif q>self.stock:
            print("enter the value (less than stock)")

        else:
            self.stock=self.stock-q
            print("Total Prices",q*100)
            print("total bikes",self.stock)

while True:
    obj=bikeShop(100)
    uc=int(input('''
1 Display stocks
2 rent a bike
3 exit    
    '''))

    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("enter the Qty:--"))
        obj.rentForBike(n)
    else:
        break
