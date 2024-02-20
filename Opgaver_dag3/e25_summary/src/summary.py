#!/usr/bin/env python3

import sys
import math

def summary(filename):

    numbers = []
    
    with open(filename, 'r') as file:
        for line in file:
            try:
                num = float(line.strip())
                numbers.append(num)

            except ValueError:                 
                print("invalid line")
    
    sum_of_numbers = sum(numbers)
    count = len(numbers)
    if count > 0:
        avarage = sum_of_numbers / count
    
        sum_squared_diff = sum((x - avarage) ** 2 for x in numbers)
        
        deviation = math.sqrt(sum_squared_diff / (count - 1)) 
    
    else:
        avarage = 0
        deviation = 0
    
    return sum_of_numbers, avarage, deviation

    
    

def main():
    for filename in sys.argv[1:]:
        
        sum_of_numbers, average, stddev = summary(filename)
        
        print(f"File: {filename} Sum: {sum_of_numbers:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")

if __name__ == "__main__":
    main()
