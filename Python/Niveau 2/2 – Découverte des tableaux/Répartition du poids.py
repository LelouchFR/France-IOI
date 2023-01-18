charrettes = int(input())

weight = [0.0] * charrettes 
totWeight = 0.0

for i in  range(charrettes):
   weight[i] = float(input())
   totWeight += weight[i]
   
   
moyenWeight = totWeight / charrettes
   
for charWeight in weight:
   print(moyenWeight - charWeight)
