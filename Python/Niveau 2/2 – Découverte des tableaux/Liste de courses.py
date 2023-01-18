ingredients = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
tot = 0

for i in range(len(ingredients)):
   choix = int(input())
   tot += choix * ingredients[i]

print(tot)
