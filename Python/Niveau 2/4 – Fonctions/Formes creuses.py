def Line(n, char):
    for i in range(n):
        print(char, end="")

def Collon(n, char):
    for i in range(n):
        print(char)

def LineHole(n, char):
    print(char, end="")
    Line(n - 2, " ")
    print(char, end="")

def Rect(lines, col):
    if (lines == 1):
        Line(col, "#")
    elif (col ==  1):
        Collon(lines, "#")
    else:
        Line(col, "#")
        print()
        
        for i in range(lines - 2):
            LineHole(col, "#")
            print()

        Line(col, "#")

def Triangle(lines):
    print("@")

    for i in range(lines-2):
        LineHole(i+2, "@")
        print()

    Line(lines, "@")

nbX = int(input())
Line(nbX, "X")
print()
print()

linesRect = int(input())
colRect = int(input())
Rect(linesRect, colRect)
print()

linesTriangles = int(input())
Triangle(linesTriangles)
