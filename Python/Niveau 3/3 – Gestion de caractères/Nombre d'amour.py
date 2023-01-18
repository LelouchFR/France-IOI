def value(word: str) -> int:
    tot = 0
    for letter in word:
        tot += ord(letter) - ord('A')
    return tot

def nombreAmour(n: int) -> int:
    amour = 0
    while n > 0:
        unite = n % 10
        amour += unite
        n //= 10
    if amour < 10:
        return amour
    else:
        return nombreAmour(amour)

name1, name2 = input().split()
print(nombreAmour(value(name1)), nombreAmour(value(name2)))
