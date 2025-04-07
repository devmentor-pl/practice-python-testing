class Cart:

    def __init__(self):
        self.__products = {}

    def add(self, key, product):
        self.__products[key] = [product]

    def remove(self, key):
        if not self.__products:
            raise KeyError('There is not such product in cart.')
        self.__products.pop(key)

    def total(self):
        total = float(sum(product[0]['price'] for product in self.__products.values()))
        return total

    def items(self):
        return list(self.__products)

if __name__ == '__main__':
    cart = Cart()
    cart.add('apple', {'name': 'apple', 'price': 3.5})
    cart.add('banana', {'name': 'banana', 'price': 4.0})
    print(cart.total())
    print(cart.items())

