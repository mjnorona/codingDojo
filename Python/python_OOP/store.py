class Product(object):
    def __init__(self, name):
        self.name = name

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        for i in range(0, len(self.products)):
            if self.products[i].name == product.name:
                for j in range(i, len(self.products)-1):
                    self.products[j] = self.products[j + 1]
                break
        self.products = self.products[:-1]
        return self

    def inventory(self):
        for i in range(0, len(self.products)):
            print self.products[i].name
        print ""
        return self

prod1 = Product("phone")
prod2 = Product("tv")
prod3 = Product("blender")
prod4 = Product("laptop")

products = [prod1, prod2, prod3]
store = Store(products, "San Jose", "Marcus Norona")
store.inventory()
store.add_product(prod4)
store.inventory()
store.remove_product(prod2)
store.inventory()
