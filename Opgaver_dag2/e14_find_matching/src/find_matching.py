#!/usr/bin/env python3

def find_matching(L, pattern):
    new_list = []
    for i, word in enumerate(L):
        if pattern in word:
            new_list.append(i)
    
    return new_list

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
