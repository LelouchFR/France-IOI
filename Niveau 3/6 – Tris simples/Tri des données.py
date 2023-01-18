n = int(input())
levels = list(map(int, input().split()))

levels.sort()

for level in levels:
    print(level, end=' ')