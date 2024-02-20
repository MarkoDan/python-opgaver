#!/usr/bin/env python3

def detect_ranges(L):
    sorted_list = sorted(L)
    new_list = []
    start = sorted_list[0]
    end = start  # Initialize 'end' to be the same as 'start'
    i = 0  # Initialize loop counter

    # Loop through the list, but ensure that you cover all elements
    while i < len(sorted_list) - 1:  # Loop up to the second-to-last element
        # Check if current and next elements are consecutive
        if sorted_list[i + 1] - sorted_list[i] == 1:
            end = sorted_list[i + 1]  # Update 'end' to this new value
        else:
            # If they are not consecutive, determine if 'start' and 'end' form a range or a single number
            if start == end:
                new_list.append(start)
            else:
                new_list.append((start, end + 1))  # Add a tuple for the range
            start = sorted_list[i + 1]  # Start a new range or number
            end = start  # Reset 'end' to the same as 'start'
        i += 1  # Move to the next element

    # After the loop, check if the last part of the list was a range or a single number
    # This also handles the case where the list has only one number
    if start == end:
        new_list.append(start)
    else:
        new_list.append((start, end + 1))  # Remember to add 1 to 'end' for Python's exclusive range

    return new_list

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
