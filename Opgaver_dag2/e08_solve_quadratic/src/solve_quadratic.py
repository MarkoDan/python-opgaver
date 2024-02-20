#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    d = math.sqrt(b**2 - 4 * a * c)
    positive_x = ((-b + d) / (2 * a))
    negative_x = ((-b - d) / (2 * a))
    return (positive_x,negative_x)


def main():
    print(solve_quadratic(1, 2, 1))

if __name__ == "__main__":
    main()
