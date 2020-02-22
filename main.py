# Date: 02/2020
# Author: Deividas Pelakauskas

class Product:

    def __init__(self, sku, supplier, my_price, supplier_price, quantity):
        self.sku = sku
        self.supplier = supplier
        self.my_price = my_price
        self.supplier_price = supplier_price
        self.quantity = quantity


class Ebay(Product):
    pass

class Amazon(Product):
    pass

