cotes = int(input())
pos = 0
neg = 0

for i in range(cotes):
   denivele = int(input())
   
   if denivele > 0:
      pos += denivele
   elif denivele <= 0:
      neg += denivele

print(pos)
print(-neg)
