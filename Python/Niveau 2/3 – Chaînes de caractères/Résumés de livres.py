livres = int(input())
mini = int(input())

for i in range(livres):
    title = input()
    description = input()

    if len(description) < mini:
        print(title)
