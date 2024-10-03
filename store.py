from products import Product

class Store:
    #products = []

    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)
        print(f"Added product: {product.name}")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Processes a list of product and quantity pairs, purchases the items,
        and returns the total price of the order.
        :param shopping_list: List of tuples with Product and quantity.
        :return: Total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product.is_active() and product.get_quantity() >= quantity:
                total_price += product.buy(quantity)
            else:
                raise Exception(f"Cannot complete the purchase for {product.name}, insufficient quantity or inactive.")
        return total_price

def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print("-")
    print(store.order([(products[0], 1), (products[1], 2)]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()