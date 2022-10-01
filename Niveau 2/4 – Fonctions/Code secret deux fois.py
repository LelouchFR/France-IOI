def code(x: int) -> str:
    password = 4242
    score = 1
    brute = 0

    def bruteforce(n: str) -> int:
        print(n)
        return int(input())

    while score != 3:
        
        while brute != password:
            brute = bruteforce("Entrez le code :")
        
        if brute == password:
            if brute == password and score == 2:
                print("Entrez le code :\nBravo.")
                break
            score += 1
            brute = bruteforce("Encore une fois.")
    pass
        
code(1)
