from store import Store
from products import Product, NonStockedProduct, LimitedProduct
from promotion import Promotion, ThirdOneFree, SecondHalfPrice, PercentDiscount
import sys
import random
import string

def start(shop):
    while True:
        print("Welcome to the store!\n")
        print("1: List all products in store")
        print("2: Show total amount in store")
        print("3: Make an order")
        print("4: Quit\n")

        user_choice = input("Enter the number of your choice: ").strip()

        if user_choice == "1":
            list_all_products(shop)
        elif user_choice == "2":
            get_total_quantity(shop)
        elif user_choice == "3":
            make_an_order(shop)
        elif user_choice == "4":
            quit_program()
        else:
            print("Invalid choice, please provide a numeric value from the given menu options!")


def list_all_products(shop):
    active_products = shop.get_all_products()
    if not active_products:
        print("No current active products available")
    else:
        for product in active_products:
            if isinstance(product, NonStockedProduct):
                print(product)  # __str__ method will be used automatically
            elif isinstance(product, LimitedProduct):
                print(product.show())  # Call show for LimitedProduct
            else:
                print(product.show())  # Call show for other products


def get_total_quantity(shop):
    get_quantity = shop.get_total_quantity()
    print(f"Total of {get_quantity} items in store\n")


def make_an_order(shop):
    shopping_list = []  # To store the products and quantities to order
    while True:
        print("---------")
        list_all_products(shop)  # Show all active products
        print("---------")
        print("When you want to finish the order, enter an empty text for the product number.")

        # Get product number
        user_product_order = input("Which product # do you want? (Enter to finish): ").strip()

        if not user_product_order:  # If the input is empty, finish the order
            break

        try:
            product_index = int(user_product_order) - 1  # Convert input to index (assuming user enters 1-based index)
            product = shop.products[product_index]  # Get the product from the list

            # Get the amount the user wants to order
            product_amount = input("What amount do you want? ").strip()
            quantity = int(product_amount)

            # Add product and quantity to the shopping list
            shopping_list.append((product, quantity))

        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid product number and quantity.")

    # Process the order if the shopping list is not empty
    if shopping_list:
        try:
            total_price = shop.order(shopping_list)  # Call the order method
            print(f"Order successful! Total price: ${total_price}")
        except Exception as e:
            print(f"Order could not be completed: {e}")
    else:
        print("No items selected for the order.")


def generate_promotion_code(length=8):
    """Generate a random promotion code."""
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def quit_program():
    """Quit the program."""
    print("Thank you for visiting the store. Goodbye!")
    sys.exit()  # Exit the program


if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, max_purchase=500)
                    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Generate unique promotion codes
    promotion_catalog = {
        'Second Half Price': {
            'instance': second_half_price,
            'code': generate_promotion_code()
        },
        'Third One Free': {
            'instance': third_one_free,
            'code': generate_promotion_code()
        },
        '30% Off': {
            'instance': thirty_percent,
            'code': generate_promotion_code()
        }
    }

    # Display promotion catalog with codes
    for promo_name, promo_info in promotion_catalog.items():
        print(f"{promo_name}: {promo_info['code']} - {promo_info['instance']}")

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    # Create the Store instance
    best_buy = Store(product_list)

    # Start the interaction
    start(best_buy)
