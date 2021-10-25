#creating class products for store products
from sql_connection import get_sql_connection

def get_all_products(productname): #retrieves all products from onlinestore database 
        connection = get_sql_connection()
        cursor = connection.cursor()
        if productname:
            query = ("SELECT * FROM `onlinestore`.product WHERE name like '%"+productname+"%';")
        else:
            query = ("SELECT * FROM `onlinestore`.product;")
        cursor.execute(query)
        response = cursor.fetchall()
        for row in response:
            print ("Id=",row[0],"\t","Name=",row[1] , "\t","Price =£",row[2],"\t"," Supplier",row[4])

        return response

def insert_new_product(connection, product): # function to allow new products to be added to database
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, price, quantity, supplier)"
             "VALUES (%s, %s, %s, %s)")
    data = (product['name'], product['price'], product['quantity'], product['supplier'],)

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id): # function to allow products to be deleted from database
    cursor = connection.cursor()
    query = ("DELETE FROM products where id=" + str(id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid










