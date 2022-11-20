acronym = input()
for i in range(int(input())):
    titles = input().split()
    if len(titles) == len(acronym):    
        res = ""
        for j in range(len(titles)):
            if titles[j][0].lower() == acronym[j][0].lower():
                res += titles[j].capitalize() + " "
            else:
                res = ""
        print(res)
