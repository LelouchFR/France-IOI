nNames = int(input())

for i in range(nNames):
    variable = input()
    if variable.isidentifier():
        print("YES")
    else:
        print("NO")
