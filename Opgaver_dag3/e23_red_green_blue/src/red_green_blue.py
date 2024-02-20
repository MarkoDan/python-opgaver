#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    
    cleaned_lines = []
    seen_colors = set()
    with open(filename, 'r') as file:
        
        #skip the first line
        next(file)
        
        pattern = re.compile(r'(\d+)\s+(\d+)\s+(\d+)\s+([\w\s]+)')
        
        for line in file:
            matches = re.findall(pattern, line)
            
            for match in matches:
                red, green, blue, colorname = match
                colorname = colorname.strip()
                
                if colorname not in seen_colors:
                    cleaned_line = f'{red}\t{green}\t{blue}\t{colorname}'
                    cleaned_lines.append(cleaned_line)
                    seen_colors.add(colorname)
                    
    return(cleaned_lines)

def main():
    count = 0
    for line in red_green_blue():
        count += 1
        print(line)
    print(count)
if __name__ == "__main__":
    main()
