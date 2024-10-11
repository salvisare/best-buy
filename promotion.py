from abc import abstractmethod, ABC

# promotion.py
class Promotion(ABC):
    def __init__(self, description):
        self.description = description

    @abstractmethod
    def apply(self, price, quantity=1):  # Default quantity to 1 for single items
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        return self.description

class SecondHalfPrice(Promotion):
    def apply(self, price, quantity):
        if quantity <= 1:
            return price * quantity  # No discount for 1 item
        # Only apply discount to the second half
        return price * (quantity / 2)  # Example of 50% off for each item

class ThirdOneFree(Promotion):
    def apply(self, price, quantity):
        if quantity < 3:
            return price * quantity  # No discount for less than 3 items
        free_items = quantity // 3  # For every three items, one is free
        total_price = price * (quantity - free_items)
        return total_price

class PercentDiscount(Promotion):
    def __init__(self, description, percent):
        super().__init__(description)  # Initialize the base class with the description
        self.percent = percent  # Store the percent discount

    def apply(self, price, quantity=1):
        discount_amount = price * (self.percent / 100)
        return (price - discount_amount) * quantity  # Apply discount per item