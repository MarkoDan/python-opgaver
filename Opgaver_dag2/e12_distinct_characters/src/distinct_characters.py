#!/usr/bin/env python3

def distinct_characters(L):
    # d = {}
    # for w in L:
    #     d[w] = len(set(w))
    # return d
    
    result = {}
    
    for string in L:
        unique_chars = set(string)
        result[string] = len(unique_chars)
    
    return result

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
