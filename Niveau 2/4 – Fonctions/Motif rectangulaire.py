def rect(longueur, largueur, letter) -> str:
    for i in range(longueur):
        print(letter * largueur)

rect(int(input()), int(input()), input())
