# Enter you module contents here

"""
This is the 'triangle' module.
This module provides functions to calculate the properties of a right-angled triangle.
It includes functions to calculate the hypothenuse and the area of the triangle.
"""

import math

__version__ = "1.0"
__author__ = "Marko Dankovich"

def hypothenuse(a, b):
    """
    Calculate the length of the hypothenuse of a right-angled triangle.

    Args:
        a (float): One of the perpendicular sides of the triangle.
        b (float): The other perpendicular side of the triangle.

    Returns:
        float: The length of the hypothenuse.
    """
    
    result = a ** 2 + b ** 2 
    return math.sqrt(result) 

def area(a, b):
    
    """
    Calculate the area of a right-angled triangle.

    Args:
        a (float): One of the perpendicular sides of the triangle.
        b (float): The other perpendicular side of the triangle.

    Returns:
        float: The area of the triangle.
    """
    
    
    result = (a * b) / 2
    return result