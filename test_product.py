import pytest
from products import Product  # Assuming Product class is in product.py


def test_create_normal_product():
    # Test creating a product with valid details
    product = Product("Laptop", 1000, 10)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 10
    assert product.active == True


def test_create_product_with_invalid_details():
    # Test creating a product with an empty name should raise a ValueError
    with pytest.raises(ValueError, match="Product name cannot be empty."):
        Product("", 1450, 100)

    # Test creating a product with a negative price should raise a ValueError
    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", -10, 100)

    # Test creating a product with a negative quantity should raise a ValueError
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("iPhone 13", 999, -5)


def test_product_becomes_inactive_when_quantity_zero():
    # Test that product becomes inactive when quantity reaches 0
    product = Product("Phone", 500, 1)
    product.buy(1)
    assert product.quantity == 0
    assert product.active == False


def test_product_buy_modifies_quantity():
    # Test that product purchase modifies the quantity correctly
    product = Product("Headphones", 150, 5)
    remaining_quantity = product.buy(2)
    assert remaining_quantity == 3  # After buying 2, 3 should be left
    assert product.quantity == 3


def test_buy_larger_quantity_than_exists_raises_exception():
    # Test that buying a larger quantity than exists raises an exception
    product = Product("Monitor", 300, 3)
    with pytest.raises(ValueError, match="Cannot purchase more than available quantity."):
        product.buy(5)

