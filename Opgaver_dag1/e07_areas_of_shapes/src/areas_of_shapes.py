# #!/usr/bin/env python3

# import math


# def main():
#     # enter you solution here
#     shapes = ['triangle', 'rectangle', 'circle']
#     while True:
#         shape = input('Choose a shape (triangle, rectangle, circle): ')
#         if shape == "":
#            break
#         elif shape not in shapes:
#             print('Unknown shape!')
#             # continue
#         else:
#             base = int(input(f'Give base of the {shape}: '))
#             height = int(input(f'Give height of the {shape}: '))
#             print(f"The area is {float(calculate_area(shape, base, height))}")


# def calculate_area(shape, base, heigth):
#     if shape == "triangle":
#         return 0.5 * base * heigth
#     elif shape == "rectangle":
#         return base * heigth
#     elif shape == "circle":
#         return math.pi * base ** 2
#     else:
#         return None


            

# if __name__ == "__main__":
#     main()


import math

def main():
    shapes = ['triangle', 'rectangle', 'circle']
    while True:
        shape = input('Choose a shape (triangle, rectangle, circle): ')
        if shape == "":
            return  # Exits if the user inputs an empty string
        elif shape not in shapes:
            print('Unknown shape!')
            continue
        else:
            if shape == 'circle':
                radius = float(input('Give radius of the circle: '))
                area = math.pi * radius ** 2
                print(f'The area is {area}')
            else:
                base = float(input(f'Give base of the {shape}: '))
                if shape == 'triangle':
                    height = float(input(f'Give height of the {shape}: '))
                    area = 0.5 * base * height
                elif shape == 'rectangle':
                    height = float(input(f'Give height of the {shape}: '))
                    area = base * height
                print(f'The area is {area}')

if __name__ == "__main__":
    main()
