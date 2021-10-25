#creating order class
class Order:
    def __init__(self, orderID, order_date, supplier, orderStatus):
        self.orderID = orderID
        self.order_date = order_date
        self.supplier = supplier
        self.orderStatus = orderStatus

    def show(self):
        print(self.orderID, self.order_date, self.supplier, self.orderStatus)

orderstatus=[]

orderstatus.append(Order(orderID, orderTotal, orderStatus))  #Adding order details - unfortunately I couldn't manage to succeed with its implementation.

#the postage function is a function I had implementedwhich looked at the supplier for each
#product object and provided different delivery options dependent on supplier, this worked in the python program before
#I added the mysql database unfortunately I did not have time to implement it properly using the database as 
# I needed to add more tables in the database 

  def postage(self):
      for obj in shopping_cart:
          if obj.supplier == "3P":
             print("Your order will be sent via the Post Service")

          if obj.supplier == "WS":
              choice = int(input('''Please select your delivery method
                                  1. Postal Service
                                  2. In-house courier: '''))
              if choice == 1:
                  print("Your order will be sent via the Post Service")

              if choice == 2:
                  print("Your order will be sent via our in-house courier")

