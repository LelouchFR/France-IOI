tot = 0
while True:
   try:
      num = int(input())
   except EOFError:
      break
   if num < 0:
      print(tot)
   else:
      tot += num
