import pytest
from lib.book import Book

def test_book_attributes():
    book = Book("Python 101", "Guido van Rossum", 50)
    assert book.title == "Python 101"
    assert book.author == "Guido van Rossum"
    assert book.price == 50

def test_book_price_validation():
    with pytest.raises(ValueError):
        Book("Python 101", "Guido van Rossum", -10)

def test_apply_discount():
    book = Book("Python 101", "Guido van Rossum", 100)
    book.apply_discount(20)
    assert book.price == 80

def test_invalid_discount():
    book = Book("Python 101", "Guido van Rossum", 100)
    with pytest.raises(ValueError):
        book.apply_discount(-10)
    with pytest.raises(ValueError):
        book.apply_discount(150)
