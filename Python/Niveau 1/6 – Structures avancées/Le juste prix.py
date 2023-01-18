marchands = int(input())
minimum = 1000000

for i in range(marchands):
   val = int(input())
   if val <= minimum:
      minimum = val
      bst = i + 1
 
print(bst)
