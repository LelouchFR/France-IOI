def check_winner(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            count = 0
            k = j
            while k < len(board[i]) and board[i][k] == board[i][j]:
                count += 1
                k += 1
            if count >= 5 and board[i][j] != 0:
                return board[i][j]

            count = 0
            k = i
            while k < len(board) and board[k][j] == board[i][j]:
                count += 1
                k += 1
            if count >= 5 and board[i][j] != 0:
                return board[i][j]

            count = 0
            k, l = i, j
            while k < len(board) and l < len(board[k]) and board[k][l] == board[i][j]:
                count += 1
                k += 1
                l += 1
            if count >= 5 and board[i][j] != 0:
                return board[i][j]

            count = 0
            k, l = i, j
            while k >= 0 and l < len(board[k]) and board[k][l] == board[i][j]:
                count += 1
                k -= 1
                l += 1
            if count >= 5 and board[i][j] != 0:
                return board[i][j]
    return 0

n = int(input())

board = []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)

winner = check_winner(board)
print(winner)