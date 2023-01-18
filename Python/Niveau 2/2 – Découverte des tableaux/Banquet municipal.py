pos = int(input())
changePos = int(input())
positions = [0] * pos

for i in range(pos):
    positions[i] = int(input())

for i in range(changePos):
    index1 = int(input())
    index2 = int(input())   
    positions[index1], positions[index2] = positions[index2], positions[index1]

for numP in positions:
    print(numP)
