class Book:
    def __init__(self, title, author, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.title = title
        self.author = author
        self.price = price


    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100")
        self.price -= self.price * percent / 100
