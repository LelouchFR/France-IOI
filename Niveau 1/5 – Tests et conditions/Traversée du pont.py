de1 = int(input())
de2 = int(input())

if de1 + de2 >= 10:
   print("Taxe spéciale !")
   print(36)
else:
   print("Taxe régulière")
   print((de1 + de2) * 2)
