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

    def calculate_fees(self):
        return self.quantity * self.my_price * self.percentage_fees + self.money_fees

    def calculate_profit(self):
        price_after_fees = self.quantity * self.my_price - self.calculate_fees()
        return price_after_fees - self.quantity * self.supplier_price

class Ebay(Product):

    percentage_fees = 0.134
    money_fees = 0.20

class Amazon(Product):

    money_fees = 0.20

    def __init__(self, my_price, supplier_price, quantity, category_fee):
        super().__init__(my_price, supplier_price, quantity)
        self.percentage_fees = category_fee


product = Ebay(15, 12, 1)
productAmz = Amazon(15, 12, 1, 0.134)
print(product.calculate_profit())
print(productAmz.calculate_profit())