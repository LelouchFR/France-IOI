positiondedépart = int(input())
largeuremplacement = int(input())
nbvendeur = int(input())
  
print(positiondedépart)
  
for i in range (nbvendeur):
   positiondedépart += largeuremplacement
   print(positiondedépart)
