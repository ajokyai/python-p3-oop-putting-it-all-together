class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price  # Will use the setter for validation

    # Price property with validation
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    # Example method: apply discount
    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100")
        self.price -= self.price * percent / 100
