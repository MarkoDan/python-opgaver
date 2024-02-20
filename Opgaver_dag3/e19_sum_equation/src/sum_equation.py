#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"
    else:
        equation = " + ".join(str(num) for num in L)
        sum_of_numbers = sum(L)
        return f"{equation} = {sum_of_numbers}"

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
