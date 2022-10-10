traductions = int(input())
trad = []

for i in range(traductions):
   w1, w2 = input().split()
   trad.append((w2, w1))

trad.sort()

for (w2, w1) in trad:
   print(w2, w1)
