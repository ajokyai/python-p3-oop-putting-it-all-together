import pytest
from lib.shoe import Shoe

def test_shoe_attributes():
    shoe = Shoe("Nike", 42, 120)
    assert shoe.brand == "Nike"
    assert shoe.size == 42
    assert shoe.price == 120

def test_shoe_size_validation():
    with pytest.raises(ValueError):
        Shoe("Nike", 0, 120)

def test_shoe_price_validation():
    with pytest.raises(ValueError):
        Shoe("Nike", 42, -50)

def test_apply_discount():
    shoe = Shoe("Nike", 42, 200)
    shoe.apply_discount(25)
    assert shoe.price == 150

def test_invalid_discount():
    shoe = Shoe("Nike", 42, 200)
    with pytest.raises(ValueError):
        shoe.apply_discount(-5)
    with pytest.raises(ValueError):
        shoe.apply_discount(150)
