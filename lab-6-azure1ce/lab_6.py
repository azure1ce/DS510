# Lab 6
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
class Vehicle:
    """Attributes and Methods of class Vehicle"""

    def __init__(self, vehicle_id: str, make: str, model: str, year: int):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Vehicle(vehicle_id='{self.vehicle_id}', make='{self.make}', model='{self.model}', year={self.year})"

    def __repr__(self):
        return f"Vehicle(vehicle_id='{self.vehicle_id}', make='{self.make}', model='{self.model}', year={self.year})"



# ----------------- Question 2 -----------------
class LibraryMember:
    """Attributes and Methods of class Library Member"""

    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"LibraryMember(member_id='{self.member_id}', name='{self.name}', total_borrowed={self.count_books()})"

    def __repr__(self):
        return f"LibraryMember(member_id='{self.member_id}', name='{self.name}', total_borrowed={self.count_books()})"
    
    def add_book(self, book_title: str):
        self.borrowed_books.append(book_title)

    def remove_book(self, book_title: str):
        self.borrowed_books.remove(book_title)

    def count_books(self):
        return len(self.borrowed_books)



# invoke the function with relevant args of your choice
# WRITE CODE HERE


# ----------------- Question 3 -----------------
class Product:
    """Attributes and Methods of class Product"""
    def __init__(
        self, product_code: str, name: str, price: float, quantity_available: int
    ):
        self.product_code = product_code
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def __str__(self):
        return f"Product(product_code='{self.product_code}', name='{self.name}', price={self.price}, quantity_available={self.quantity_available})"

    def __repr__(self):
        return f"Product(product_code='{self.product_code}', name='{self.name}', price={self.price}, quantity_available={self.quantity_available})"

    def update_price(self, new_price: float):
        self.price = new_price

    def add_stock(self, quantity: int):
        self.quantity_available += quantity

    def sell_product(self, quantity: int):
        if self.quantity_available < quantity:
            self.quantity_available
        else:
            self.quantity_available -= quantity


# invoke the function with relevant args of your choice
# WRITE CODE HERE
