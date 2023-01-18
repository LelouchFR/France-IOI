n, m = map(int, input().split())
stock = list(map(int, input().split()))
bacs = list(map(int, input().split()))

ind = []
for bac in bacs:
    i = 0
    while i < len(stock) and stock[i] < bac:
        i += 1
    ind.append(i)
    stock.insert(i, bac)

print(" ".join(map(str, ind)))
print(" ".join(map(str, stock)))