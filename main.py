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
        self.percentage_fees = category_fee  # Category fee depends on the category on Amazon
        self.money_fees = 0.25  # Amazon fixed fee of 25p


def main_menu_options():
    """
    Method to return user inputs (there are the main asked inputs for both calculations (eBay and amazon)

    :return: user inputs (price, supplier price and quantity) as int
    """
    
    your_price = int(input("Enter your price:\n"))
    supplier_price = int(input("Enter supplier price:\n"))
    quantity = int(input("Enter quantity:\n"))
    return your_price, supplier_price, quantity


def amazon_category_fee(category_num, your_price):
    """
    Function to return fee percentage for amazon by category
    
    Dict (amazon_fees) guide:
    1. Additive Manufacturing - 12%
    2. Amazon Device Accessories - 45%
    3. Baby Products - 8% if sale is up to £10 or 15% if sale is greater than £10
    4. Beauty - 8% if sale is up to £10 or 15% if sale is greater than £10
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

    Source: https://sellercentral.amazon.co.uk/gp/help/external/H78LW99F4XF3Z38

    :param category_num: int for selection of category
    :return: category percentage fee
    """

    amazon_fees = {1: 0.12, 2: 0.45, 3: 0.08, 4: 0.08, 5: 0.1, 6: 0.15, 7: 0.15, 8: 0.15, 9: 0.15, 10: 0.07, 11: 0.15,
                   12: 0.07, 13: 0.12, 14: 0.15, 15: 0.15}  # Percentage fees by category (find guide above)
    category_fee_depended = [3, 4, 9, 11, 15]  # Category number where percentage depends on price

    # Handling category feeds taking in consideration prices. Some categories hold same conditions, therefore they're in
    # one line of code
    if category_num in category_fee_depended:
        if (category_num == 3 and your_price > 10) or (category_num == 4 and your_price > 10):
            amazon_fees[category_num] = 0.15
        elif category_num == 9 and your_price > 40:
            amazon_fees[category_num] = 0.07
        elif (category_num == 11 and your_price > 100) or (category_num == 15 and your_price > 100):
            amazon_fees[category_num] = 0.08

    return amazon_fees[category_num]


def main():
    menu_status = True  # For menu termination
    while menu_status:
        option = input("Pick an option:\n"
                       "1. Calculate eBay profit\n"
                       "2. Calculate Amazon profit\n"
                       "0. Exit calculator\n")

        # eBay menu
        if option == "1":
            your_price, supplier_price, quantity = main_menu_options()
            product = Ebay(your_price, supplier_price, quantity)
            print("Your profit is " + str(product.calculate_profit()))
            print("Total fees to pay to eBay and PayPal: " + str(product.calculate_fees()))

        # Amazon menu
        elif option == "2":
            your_price, supplier_price, quantity = main_menu_options()
            category_num = int(input("In which category is the product in: \n1. Additive Manufacturing\n"
                                     "2. Amazon Device Accessories\n3. Baby Products\n4. Beautify\n"
                                     "5. Beer, Wine & Spirits\n6. Books, Music, VHS, DVD's\n"
                                     "7. Business, Industrial & Scientific supplies\n8. Car & Motorbike\n"
                                     "9. Clothing\n10. Computers\n11. Computer Accessories\n"
                                     "12.Consumer Electronics\n13. DIY & Tools\n14. Education Supplies\n"
                                     "15. Electronic accessories\n"))
            product = Amazon(your_price, supplier_price, quantity,
                             amazon_category_fee(category_num, your_price * quantity))
            print("Your profit is: " + str(product.calculate_profit()))
            print("Total fees to pay to Amazon: " + str(product.calculate_fees()))

        # Terminate menu
        elif option == "0":
            print("Thank you for using e-commerce calculator.")
            menu_status = False

        else:
            print("Unrecognised option, please try again.")


main()
