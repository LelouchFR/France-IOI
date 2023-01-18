def decoder(letter: str) -> str:
   if 'a' <= letter <= 'z':
      return grid[ord(letter) - ord('a')]
   elif 'A' <= letter <= 'Z':
      min_char = grid[ord(letter) - ord('A')]
      maj_char = chr(ord(min_char) - ord('a') + ord('A'))
      return maj_char
   else:
      return letter
     
grid = list(input())
text = input()
print(''.join((decoder(letter) for letter in text)))
