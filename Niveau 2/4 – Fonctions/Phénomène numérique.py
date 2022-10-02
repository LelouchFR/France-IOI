def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1

inj = int(input())

while inj != 1:
    inj = collatz(inj)
    print(inj, end=" ")
