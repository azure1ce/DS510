# Lab 7
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------


class Vehicle:
    """Attributes and Methods of class Vehicle"""

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
       return(f"{self.year} {self.make} {self.model}")

class Bike(Vehicle):
    """Attributes and Methods of class Bike"""

    def __init__(self, make: str, model: str, year: int, bike_type: str):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def __str__(self):
       return(f"{super().__str__()}, {self.bike_type} type")

class Car(Vehicle):
    """Attributes and Methods of class Car"""
    
    def __init__(self, make: str, model: str, year: int, is_electric: bool = False):
        super().__init__(make, model, year)
        self.is_electric = is_electric

    def __str__(self):
        if self.is_electric:
            self.type = "Electric"
        else:
            self.type = "Non-Electric"
        return(f"{super().__str__()}, {self.type}")
        
    def driving_range(self, energy: int) -> int:
        miles_per_battery_percent = 4
        miles_per_gallon = 30
        if self.is_electric:
            return energy * miles_per_battery_percent
        else:
            return energy * miles_per_gallon


# ----------------- Question 2 -----------------


class ComplexNumber:
    """Attributes and Methods of class Complex Number"""

    def __init__(self, real: int, imaginary: int):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        output = ComplexNumber(0,0)
        output.real = self.real + other.real
        output.imaginary = self.imaginary + other.imaginary
        return output
        
    def __mul__(self, other):
        output = ComplexNumber(0,0)
        output.real = self.real*other.real - self.imaginary*other.imaginary  
        output.imaginary = self.real*other.imaginary+self.imaginary*other.real
        return output
        
    def __str__(self):
        return(f"ComplexNumber with real part {self.real} and imaginary part {self.imaginary}")


# invoke the function with relevant args of your choice
# WRITE CODE HERE


# ----------------- Question 3 -----------------
class Shape:
    """Attributes and Methods of class Shape"""
    
    def area(self) -> int:
        raise NotImplementedError("This method should be overridden by subclasses")

    def dimensions(self) -> dict:
        raise NotImplementedError("This method should be overridden by subclasses")
        
class Rectangle(Shape):
    """Attributes and Methods of class Rectangle"""

    def __init__(self, length: int = None, width: int = None, side: int = None):
            self.side = side
            self.length = length
            self.width = width
        
        
    def area(self):
        if self.side != None:
            return self.side **2
        elif (self.length != None) & (self.width != None):
            return self.length * self.width
            
    def dimensions(self):
        output = dict()
        if self.side != None:
            output["side"] = self.side
            return output
        elif (self.length != None) & (self.width != None):
            output["length"] = self.length
            output["width"] = self.width
            return output

class Circle(Shape):
    """Attributes and Methods of class Circle"""
    
    def __init__(self, radius: int):
        self.radius = radius
        
    def area(self):
        pi = 3.1415926
        if (self.radius != None):
            return round(pi*self.radius**2,2)
            
    def dimensions(self):
        output = dict()
        output["radius"] = self.radius
        return output

# invoke the function with relevant args of your choice
# WRITE CODE HERE
