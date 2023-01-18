def code() -> str:
    password = 4242
    password2 = 2121
    score = 1
    brute = 0

    def bruteforce(n: str) -> int:
        print(n)
        return int(input())

    while score != 3:
        
        if brute != password or brute != password2:
            brute = bruteforce("Entrez le code :")
        
        if brute == password:
            score += 1
            brute = bruteforce("Premier code bon.")
        elif brute == password2 and score == 2:
            print("Entrez le code :\nBravo.")
            break
    pass
        
code()
