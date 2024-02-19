#!/usr/bin/env python3

def main():
    for i in range(1, 11):  # Start range at 1 to match the table starting at 1
        for j in range(1, 11):
            print(f'{i * j:4}', end='')  # Print each product with 4 spaces for alignment
        print()  # Print a newline after each row to start the next row





if __name__ == "__main__":
    main()
