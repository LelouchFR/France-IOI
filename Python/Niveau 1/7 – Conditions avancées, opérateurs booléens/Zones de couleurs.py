j = int(input())

for i in range(j):
   x = int(input())
   y = int(input())
   
   if not (90 >= x >= 0 and 70 >= y >= 0):
      print("En dehors de la feuille")
   elif (45 >= x >= 15 and 70 >= y >= 60) or (85 >= x >= 60 and 70 >= y >= 60):
      print("Dans une zone rouge")
   elif (85 >= x >= 10 and 55 >= y >= 10) and not (50 >= x >= 25 and 45 >= y >= 20):
      print("Dans une zone bleue")
   else:
      print("Dans une zone jaune")
