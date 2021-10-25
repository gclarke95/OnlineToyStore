from sql_connection import get_sql_connection
from products import *
from shopping_cart import *
from checkout import *

class Main(): 
    def StartMessage(self):
        while True:
            print('''
                     Welcome to The Toy Store

                     Please select which action you would like:
                     1. View store products
                     2. Add item to Shopping Cart
                     3. View Shopping Cart
                     4. Remove item from Shopping Cart
                     5. Checkout
                     6. Exit
                      ''')

            selection = int(input("Select which action: "))
            if selection == 1:
                print()
                selection2=input("Enter search text or return for full product list  ")
                get_all_products(selection2)
                print()
                selection2 = input("Enter any character to continue ")

            elif selection == 2:
                print()
                add_product()
                print()
                selection2 = input("Enter any character to continue ")

            elif selection == 3:
                print()
                displaycart()
                print()
                selection2 = input("Enter any character to continue ")

            elif selection == 4:
                print()
                removeitem()
                print()
                selection2 = input("Enter any character to continue ")

            elif selection == 5:
                print()
                checkout()
                print()
                selection2 = input("Enter any character to continue ")

            elif selection == 6:
                print()
                print("              Thank you for visiting The Toy Store, we hope to see you again")
                break

            else:
                print("Invalid selection, please try again")
                print()
                selection2 = input("Enter any character to continue ")


startmessage = Main()
startmessage.StartMessage()
