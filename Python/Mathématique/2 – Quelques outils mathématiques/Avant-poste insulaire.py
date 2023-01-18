from math import *

d = int(input())

perimeter, area = pi * d, (pi * (d/2)**2)
perimeter, area = round(perimeter), round(area)

print(perimeter)
print(area)