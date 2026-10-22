apple = {"name": "apple", "price": 3.5}
bread = {"name": "bread", "price": 7.5}

class Cart:
    def __init__(self):
      self.__items = []
    
    def add(self, product):
      self.__items.append(product)

    def remove(self, product_name):
      for index, item in enumerate(self.__items):
        if item["name"] == product_name:
          del self.__items[index]
          break
    
    def total(self):
      return float(sum(item["price"] for item in self.__items))

    def items(self):
      items_list = []
      for i in self.__items:
        items_list.append(i["name"])
      return items_list
    
new_cart = Cart()
new_cart.add(apple)
new_cart.add(bread)

print(new_cart.items())
print(new_cart.total())

new_cart.remove("lemon")

print(new_cart.items())
print(new_cart.total())


"""
Rzeczy, których nie zrobiłem, a potencjalnie warto je dodać:
- raise ValueError dla różnych błędów i problemów
- zabezpieczenie struktury poszczególnych produktów w koszyku poprzez stworzenie klasy dla produktów, wykorzystanie tej klasy w metodach oraz wymuszanie zgodności z taką klasą
"""