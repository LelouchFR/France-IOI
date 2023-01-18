paires = int(input())
for i in range(paires):
   xmin1 = int(input())
   xmax1 = int(input())
   ymin1 = int(input())
   ymax1 = int(input())
   xmin2 = int(input())
   xmax2 = int(input())
   ymin2 = int(input())
   ymax2 = int(input())

   if (xmax2 <= xmin1 or xmax1 <= xmin2) or (ymax2 <= ymin1 or ymax1 <= ymin2):
      print("NON")
   else:
      print("OUI")
