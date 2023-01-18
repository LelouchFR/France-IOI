start = int(input())
end = int(input())
personnes = int(input())
sus = 0

for i in range(personnes):
   a = int(input())
   b = int(input())
   
   if b >= start and a <= end:
      sus += 1
       
print(sus)
