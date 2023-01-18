personnes = int(input())

for i in range(personnes):
   size = int(input())
   age = int(input())
   weight = int(input())
   horse = int(input())
   hairB = int(input())
   good = 0
   
   if 182 >= size >= 178:
      good += 1
   if age >= 34:
      good += 1
   if weight < 70:
      good += 1
   if horse == 0:
      good += 1
   if hairB == 1:
      good += 1

   if good == 5:
      print("Très probable")
   elif good >= 3:
      print("Probable")
   elif good == 0:
      print("Impossible")
   else:
      print("Peu probable")
