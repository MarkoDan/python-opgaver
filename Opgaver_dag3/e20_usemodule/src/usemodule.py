#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    a, b = 3, 4
    print(f"The hypothenuse of a triangle with sides {a} and {b} is {triangle.hypothenuse(a, b)}")
    print(f"The area of a triangle with sides {a} and {b} is {triangle.area(a, b)}")

if __name__ == "__main__":
    main()
