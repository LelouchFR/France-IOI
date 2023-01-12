from math import pi

inner, outer, population = int(input()), int(input()), int(input())
area = pi * (outer ** 2 - inner ** 2)
density = population / area
print(round(density, 2))