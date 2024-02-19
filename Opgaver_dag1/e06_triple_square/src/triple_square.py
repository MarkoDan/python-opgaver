#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        triple(i)
        square(i)
        if square(i) > triple(i):
            break
        print(f"triple({i}) == {triple(i)} square({i}) == {square(i)}")


def triple(num):
    return num * 3

def square(num):
    return num ** 2

if __name__ == "__main__":
    main()
