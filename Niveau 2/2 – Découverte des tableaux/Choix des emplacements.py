placements = int(input())
marchands = [0] * placements

for i in range(placements):
    marchands[int(input())] = i

for marchand in marchands:
    print(marchand)
