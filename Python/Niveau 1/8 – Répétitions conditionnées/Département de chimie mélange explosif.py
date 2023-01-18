tests = int(input())
tmin = int(input())
tmax = int(input())

while True:
   try:
      testss = int(input())
   except EOFError:
      break
   if testss >= tmin and testss <= tmax:
      print("Rien à signaler")
   else:
      print("Alerte !!")
      break
