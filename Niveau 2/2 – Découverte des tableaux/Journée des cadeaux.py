hab = int(input())
fortunes = [0] * hab

for i in range(hab):
    fortunes[i] = int(input())

fortunes.sort()

mediane = 0
moyenne = (hab - 1) // 2

if hab % 2 == 1:
    mediane = fortunes[moyenne]
else:
    mediane = (fortunes[moyenne] + fortunes[moyenne + 1]) / 2

print(mediane)
