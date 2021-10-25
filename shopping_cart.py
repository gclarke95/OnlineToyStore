#Creating shopping cart class
from sql_connection import get_sql_connection
from products import *

def add_product(): #function to add product to shopping cart 
        prod     = input("Select the product ID you wish to add to your shopping cart: ") #user input to select product
        inputqty = input("How many would you like to purchase ? ")  #user select quantity to add to cart 
        connection = get_sql_connection()
        cursor = connection.cursor(buffered=True)
        query = ("SELECT * FROM product WHERE id="+str(prod)+" LIMIT 1;")
        cursor.execute(query)
        resultrow = cursor.fetchone()

        if resultrow:              #checking to see if a record for this product exits in cart already

            cursor = connection.cursor(buffered=True)
            cursor.execute("SELECT * FROM shopping_cart WHERE productid = "+str(prod) +" LIMIT 1;")
            rresult = cursor.fetchone()
            if  rresult:         #if record doesn't exist create one in the cart else just increment the quantity by x
                query = ("UPDATE shopping_cart SET qty = qty + "+str(inputqty)+
                         " WHERE productid = "+ str(resultrow[0])+";")
            else:
                query = ("INSERT INTO shopping_cart(price,qty,productid) "
                         "VALUES ( "+ str(resultrow[0]) +","+  str(inputqty) + ","+ str(resultrow[0])+ ");"  #cartid auto ??
                         )
            cursor = connection.cursor(buffered=True)
            cursor.execute(query)
            connection.commit()
            cost=resultrow[2]*float(inputqty)
            print(resultrow[1], "has been added to you basket at a cost of £" ,cost)
        else:
            print("Error: The selected product has not been found - Select again")

def displaycart(): #function to display contents of shopping_cart
    connection = get_sql_connection()
    cursor = connection.cursor()
    query = ("SELECT * FROM shopping_cart ;")  # retrieve the whole shopping cart
    cursor.execute(query)
    resultrow = cursor.fetchall()
    cost = 0
    for row in resultrow:    #print the whole shopping cart and sum the costs
        print("Id=", row[0], "\t", "Price=   £", row[1], "\t", "Qty = ", row[2] ) #need to get the name by joining tables
        cost = (row[1]*row[2]) + cost      # (price * qty) + running total
    print("The total cost of items in your shopping cart is currently £",cost)

def removeitem(): #function to remove items from shopping_cart
    prodid = input("Select the product ID you wish to remove from your shopping cart: ")
    connection = get_sql_connection()
    cursor = connection.cursor()
    query = ("DELETE FROM shopping_cart WHERE productid=" + str(prodid))
    cursor.execute(query)
    connection.commit()
    print("Product ID " + prodid + " has been removed from your shopping cart ")

