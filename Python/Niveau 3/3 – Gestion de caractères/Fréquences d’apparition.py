def main():
    auth = [0] * 26
    line = input().lower()
    for letter in line:
        if 'a' <= letter <= 'z':
            auth[ord(letter) - ord('a')] += 1
    tot = sum(auth)
    for num in auth:
        print(num / tot)
main()
