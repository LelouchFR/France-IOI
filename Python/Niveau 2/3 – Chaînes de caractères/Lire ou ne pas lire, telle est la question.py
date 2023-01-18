livres = int(input())
Maxi = 0

for i in range(livres):
    title = input()
    
    if len(title) > Maxi:
        print(title)
        Maxi = len(title)
