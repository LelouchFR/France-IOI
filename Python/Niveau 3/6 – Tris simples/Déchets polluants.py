n, m = map(int, input().split())
pollution = list(map(int, input().split()))

pollution.sort(reverse=True)

print(" ".join(map(str, pollution[:m])))