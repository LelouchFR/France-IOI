lignes, mots = map(int, input().split(' '))
longueur = [0] * 101

for i in range(lignes):
    words = input().split(' ')
    for word in words:
        longueur[len(word)] += 1

for i in range(len(longueur)):
    if longueur[i] != 0:
        print(i, ' : ', longueur[i])
