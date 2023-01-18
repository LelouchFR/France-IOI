dep = int(input())

deps = [0] * dep

for i in range(dep):
   deps[i] = int(input())
   
for i in range(dep - 1, -1, -1):
   depl = deps[i]
   if (depl == 1):
      print(2)
   elif (depl == 2):
      print(1)
   elif (depl == 4):
      print(5)
   elif (depl == 5):
      print(4)
   elif (depl == 3):
      print(3)
