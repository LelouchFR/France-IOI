from math import *

population = int(input())
croissance = float(input())

population = floor(population * (1 + croissance / 100))
print(population)
