def min2(x, y):
    if x < y:
        return x
    else:
        return y

mini = int(input())

for i in range(9):
    j = int(input())
    mini = min2(j, mini)

print(mini)
