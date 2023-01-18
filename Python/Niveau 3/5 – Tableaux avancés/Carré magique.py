import sys

N = int(input())
grid = []
for i in range(N):
  line = list(map(int, input().split()))
  grid.append(line)

sum_ = sum(grid[0])
for i in range(N):
  if sum(grid[i]) != sum_:
    print("no")
    sys.exit()
  column_sum = 0
  for j in range(N):
    column_sum += grid[j][i]
  if column_sum != sum_:
    print("no")
    sys.exit()

diag1_sum = 0
diag2_sum = 0
for i in range(N):
  diag1_sum += grid[i][i]
  diag2_sum += grid[i][N-i-1]
if diag1_sum != sum_ or diag2_sum != sum_:
  print("no")
  sys.exit()

numbers = set()
for i in range(N):
  for j in range(N):
    if grid[i][j] in numbers:
      print("no")
      sys.exit()
    numbers.add(grid[i][j])

for i in range(1, N**2+1):
  if i not in numbers:
    print("no")
    sys.exit()
    
print("yes")