letters = int(input())

for i in range(2*letters-1):
    for j in range(2*letters-1):
        if i < letters and j < letters:
            print(chr(ord("a") + min(i, j)), end="")
        elif i < letters and j >= letters:
            print(chr(ord("a") + min(i, 2*letters-2-j)), end="")
        elif i >= letters and j < letters:
            print(chr(ord("a") + min(2*letters-2-i, j)), end="")
        else:
            print(chr(ord("a") + min(2*letters-2-i, 2*letters-2-j)), end="")
    print()