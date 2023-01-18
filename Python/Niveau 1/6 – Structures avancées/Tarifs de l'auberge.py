age = int(input())
bg = int(input())

if age < 10:
   print(5)
elif age == 60:
   print(0)
else:
   if bg >= 20:
      print(40)
   else:
      print(30)
