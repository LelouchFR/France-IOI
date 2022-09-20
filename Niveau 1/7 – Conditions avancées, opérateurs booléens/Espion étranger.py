dD = int(input())
dF = int(input())
enter = int(input())
tot = 0

for i in range(enter):
   uX = int(input())
   if (dD <= uX) and (dF >= uX):
      tot += 1
print(tot)
