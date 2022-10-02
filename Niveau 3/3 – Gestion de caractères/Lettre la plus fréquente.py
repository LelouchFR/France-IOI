def main():
    frequ = [0] * 26
    for letter in input():
        if 'a' <= letter <= 'z':
            frequ[ord(letter) - ord('a')] += 1
        if 'A' <= letter <= 'Z':
            frequ[ord(letter) - ord('A')] += 1

    maxFrequ = 0

    for i in range(26):
        if frequ[i] > maxFrequ:
            maxFrequ = frequ[i]
            maj = i
    print(chr(ord('A') + maj))

main()
