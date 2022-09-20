value = int(input())
times = 0

while True:
   try:
      uX = int(input())
   except EOFError:
      break
   times += 1
   if uX > value:
      print("c'est moins")
   elif uX < value:
      print("c'est plus")
   else:
      print("Nombre d'essais nécessaires :")
      print(times)
