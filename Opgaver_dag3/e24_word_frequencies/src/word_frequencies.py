#!/usr/bin/env python3

def word_frequencies(filename='./alice.txt'):

    frequencies = {}

    with open(filename, 'r') as file:

        for line in file:

            words = line.split()

            for word in words:

                cleaned_word = word.strip("""!"#$%&'()*,-./:;?@[]_""")

                frequencies[cleaned_word] = frequencies.get(cleaned_word, 0) + 1


    return frequencies

def main():
    
    frequencies = word_frequencies()
    
    for word, count in frequencies.items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
