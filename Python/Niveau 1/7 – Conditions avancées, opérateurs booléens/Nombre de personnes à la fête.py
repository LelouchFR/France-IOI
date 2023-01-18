persons = int(input())
present = 0
pmax = 0
  
for loop in range (persons * 2):
     p = int(input())
       
     if p > 0 :
          present += 1
          if present > pmax:
             pmax = present
     elif p <= 0 :
          present -= 1
       
print(pmax)
