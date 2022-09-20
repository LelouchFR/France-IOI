Maisons = int(input())
absMax = 1
absMin = 1000000
ordMax = 1
ordMin = 1000000

for i in range(Maisons):
   abss = int(input())
   ords = int(input())
   
   if abss > absMax:
      absMax = abss
   elif abss < absMin:
      absMin = abss
   if ords > ordMax:
      ordMax = ords
   elif ords < ordMin:
      ordMin = ords
  
larg = absMax - absMin
longue = ordMax - ordMin

if absMin > absMax:
   larg = absMin - absMax
   print((2 * larg - 1) + (2 * longue - 1))
else:
   print((2 * larg) + (2 * longue))
