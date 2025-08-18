class Cart:
    def __init__(self):
        self.cart_list = []

    def add_to_cart(self, product, price):
        item = {"product": product, "price": price}
        self.cart_list.append(item)

    def remove_from_cart(self, product,):
       for item in self.cart_list:
            if  item["product"] == product:
               self.cart_list.remove(item)
               break

    def total_cart(self):
        total = 0.0
        for item_price in self.cart_list:
           total += item_price["price"]
        return float(total)

    def items_cart_list(self):
        product_list = []
        for item in self.cart_list:
            product_list.append(item["product"])
        return product_list



