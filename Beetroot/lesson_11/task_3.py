"""
Product Store

Write a class Product that has three attributes:

type name price Then create a class ProductStore, which will have some Products and will operate with all products in
the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error
information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement
additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(
        30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by
        input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name,amount) - removes a particular amount of products from the store if available, in other case
        raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store. ```

class Product:
    pass

class ProductStore:
pass

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen, 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell(‘Ramen’, 10)
assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
"""


class Product:
    def __init__(self, product_type='', name='', price=0):
        self.product_type = product_type
        self.name = name
        self.price = price


class ProductStore:

    def __init__(self, premium=30):
        self.premium = premium
        self.products = {}
        self.income = 0
        self.price = 0

    def shop_price(self, price):
        return price * (1 + self.premium / 100)

    def add(self, product: Product, amount):
        if product.name not in self.products:
            self.products.update({product.name: {'amount': amount,
                                                 'price': self.shop_price(product.price),
                                                 'type': product.product_type}})
        else:
            self.products[product.name]['amount'] += amount
            self.products[product.name]['price'] = max(self.shop_price(product.price),
                                                       self.products[product.name]['price'])
            self.products[product.name]['type'] = product.product_type

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier in self.products:
            self.products.update({identifier: {'price': self.products[identifier]['price'] * (1 - percent/100)}})
        for item, value in self.products.items():
            if value.get(identifier_type) == identifier:
                self.products[item]['price'] = round(self.products[item]['price'] * (1 - percent / 100), 2)

    def sell_product(self, product_name, amount):
        if product_name in self.products:
            self.products[product_name]['amount'] -= amount
            self.income += self.products[product_name].get('price') * amount
        else:
            raise ValueError('Wrong amount.')

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products.keys()

    def get_product_info(self, product_name):
        try:
            return product_name, self.products[product_name].get('amount')
        except Exception:
            raise ValueError("There is no such product in a store.")


if __name__ == '__main__':
    t_shirt = Product('Sport', 'Football T-Shirt', 100)

    t_shirt_2 = Product('Sport', 'Football T-Shirt', 200)
    pasta = Product('Food', 'Pasta', 5)

    ramen = Product('Food', 'Ramen', 2)
    pr_store = ProductStore()
    pr_store.add(t_shirt, 100)
    print(pr_store.products)
    pr_store.add(t_shirt_2, 200)
    pr_store.add(ramen, 30)
    pr_store.add(pasta, 50)
    print(pr_store.products)
    pr_store.set_discount('Food', 10, 'type')
    pr_store.sell_product('Pasta', 5)
    print(pr_store.products)
    print(pr_store.get_income())

