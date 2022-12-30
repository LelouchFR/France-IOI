def decoder(letter: str, key: int) -> str:
   def turn_around(letter, pivot, key):
      deez = ord(letter) - ord(pivot)
      deez_decoded = (deez - key) % 26
      return chr(ord(pivot) + deez_decoded)
   result = ''      
   if 'a' <= letter <= 'z':
      result = turn_around(letter, 'a', key)
   elif 'A' <= letter <= 'Z':
      result = turn_around(letter, 'A', key)
   else:
      result = letter
   return result
   
pages = int(input())
for i in range(2, pages + 1):
   line = input()
   key = (-5 * i) if i % 2 == 1 else (3 * i)
   print(''.join((decoder(letter, key) for letter in line)))