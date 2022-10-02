title = input()
author = input()
vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'I', 'E', 'O', 'U', 'Y')

for char in title:
    if char in vowels:
        title = title.replace(char, '')

for char in author:
    if char in vowels:
        author = author.replace(char, '')

print((title + '\n' + author).replace(" ", ""))
