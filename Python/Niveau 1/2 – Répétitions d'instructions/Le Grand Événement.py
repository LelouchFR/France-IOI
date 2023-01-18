from robot import *

for loop in range(9):
   droite()
for loop in range(9):
   haut()
gauche()
for loop in range(4):
   for loop in range(8):
      bas()
   gauche()
   for loop in range(8):
      haut()
   gauche()
for loop in range(9):
   bas()
