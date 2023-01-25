blocks = int(input())
n = set(map(int, input().split()))
clientsQ = int(input())

for _ in range(clientsQ):
    block = int(input())
    print(1) if block in n else print(0)