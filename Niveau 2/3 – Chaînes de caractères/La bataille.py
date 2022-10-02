CJ1 = input()
CJ2 = input()

CsJ1 = len(CJ1)
CsJ2 = len(CJ2)

i = 0

while i < CsJ1 and i < CsJ2 and CJ1[i] == CJ2[i]:
    i += 1

if CsJ1 == CsJ2:
    if i == CsJ1:
        print('=')
    elif CJ1[i] < CJ2[i]:
        print('1')
    else:
        print('2')
else:
    if i == CsJ1:
        print('2')
    elif i == CsJ2:
        print('1')
    elif CJ1[i] < CJ2[i]:
        print('1')
    else:
        print('2')
print(i)
