lieux = int(input())
ville = 0

for i in range(lieux):
    Hab = int(input())
    if Hab > 10000:
        ville += 1
print(ville)
