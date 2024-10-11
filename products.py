class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

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


    # Buy a given quantity
    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError("Cannot purchase more than available quantity.")  # Ensure this message matches the test

        total_price = quantity * self.price

        # Update the quantity after purchase
        self.quantity -= quantity  # Update quantity directly

        # Check if the product is now inactive
        if self.quantity == 0:
            self.active = False  # Product becomes inactive when quantity reaches 0

        return self.quantity  # Return the remaining quantity

    def show(self):
        status = "Active" if self.is_active() else "Inactive"
        return f"Product details: {self.name}, {self.price:.2f}, {self.quantity}, {status}"


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def buy(self, quantity):
        raise ValueError("Cannot purchase non-stocked products.")

    def __str__(self):
        return f"{self.name} (Non-stocked product): ${self.price:.2f} (License, no quantity available)"

class LimitedProduct(Product):
    def __init__(self, name, price, max_purchase):
        super().__init__(name, price, max_purchase)  # Initialize with max purchase as quantity
        self.max_purchase = max_purchase  # Set maximum purchase limit

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0")
        if quantity > self.max_purchase:
            raise ValueError(f"Cannot purchase more than {self.max_purchase} of this product.")

        # Call the parent method to update quantity
        return super().buy(quantity)


    def show(self):
        status = "Active" if self.is_active() else "Inactive"
        return f"{self.name} (Limited product): ${self.price:.2f}, Max purchase: {self.max_purchase}"
