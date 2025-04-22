# Avery bowman, class project Geometry Calculator

import math
from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    # Abstract base class for all shapes
    
    @abstractmethod
    def area(self):
        # Calculate the area of the shape
        pass
    
    @abstractmethod
    def perimeter(self):
        # Calculate the perimeter of the shape
        pass
    
    @abstractmethod
    def display_info(self):
        # Display all information about the shape
        pass
    
    @staticmethod
    @abstractmethod
    def explain_formulas():
        # Explain the formulas used for this shape
        pass
    
    def has_larger_area(self, other):
        # Compare if this shape has a larger area than another shape
        return self.area() > other.area()
    
    def has_longer_perimeter(self, other):
        # Compare if this shape has a longer perimeter than another shape
        return self.perimeter() > other.perimeter()


class Circle(Shape):
    # Circle shape class
    
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        # Calculate the area of the circle
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        # Calculate the circumference of the circle
        return 2 * math.pi * self.radius
    
    def display_info(self):
        # Display all information about the circle
        return f"""
Circle Information:
Radius: {self.radius}
Area: {self.area():.2f}
Circumference: {self.perimeter():.2f}
"""
    
    @staticmethod
    def explain_formulas():
        # Explain the formulas used for circle calculations
        return


class Rectangle(Shape):
    # Rectangle shape class
    
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        self.length = length
        self.width = width
    
    def area(self):
        # Calculate the area of the rectangle
        return self.length * self.width
    
    def perimeter(self):
        # Calculate the perimeter of the rectangle
        return 2 * (self.length + self.width)
    
    def display_info(self):
        # Display all information about the rectangle
        return f"""
Rectangle Information:
Length: {self.length}
Width: {self.width}
Area: {self.area():.2f}
Perimeter: {self.perimeter():.2f}
"""
    
    @staticmethod
    def explain_formulas():
        # Explain the formulas used for rectangle calculations
        return
    
class Square(Rectangle):
    # Square shape class - a special case of rectangle
    
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive")
        super().__init__(side, side)
        self.side = side
    
    def display_info(self):
        # Display all information about the square
        return f"""
Square Information:
Side: {self.side}
Area: {self.area():.2f}
Perimeter: {self.perimeter():.2f}
"""
    
    @staticmethod
    def explain_formulas():
        # Explain the formulas used for square calculations
        return


class Triangle(Shape):
    # Triangle shape class
    
    def __init__(self, side1, side2, side3):
        # Check if the triangle is valid using the triangle inequality theorem
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All sides must be positive")
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            raise ValueError("Invalid triangle: the sum of the lengths of any two sides must be greater than the length of the remaining side")
        
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Calculate the area of the triangle using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        # Calculate the perimeter of the triangle
        return self.side1 + self.side2 + self.side3
    
    def display_info(self):
        # Display all information about the triangle
        return f"""
Triangle Information:
Side 1: {self.side1}
Side 2: {self.side2}
Side 3: {self.side3}
Area: {self.area():.2f}
Perimeter: {self.perimeter():.2f}
"""
    
    @staticmethod
    def explain_formulas():
        # Explain the formulas used for triangle calculations
        return """
Triangle Formulas:
Area = √[s(s-a)(s-b)(s-c)] (Heron's formula)
where s = (a+b+c)/2 (semi-perimeter)
Perimeter = a + b + c
Where a, b, and c are the three sides of the triangle.
"""


class GeometryCalculator:
    # Main class to manage the geometry calculator functionality
    
    def __init__(self):
        self.shapes = []
        self.current_shape_index = -1
    
    def add_circle(self, radius):
        # Add a circle to the calculator
        try:
            circle = Circle(radius)
            self.shapes.append(circle)
            self.current_shape_index = len(self.shapes) - 1
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def add_rectangle(self, length, width):
        # Add a rectangle to the calculator
        try:
            rectangle = Rectangle(length, width)
            self.shapes.append(rectangle)
            self.current_shape_index = len(self.shapes) - 1
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def add_square(self, side):
        # Add a square to the calculator
        try:
            square = Square(side)
            self.shapes.append(square)
            self.current_shape_index = len(self.shapes) - 1
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def add_triangle(self, side1, side2, side3):
        # Add a triangle to the calculator
        try:
            triangle = Triangle(side1, side2, side3)
            self.shapes.append(triangle)
            self.current_shape_index = len(self.shapes) - 1
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def get_current_shape(self):
        # Get the currently selected shape
        if not self.shapes or self.current_shape_index < 0:
            return None
        return self.shapes[self.current_shape_index]
    
    def select_shape(self, index):
        # Select a shape by index
        if 0 <= index < len(self.shapes):
            self.current_shape_index = index
            return True
        return False
    
    def list_shapes(self):
        # List all shapes in the calculator
        if not self.shapes:
            return "No shapes created yet."
        
        result = "Available Shapes:\n"
        for i, shape in enumerate(self.shapes):
            shape_type = type(shape).__name__
            if i == self.current_shape_index:
                result += f"{i}: {shape_type} (SELECTED)\n"
            else:
                result += f"{i}: {shape_type}\n"
        return result
    
    def sort_shapes_by_area(self):
        # Sort shapes by area
        if not self.shapes:
            return "No shapes to sort."
        
        self.shapes.sort(key=lambda shape: shape.area())
        return "Shapes sorted by area (smallest to largest)."
    
    def sort_shapes_by_perimeter(self):
        # Sort shapes by perimeter
        if not self.shapes:
            return "No shapes to sort."
        
        self.shapes.sort(key=lambda shape: shape.perimeter())
        return "Shapes sorted by perimeter (smallest to largest)."
    
    def compare_shapes(self, index1, index2):
        # Compare two shapes
        if not (0 <= index1 < len(self.shapes) and 0 <= index2 < len(self.shapes)):
            return "Invalid shape indices."
        
        shape1 = self.shapes[index1]
        shape2 = self.shapes[index2]
        shape1_type = type(shape1).__name__
        shape2_type = type(shape2).__name__
        
        area_comparison = "larger" if shape1.has_larger_area(shape2) else "smaller"
        perimeter_comparison = "longer" if shape1.has_longer_perimeter(shape2) else "shorter"
        
        result = f"Comparison between {shape1_type} (index {index1}) and {shape2_type} (index {index2}):\n"
        result += f"- {shape1_type} has a {area_comparison} area than {shape2_type}\n"
        result += f"- {shape1_type} has a {perimeter_comparison} perimeter than {shape2_type}\n"
        result += f"- {shape1_type} area: {shape1.area():.2f}, {shape2_type} area: {shape2.area():.2f}\n"
        result += f"- {shape1_type} perimeter: {shape1.perimeter():.2f}, {shape2_type} perimeter: {shape2.perimeter():.2f}"
        
        return result


def main():
    # Main function to run the Geometry Calculator
    calculator = GeometryCalculator()
    
    while True:
        print("\n===== Geometry Calculator =====")
        current_shape = calculator.get_current_shape()
        
        if current_shape:
            print(f"Current Shape: {type(current_shape).__name__}")
        else:
            print("No shape selected")
        
        print("\nMenu Options:")
        print("1. Create a new shape")
        print("2. List all shapes")
        print("3. Select a shape")
        print("4. Display current shape info")
        print("5. Show formulas for current shape")
        print("6. Compare shapes")
        print("7. Sort shapes")
        print("8. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-8): "))
            
            if choice == 1:
                create_shape(calculator)
            elif choice == 2:
                print(calculator.list_shapes())
            elif choice == 3:
                select_shape(calculator)
            elif choice == 4:
                display_shape_info(calculator)
            elif choice == 5:
                show_formulas(calculator)
            elif choice == 6:
                compare_shapes(calculator)
            elif choice == 7:
                sort_shapes(calculator)
            elif choice == 8:
                print("Thank you for using the Geometry Calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")


def create_shape(calculator):
    # Helper function to create a new shape
    print("\nCreate a new shape:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")
    
    try:
        shape_choice = int(input("Enter your choice (1-4): "))
        
        if shape_choice == 1:
            radius = float(input("Enter the radius: "))
            if calculator.add_circle(radius):
                print("Circle created successfully!")
        
        elif shape_choice == 2:
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            if calculator.add_rectangle(length, width):
                print("Rectangle created successfully!")
        
        elif shape_choice == 3:
            side = float(input("Enter the side length: "))
            if calculator.add_square(side):
                print("Square created successfully!")
        
        elif shape_choice == 4:
            side1 = float(input("Enter the first side: "))
            side2 = float(input("Enter the second side: "))
            side3 = float(input("Enter the third side: "))
            if calculator.add_triangle(side1, side2, side3):
                print("Triangle created successfully!")
        
        else:
            print("Invalid choice.")
    
    except ValueError:
        print("Please enter valid numerical values.")


def select_shape(calculator):
    # Helper function to select a shape
    print(calculator.list_shapes())
    
    if not calculator.shapes:
        return
    
    try:
        index = int(input("Enter the index of the shape to select: "))
        if calculator.select_shape(index):
            print(f"Shape at index {index} selected.")
        else:
            print("Invalid index.")
    
    except ValueError:
        print("Please enter a valid number.")


def display_shape_info(calculator):
    # Helper function to display information about the current shape
    current_shape = calculator.get_current_shape()
    
    if current_shape:
        print(current_shape.display_info())
    else:
        print("No shape selected.")


def show_formulas(calculator):
    # Helper function to show formulas for the current shape
    current_shape = calculator.get_current_shape()
    
    if current_shape:
        print(type(current_shape).explain_formulas())
    else:
        print("No shape selected.")


def compare_shapes(calculator):
    # Helper function to compare two shapes
    if len(calculator.shapes) < 2:
        print("You need at least two shapes to compare.")
        return
    
    print(calculator.list_shapes())
    
    try:
        index1 = int(input("Enter the index of the first shape: "))
        index2 = int(input("Enter the index of the second shape: "))
        
        result = calculator.compare_shapes(index1, index2)
        print(result)
    
    except ValueError:
        print("Please enter valid numerical values.")


def sort_shapes(calculator):
    # Helper function to sort shapes
    if not calculator.shapes:
        print("No shapes to sort.")
        return
    
    print("\nSort shapes by:")
    print("1. Area")
    print("2. Perimeter")
    
    try:
        sort_choice = int(input("Enter your choice (1-2): "))
        
        if sort_choice == 1:
            print(calculator.sort_shapes_by_area())
        elif sort_choice == 2:
            print(calculator.sort_shapes_by_perimeter())
        else:
            print("Invalid choice.")
    
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()