longueurMax = int(input())

for x in range(1, longueurMax):
  for y in range(x + 1, longueurMax):
    z = (x ** 2 + y ** 2) ** 0.5
    if z.is_integer() and z <= longueurMax:
      print(x, y, int(z))