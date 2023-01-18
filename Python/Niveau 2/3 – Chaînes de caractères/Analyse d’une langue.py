lettre = input()
lines = int(input())
tot = 0

for i in range(lines):
    line = input()
    for char in line:
        if char == lettre:
            tot += 1
print(tot)
