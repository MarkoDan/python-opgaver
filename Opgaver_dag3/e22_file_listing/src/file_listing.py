#!/usr/bin/env python3

import re

#change the path to ./listning.txt incase you want to run the code
def file_listing(filename="src/listing.txt"):
    new_list = []
    
    pattern = r'(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+(.+)$'
    
    with open(filename, 'r') as file:
        for line in file:
            
            match = re.search(pattern, line)

            if match:
                size = int(match.group(1))
                month = match.group(2)
                day = int(match.group(3))
                hour = int(match.group(4))
                minute = int(match.group(5))
                filename = match.group(6)
                
                new_list.append((size, month, day, hour, minute, filename))
    
    return new_list
        

def main():
    
    result = file_listing()
    print(result)

if __name__ == "__main__":
    main()
