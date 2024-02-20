#!/usr/bin/env python3

def reverse_dictionary(d):
    new_dict = {}
    
    for key, values in d.items():
        for value in values:
            if value not in new_dict:
                new_dict[value] = [key]
            
            else:
                new_dict[value].append(key)
    
    return new_dict
    

def main():
    
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    new_dict = reverse_dictionary(d)
    
    for key, value in new_dict.items():
        print(f"Key: {key}, Value: {value}")

if __name__ == "__main__":
    main()
