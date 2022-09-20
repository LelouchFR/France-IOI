numP = int(input())
Lsize = int(input())
kata = False

for i in range(Lsize):
   num = int(input())   
   if num == numP:
      kata = True
      
if kata:
   print("Sorti de la ville")
else:
   print("Encore dans la ville")
