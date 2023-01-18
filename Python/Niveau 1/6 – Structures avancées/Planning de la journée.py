position = int(input())
v = 0   
villages = int(input())
for i in range(villages):
   villesPo = int(input())
   if villesPo - position <= 50 and villesPo - position >= -50:
      v += 1
print(v)
