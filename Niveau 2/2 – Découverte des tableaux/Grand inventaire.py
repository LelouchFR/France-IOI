OP = int(input())
ings = [0] * 10

for i in range(OP):
    newIng = int(input()) - 1
    quantite = int(input())
    ings[newIng] += quantite

for ing in ings:
    print(ing)
