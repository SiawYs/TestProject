import math
import sys

def calc_circle_area(radius):
    pi = 3.14159

    if radius < 0:
        return "Error: Negative radius not allowed"
    area = pi * (radius**2)

    return area

class Shape:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Shape name is: {self.name}")

def complicated_function(a, b, c):
    if a + b > c:
        print("a + b is greater than c")
        return a * b
    elif a + b < c:
        print("a + b is less than c")
        return a - b
    else:
        print("a + b is equal to c")
        return 0

def main_function():
    shape = Shape("Circle")
    shape.display_name()
    result = calc_circle_area(5)
    print("Area of circle:", result)

    complicated_function(10, 5, 20)

main_function()
