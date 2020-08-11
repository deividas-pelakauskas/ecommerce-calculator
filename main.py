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


def amazon_cateogry_fee(category_num, your_price):
    """
    Function to return fee percentage for amazon by category
    
    Dict (amazon_fees) guide:
    1. Additive Manufacturing - 12%
    2. Amazon Device Accessories - 45%
    3. Baby Products - 8% if sale is up to £10 or 15% if sale is greater than £10
    4. Beautify - 8% if sale is up to £10 or 15% if sale is greater than £10
    5. Beer, Wine & Spirits - 10%
    6. Books, Music, VHS, DVD's - 15%
    7. Business, Industrial & Scientific supplies - 15%
    8. Car & Motorbike - 15%
    9. Clothing - 15% if sale is up to £40 or 7% if sale is greater than £40
    10. Computers - 7%
    11. Computer Accessories - 15$ if sale is up to £100 or 8% if sale is greater than £100
    12. Consumer Electronics - 7%
    13. DIY & Tools - 12%
    14. Education Supplies - 15%
    15. Electronic accessories - 15% if sale is up to £100 or 8$ if sale is greater than £100
    
    :param category_num: int for selection of category
    :return: category percentage fee
    """

    amazon_fees = {1: 0.12, 2: 0.45, 3: 0.08, 4: 0.08, 5: 0.1, 6: 0.15, 7: 0.15, 8: 0.15, 9: 0.15, 10: 0.07, 11: 0.15,
                   12: 0.07, 13: 0.12, 14: 0.15, 15: 0.15}  # Percentage fees by category (guide is in the function
    # comments above)
    category_price_depended = [3, 4, 9, 11, 15]  # Category number where percentage depends on price

    # Handling category feeds taking in consideration prices. Some categories hold same conditions, therefore they're in
    # one line of code
    if category_num in category_price_depended:
        if (category_num == 3 and your_price > 10) or (category_num == 4 and your_price > 10):
            amazon_fees[category_num] = 0.15
        elif category_num == 9 and your_price > 40:
            amazon_fees[category_num] = 0.07
        elif (category_num == 11 and your_price > 100) or (category_num == 15 and your_price > 100):
            amazon_fees[category_num] = 0.08

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
        your_price = int(input("Enter your price:\n"))
        print(amazon_cateogry_fee(your_cat, your_price))


main()
