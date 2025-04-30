import math

def circumference(r):
    return 2 * 22/7 * r


radii = int(input('Enter the radius of a circle: '))
print(f'Circumference is {math.floor(circumference(radii))}')
