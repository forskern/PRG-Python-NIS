#!/usr/bin/env python3


from stockproduct import StockProduct
import cgi
data = cgi.FieldStorage()
func_stock_add = data.getvalue("add_stock")
func_stock_remove = data.getvalue("remove_stock")
func_update = data.getvalue("update_stock")
func_stock_view = data.getvalue("view_stock")
add_to_cart = data.getvalue("cart_add")
remove_from_cart = data.getvalue("cart_remove")
display_cart = data.getvalue("cart_display")
func_bill_invoice = data.getvalue("get_invoice")


# Admin Module

class StockFunction:

    def __init__(self):
        self.product_list = {}                                              # Initialize empty dictionary
        self.cart = {}

    def func_stock_add(self, code, name, description, quantity, price):
        prod_name = StockProduct(code, name, description, quantity, price)  # Create new stock item
        self.product_list[prod_name.code] = prod_name                       # Add stock item to product list
        if data.getvalue("add_stock") == 1:
            func_stock_add()

    def func_stock_remove(self, code):
        for item in self.product_list:                                      # If item is present in product list
            if item.code == code:                                           # Iteration item.code equals "code"
                # self.product_list.remove(item)                            # Removes item from product list
                del item

    def func_update(self, code, quantity, price):
        if quantity < 0:                                                    # Ensure no negative values is accepted
            return -1                                                       # Return error value
        if code in self.product_list:                                       # If code is present in product list
            prod_name = self.product_list[code]                             # Finds prod_name in product list
            prod_name.quantity = quantity                                   # Update quantity
            return prod_name.quantity                                       # Return updated value
        if code in self.product_list:
            prod_name = self.product_list[code]
            prod_name.price = price                                         # Update price
            return prod_name.price                                          # Return updated value
        else:
            return -1                                                       # Return error value

    def func_stock_view(self):
        return self.product_list                                            # Returns overview of products in stock

# Customer Module

    def add_to_cart(self, name, code, quantity, price):
        # self.cart += quantity * price
        # if type(name) == str and quantity > 0:
        #     self.cart.update({name: quantity})
        prod_name = StockProduct(code, quantity)
        self.cart[prod_name.code] = prod_name
        # for item in self.product_list:                                    # For every item in the product list
        #     if item.code == code:                                         # If item code is a code in the product list
        #         self.cart.append(item)*quantity                           # Item added to the cart

    def remove_from_cart(self, code):
        for item in self.cart:                                              # For every item in the cart
            if item.code == code:                                           # If item is present in the cart
                del item                                                    # Remove item from cart

    def display_cart(self):
        return self.cart                                                    # Returns overview of products in cart

    def func_bill_invoice(self):
        gtotal = 0
        for i in self.cart.keys():
            total = int(stock[i])*int(self.cart[i])                         # Total=item price in stock * item in cart
            gtotal += total


if __name__ == '__main__':
    stock = [{"id": 1001,
              "Name": "Audi e-tron",
              "Description": "Full-electrical model",
              "Available": 10,
              "Price": 25000},
             {"id": 1002,
              "Name": "Toyota Avensis",
              "Description": "Mid-size/large family car",
              "Available": 7,
              "Price": 28600},
             {"id": 1003,
              "Name": "Suzuki KingQuad",
              "Description": "Special edition ATV",
              "Available": 22,
              "Price": 8000},
             {"id": 1004,
              "Name": "1931 Harley Davidson",
              "Description": "Model D, Breakout Black",
              "Available": 10,
              "Price": 11000},
             {"id": 1005,
              "Name": "Nissan Leaf",
              "Description": "Pure electric vehicle powered only by electricity",
              "Available": 12,
              "Price": 19000}]


print("Content-Type: text/html\n\n")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Shopping Cart</title>")
print("</head>")
print("<body>")
print("<h1>{} {} {} {}</h1>".format(func_stock_add, func_stock_remove, func_update, func_stock_view))
print("<a href=\"shoppingcart.html\">Back</a>")
print("</body>")
print("</html>")
print(stock)
