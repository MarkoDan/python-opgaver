#!/usr/bin/env python3

def file_extensions(filename):
    no_extension = []
    with_extension = {}
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '.' in line:
                
                extention = line.split('.')[-1]
                
                if extention not in with_extension:
                    with_extension[extention] = []
                with_extension[extention].append(line)
            else:
                no_extension.append(line)
    
    return (no_extension, with_extension)

def main():
    no_extension, with_extension = file_extensions("./filenames.txt")
    
    print(f"{len(no_extension)} files with no extension")
    for ext in sorted(with_extension.keys()):
        print(f"{ext} {len(with_extension[ext])}")

if __name__ == "__main__":
    main()
