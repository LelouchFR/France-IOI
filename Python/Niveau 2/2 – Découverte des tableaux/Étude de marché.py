prod = int(input())
prods = [0] * prod
personnes = int(input())

for i in range(personnes):
    prefProd = int(input())
    prods[prefProd] += 1

for prod in prods:
    print(prod)
