from math import *

def distEuc(x1, y1, x2, y2):
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distEuc(x1, y1, x2, y2))
