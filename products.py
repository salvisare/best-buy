# products.py
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
        self.promotion = None  # Initialize the promotion attribute

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

    def get_promotion(self):
        return self.promotion  # Return the actual promotion instance

    def set_promotion(self, promotion):
        self.promotion = promotion  # Set the promotion correctly

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
            raise ValueError("Cannot purchase more than available quantity.")

        # Calculate the total price considering the promotion
        if self.promotion:
            total_price = self.promotion.apply(self.price, quantity)
        else:
            total_price = self.price * quantity

        # Update the quantity after purchase
        self.quantity -= quantity

        # Check if the product is now inactive
        if self.quantity == 0:
            self.active = False

        return total_price  # Return the total price of the order

    def show(self):
        status = "Active" if self.is_active() else "Inactive"
        promotion_str = f" ({self.get_promotion().description})" if self.get_promotion() else " (No promotion)"
        return f"Product details: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Status: {status}{promotion_str}"


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
