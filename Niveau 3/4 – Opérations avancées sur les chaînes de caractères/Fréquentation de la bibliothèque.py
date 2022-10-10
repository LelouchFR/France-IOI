def lineSum():
   tot = 0
   while True:
      try:
         line = input()
      except EOFError:
         return tot
      tot += sum(map(int, line.split()))

print(lineSum())
