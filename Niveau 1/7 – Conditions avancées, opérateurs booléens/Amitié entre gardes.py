gAD = int(input())
gAF = int(input())
gBD = int(input())
gBF = int(input())

if (gAD <= gBD and gAF >= gBD) or (gBD <= gAD and gBF >= gAD):
   print("Amis")
else:
   print("Pas amis")
