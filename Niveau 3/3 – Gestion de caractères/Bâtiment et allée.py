author = input()
age = int(input())

letter = author[0]
num = ord(letter) - ord('A') + 1
allee = chr(age + ord('A') - 1)

print(num, end="")
print(allee)
