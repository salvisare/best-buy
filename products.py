class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")

        if float(price) < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    # Get quantity
    def get_quantity(self):
        return float(self.quantity)

    # Is active
    def is_active(self):
        return self.active

    # Set quantity with if active
    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        if self.quantity == 0:
            self.active = False

    # Activate the product
    def activate(self):
        self.active = True

    # Deactivate the product
    def deactivate(self):
            self.active = False

    # Buys a given quantity of the product
    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available")

        total_price = quantity * self.price

        # Update the quantity after purchase
        self.set_quantity(self.quantity - quantity)

        return total_price

    # Buy a given quantity
    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available")

        total_price = quantity * self.price

        # Update the quantity after purchase
        self.set_quantity(self.quantity - quantity)

        return total_price

    def show(self):
        status = "Active" if self.is_active() else "Inactive"
        print(f"Product details: {self.name}, {self.price}, {self.quantity}, {status}")


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()