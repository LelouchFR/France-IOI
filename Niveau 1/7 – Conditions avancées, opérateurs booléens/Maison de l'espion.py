xmin = int(input())
xmax = int(input())
ymin = int(input())
ymax = int(input())
maisons = int(input())
tot = 0

for i in range(maisons):
   xm = int(input())
   ym = int(input())
   if xmin <= xm  <= xmax and ymin <= ym <= ymax: 
         tot += 1

print(tot)
