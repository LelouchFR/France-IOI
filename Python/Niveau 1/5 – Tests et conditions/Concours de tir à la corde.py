membres = int(input())
p1 = 0
p2 = 0

for i in range(membres):
    p1 += int(input())
    p2 += int(input())

if p1 > p2:
    print("L'équipe 1 a un avantage")
elif p2 > p1:
    print("L'équipe 2 a un avantage")

print("Poids total pour l'équipe 1 : ",p1)
print("Poids total pour l'équipe 2 : ",p2)
