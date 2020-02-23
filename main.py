# Date: 02/2020
# Author: Deividas Pelakauskas

class Product:
    # All percentage fees added up
    percentage_fees = 0

    # All fixed money fees added up
    money_fees = 0

    def __init__(self, my_price, supplier_price, quantity):
        self.my_price = my_price
        self.supplier_price = supplier_price
        self.quantity = quantity

    # Calculate marketplace fees
    def calculate_fees(self):
        return self.quantity * self.my_price * self.percentage_fees + self.money_fees

    # Calculate profit taking away all fees
    def calculate_profit(self):
        price_after_fees = self.quantity * self.my_price - self.calculate_fees()
        return price_after_fees - self.quantity * self.supplier_price


class Ebay(Product):

    def __init__(self, my_price, supplier_price, quantity):
        super().__init__(my_price, supplier_price, quantity)
        self.percentage_fees, self.money_fees = self.ebay_fees()

    # Ebay final value fee is capped at £250
    def ebay_fees(self):
        # Ebay final value fee is capped at £250
        if self.my_price * self.quantity > 2500:
            percentage_fees = 0.034  # 3.4% PayPal
            money_fees = 250.30  # £250 + 30p fixed PayPal fee
            return percentage_fees, money_fees
        else:
            percentage_fees = 0.134  # eBay 10% and 3.4% PayPal
            money_fees = 0.30  # 30p fixed PayPal fee
            return percentage_fees, money_fees


class Amazon(Product):

    def __init__(self, my_price, supplier_price, quantity, category_fee):
        super().__init__(my_price, supplier_price, quantity)
        self.percentage_fees = category_fee  # Category fee depends on the category on Amazon
        self.money_fees = 0.20  # Amazon fixed fee of 20p


# Testing
# product = Ebay(2501, 2000, 1)
# productAmz = Amazon(15, 12, 1, 0.134)
# print(product.calculate_profit())
# print(productAmz.calculate_profit())
# print(product.money_fees)

main_menu = 0
main_menu = int(input("Pick an option:\n"
                      "1. Calculate eBay profit\n"
                      "2. Calculate Amazon profit\n"))
if main_menu == 1:
    your_price = int(input("Enter your price:\n"))
    supplier_price = int(input("Enter supplier price:\n"))
    quantity = int(input("Enter quantity sold:\n"))
    product = Ebay(your_price, supplier_price, quantity)
    print("Your profit is - " + str(product.calculate_profit()))