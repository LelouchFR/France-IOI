N, M = map(int, input().split())
T = [['.'] * M for i in range(N)]

for i in range(int(input())):
    iLig1, iCol1, iLig2, iCol2, char = input().split()

    for j in range(int(iLig1), int(iLig2) + 1):
        for k in range(int(iCol1), int(iCol2) + 1):
            T[j][k] = char
            
for t in T:       
    print("".join(t))