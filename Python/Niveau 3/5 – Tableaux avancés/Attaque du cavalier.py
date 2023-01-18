N = 8
vectors = [(1, 2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1)]
vectors = [(1,2), (2, 1)]

vectors.extend([(-k, l) for (k, l) in vectors])
vectors.extend([(k, -l) for (k, l) in vectors])

def Knight(chessBoard):
    result = False
    for i in range(N):
        for j in range(N):
            if chessBoard[i][j] == 'C':
                for k, l in vectors:
                    ik, jl = i + k, j + l
                    if 0 <= ik < N and 0 <= jl < N:
                        threatened = chessBoard[ik][jl]
                        if threatened != '.':
                            if 'a' <= threatened <= 'z':
                                result = True
    return result

chessBoard = [input() for i in range(N)]
print('yes' if Knight(chessBoard) else 'no')