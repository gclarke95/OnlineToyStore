# Online Store

The Brief:

The system implementation brief was to design a software system for an online store.  
The system allows customers to search for products sold at the website and add them to their shopping basket. 
Products are sold both by the website itself and several third-party sellers, once customers have finished shopping they go through the checkout process.

Customers have the choice of several delivery options, including standard delivery using the postal service and the company’s own in-house courier service.
Products ordered from third-party sellers at the marketplace do not have access to the in-house courier system. When the delivery options have been chosen, 
then the customer is presented with the payment options, where they can opt to use a credit or debit card, an online payment service (e.g., PayPal) or a gift voucher.

Additionally, customers may also use promotional codes that are periodically issued by the website. 
Customers have the option to store their payment details and so can simply use stored details for each purchase.

## Installation and Database:

This project utilises python and mysql which can be installed using the following commands:

pip install mysql-connector-python-rf
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/codio/install_software/master/python-lsp/install.sh)"
sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev


- A database with the name **onlinestore** has been created in codio for this project.
  If you wish to run this project outside of codio, you will need to create a new MySQL database
  with the name **onlinestore**. 
  
Code for the database incase it is not operating in the codio environment is as follows:

CREATE DATABASE onlinestore;

CREATE TABLE onlinestore.product(
  id INT NOT NULL AUTO_INCREMENT,
  name    VARCHAR(100) NOT NULL,
  price   DOUBLE NOT NULL,
  quantity INT NOT NULL,
  supplier VARCHAR(45) NOT NULL,
  PRIMARY KEY (id));

INSERT INTO onlinestore.product (id, name, price, quantity, supplier) VALUES ('1', 'lego', '10.00', '100', '3P');
INSERT INTO onlinestore.product (id,name, price, quantity, supplier) VALUES ('2', 'action man', '15.00', '100', 'WS');
INSERT INTO onlinestore.product (id,name, price, quantity, supplier) VALUES ('3', 'puzzle', '05.00', '200', '3P');
INSERT INTO onlinestore.product (id,name, price, quantity, supplier) VALUES ('4', 'book', '10.00', '50', 'WS');
INSERT INTO onlinestore.product (id,name, price, quantity, supplier) VALUES ('5', 'playdough', '12.00', '150', '3P');
INSERT INTO onlinestore.product (id,name, price, quantity, supplier) VALUES ('6', 'dolls house', '40.00', '150', 'WS');
INSERT INTO onlinestore.product (id,name, price, quantity, supplier) VALUES ('7', 'pencil case', '10.00', '120', '3P');

CREATE TABLE onlinestore.shopping_cart (
   cartid     INT NOT NULL AUTO_INCREMENT,
   price      DOUBLE NULL,
   qty        INT,
   productid  INT NOT NULL,
   PRIMARY KEY (`cartid`));


# Running the program:

To start the program run the homepage.py file.

The homepage file encapsulate all the python code using the import function.

The user is then able to choose from the menu to view products, add to cart and checkout.

The exit option, breaks the program, and prints a goodbye message.

Each python file represents a class in the onlinestore (see below);

- Payment
- Products
- Orders
- Shopping_cart
- Checkout

The product and shopping_cart classes draw data from the database. 

Due to time constraints I did not have time to implement all of the classes using the database but I have shown the classes anyway to illustrate
my thinking,e.g. the payment class, I have not included them when running the system so the system is able to run. 


Testing:

- Automated testing was undertaken with automation anywhere
- Testing screenshots are also provided within the testing folder as well as using pylint 

# Limitations:

Unfortunately due to time constraints and being relatively new to coding I did not have time to implement all of the onlinestore 
system requirements such as:

- Storing payment details ; and
- Delivery depending on supplier id.

I have included the functions I created to implement these, but I did not manage to create all the neccessary classes in the onlinestore
database in order to implement them all properly. I have included some classes and functions which are not used in the final
program so that my thinking can be illustrated. 

I based my onlinestore system on my class diagram I produced in Unit 7, which on reflection should have included 
a user class, with customer and sellers inheriting from this class which would upload products to the website / purchase products.

I have created functions within the store to upload and remove products from the database but this is not limited to sellers.

Finally a limitation within the code I have noticed through testing is with the shopping cart, as it does not create a new shopping cart
each time someone starts the program, therefore people are adding to an already existing cart in the database, this is due to setting up the
shopping cart table incorrectly in the database. 

When returning prices too, sometimes there is an error with the correct price, this is shown within the testing screenshots. 

These limitations are something I will fix when time allows for my development. 

References:  

Programiz (n.d) Python Objects and Classes Available from:
https://www.programiz.com/python-programming/class [Accessed 10 September 2021].