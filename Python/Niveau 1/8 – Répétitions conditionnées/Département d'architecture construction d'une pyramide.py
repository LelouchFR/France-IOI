PMax = int(input())
P = 0
stage = 0

while (P + (stage * stage)) <= PMax:
   P += (stage * stage)
   stage += 1
stage -= 1

print(stage)
print(P)
