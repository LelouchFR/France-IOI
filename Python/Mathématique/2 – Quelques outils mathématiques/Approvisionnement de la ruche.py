from math import sqrt

xHive, yHive = int(input()), int(input())
count = 0

for i in range(int(input())):
    xFlower, yFlower = int(input()), int(input())
    dist = sqrt((xFlower - xHive) ** 2 + (yFlower - yHive) ** 2)
    if dist < 1000:
        count += 1

print(count)