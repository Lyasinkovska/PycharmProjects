class Product:
    def __init__(self, product_type='', name='', price=0):
        self.product_type = product_type
        self.name = name
        self.price = price


class StoreProduct:

    def __init__(self, prod: Product):
        self.prod = prod
        self.price = prod.price
        # self.name = prod.name
        self.premium = 30
        self.amount = 0

    def set_shop_price(self, premium: int):
        return round(self.price * (1 + premium / 100), 2)

    def current_shop_price(self, old_price, premium=30):
        return max(old_price, self.set_shop_price(premium))

    def __repr__(self):
        return f"{self.prod.product_type}, {self.prod.name}, {self.prod.price}"

    def __str__(self):
        return f"{self.prod.product_type}, {self.prod.name}, {self.prod.price}"


class ProductStore:

    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product: Product, amount: int):
        shop_product = StoreProduct(product)
        if shop_product not in self.products.keys():

            self.products.update({shop_product: amount})
            shop_product.__str__()
        else:
            self.products[product] += amount
            # self.products[product.price] = product.price




    # def set_discount(self, identifier: str, percent: int, identifier_type='name'):
    #     self.products[identifier][0].price = self.products.get(identifier)[0].set_shop_price(-percent)


if __name__ == '__main__':
    store = ProductStore()
    p = Product('Food', 'Ramen', 2)
    p3 = Product('Food', 'Ramen', 8)
    p2 = Product('Food', 'Pasta', 5)
    print(id(p), id(p2), id(p3))
    store.add(p, 100)
    store.add(p, 20)
    print(store.products)


