#class checkout
#within this function I should have been able to connect to the databse and have stored payment details for 
#customers as well as this looked up the product supplier which would then impact which delivery method customers could use
def checkout(): #function which allows users to select how they pay for their purchase 
    payment_method = int(input('''Please select how you would like to pay for your purchase: 
                                1. Gift Voucher
                                2. Credit / Debit Card
                                3. Paypal
                                4. Promotional Code
                                '''))

    if payment_method == 1:
       input("Please enter your gift voucher code: ")
       print("Thank you, your order is now being processed")

    elif payment_method == 2:
        input("Please enter your Credit / Debit card information: ")
        print("Thank you, your order is now being processed")

    elif payment_method == 3:
         input("Please enter your PayPal number: ")
         print("Thank you, your order is now being processed")

    elif payment_method == 4:
         input("Please enter your promotional code: ")
         print("Thank you, your order is now being processed")

    else:
        print("Please select a valid payment method")

