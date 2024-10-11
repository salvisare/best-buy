from products import Product

class Store:

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


    def display_products(self):
        print("Available Products:")
        for product in self.products:
            print(product.show())  # Call the show method to display product details


