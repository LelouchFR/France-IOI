nums = int(input())
result = list(map(int, input().split()))

result.sort()

print(' '.join(map(str, result)))