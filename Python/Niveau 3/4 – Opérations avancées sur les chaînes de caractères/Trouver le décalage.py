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
   
deezMaxFreq = ord('e') - ord('a')
alphabetSize = 26
text = input()
letterFreq = [0 for i in range(alphabetSize)]
maxFreq = 0
deezMax = -1
for letter in text.lower():
   if 'a' <= letter <= 'z':
      deez = ord(letter) - ord('a')
      letterFreq[deez] += 1
      if letterFreq[deez] > maxFreq :
         maxFreq = letterFreq[deez]
         deezMax = deez

key = (deezMax - deezMaxFreq) % alphabetSize
print(''.join(decoder(letter, key) for letter in text))