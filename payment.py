#creating the payment class which the different payment methods inherit from, 
#I then wanted to sit up multiple functions that could be called depending on
#the customers chosen payment option,
#I also wanted to create a function to store payment details but did not have time to implement this, this file
#is not used in the program but I wanted to include it to show my thinking

class Payment:
    def __init__(self, payment_amount, order_id):
        self.payment_amount = payment_amount
        self.order_id = order_id

    def show(self):
        print(f"Your Order ID is {self.order_id} Your Order total is {self.payment_amount}")

class Card(Payment):  #card class inherited from payment
    def __init__(self,card_no):
        self.card_no = card_no

class Giftvoucher(Payment):
    def __init__(self,voucher_no):
        self.voucher_no = voucher_no

class Paypal(Payment):
    def __init__(self, paypal_no):
        self.paypal_no = paypal_no

    def promotional_code():
        p_code = int(input("Please enter your promotional code:"))
        print("valid code")

    def gift_voucher(self):
        g_code = int(input("Please enter your gift code:"))
        print("valid code")

    def credit_debit_card():
        card = int(input("Please enter your credit or debit card number:"))
        print("Valid code")

    def paypal():
        paypal = int(input("Please enter your PayPal number:"))
        print("Valid code")


    def choosing_to_store_payment_details():  #function which allows users to store their payment details for future use 
        choosing = int(input("If you want to store payment details, please enter 1. If you don't, enter 2:"))
        if choosing == 1:
            paying.stored_payment_details()
            print("Your payment details have been successfully stored")
        if choosing == 2:
            print("Your payment details have not been stored")