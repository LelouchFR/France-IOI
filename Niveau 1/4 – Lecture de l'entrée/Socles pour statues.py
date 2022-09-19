debut = int(input())
fin = int(input())
tot = 0
dub = debut
for i in range(dub):
   if debut >= fin:
      tot += debut * debut
      debut -= 1
print(tot)
