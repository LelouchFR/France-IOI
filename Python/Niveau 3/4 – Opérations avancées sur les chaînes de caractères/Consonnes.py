for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'a' or chr(i) == 'e' or chr(i) == 'i' or chr(i) == 'o' or chr(i) == 'u' or chr(i) == 'y':
        print('', end="")
    else:
        print(chr(i), end=" ")
