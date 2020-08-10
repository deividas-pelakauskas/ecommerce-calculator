# Date: 02/2020
# Author: Deividas Pelakauskas

class Product:

    # All percentage fees added up (0 by default)
    percentage_fees = 0

    # All fixed money fees added up (0 by default)
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
        self.percentage_fees = category_fee / 100  # Category fee depends on the category on Amazon
        self.money_fees = 0.25  # Amazon fixed fee of 25p



def amazon_cateogry_fee(category_num):
    """
    Function to return fee percentage for amazon by category
    
    Dict (amazon_fees) guide:
    1. Additive Manufacturing - 12%
    2. Amazon Device Accessories - 45%
    3. Baby Products - 8% if sale is up to £10 or 15% if sale os greater than £10
    
    :param category_num: int for selection of category
    :return: category percentage fee
    """
    amazon_fees = {1: 0.12, 2: 0.45, 3: 0.08}
    return amazon_fees[category_num]


def main():
    main_menu = int(input("Pick an option:\n"
                          "1. Calculate eBay profit\n"
                          "2. Calculate Amazon profit\n"))
    # eBay menu
    if main_menu == 1:
        your_price = int(input("Enter your price:\n"))
        supplier_price = int(input("Enter supplier price:\n"))
        quantity = int(input("Enter quantity sold:\n"))
        product = Ebay(your_price, supplier_price, quantity)
        print("Your profit is " + str(product.calculate_profit()))

    # Amazon menu
    elif main_menu == 2:
        your_price = int(input("Enter your price:\n"))
        supplier_price = int(input("Enter supplier price:\n"))
        quantity = int(input("Enter quantity sold:\n"))
        fee_percentage = int(input("Enter category fee percentage:\n"))
        product = Amazon(your_price, supplier_price, quantity, fee_percentage)
        print("Your profit is " + str(product.calculate_profit()))

    elif main_menu == 3:
        your_cat = int(input("Test:\n"))
        print(amazon_cateogry_fee(your_cat))

main()