from robot import *

x = 1
for i in range(10):
   for j in range(x):
      if x > 10:
         break
      droite()
   ramasser()
   for j in range(x):
      if x > 10:
         break
      gauche()
   x += 1
   deposer()
