from math import *

tActu = float(input())
tFut = float(input())
legume = float(input())

price = round((legume / (1 + tActu / 100) * (1 + tFut / 100)) * 100) / 100
print(price)
