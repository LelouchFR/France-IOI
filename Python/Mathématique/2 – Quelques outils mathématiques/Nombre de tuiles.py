from math import sqrt

F = float(input())
L = float(input())
H = float(input())
h = float(input())

print(L * 2 * sqrt((F/2)**2 + (H-h)**2))