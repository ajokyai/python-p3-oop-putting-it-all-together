class Shoe:
    def __init__(self, brand, size, price):
        if size <= 0:
            raise ValueError("Size must be positive")
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.brand = brand
        self.size = size
        self.price = price


    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100")
        self.price -= self.price * percent / 100
