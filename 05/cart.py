class Cart:
    def __init__(self):
        self._products = []
    
    def add(self, product):
        self._products.append(product)

    def remove(self, product_name):
        for product in self._products:
            if product["name"] == product_name:
                self._products.remove(product)
                break
    
    def total(self):
        return float(sum(p["price"] for p in self._products))

    def items(self):
        return self._products.copy()
    