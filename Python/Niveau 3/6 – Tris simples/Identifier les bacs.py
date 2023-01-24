bacss = int(input())
bacs = []
for i in range(bacss):
    ids, pollvl = map(int, input().split())
    bacs.append((ids, pollvl))

for ids, pollvl in sorted(bacs, key=lambda x: (x[1], x[0])):
    print(ids, pollvl)