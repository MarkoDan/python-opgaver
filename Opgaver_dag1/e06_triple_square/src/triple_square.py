#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        triple_result = triple(i)
        square_result = square(i)
        if square_result > triple_result:
            break
        print(f"triple({i})=={triple_result} square({i})=={square_result}")


def triple(num):
    return num * 3

def square(num):
    return num ** 2

if __name__ == "__main__":
    main()
