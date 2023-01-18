personnes = int(input())
Lpersonnes = [0] * personnes

for i in range(personnes):
    Lpersonnes[i] = int(input())

Lpersonnes.sort()

for i in range(personnes // 2):
    print("{} {}".format(Lpersonnes[i], Lpersonnes[personnes - 1 - i]))
