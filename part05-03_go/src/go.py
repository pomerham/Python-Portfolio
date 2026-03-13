# Write your solution here
def who_won(game_board: list):
    p1 = 0
    p2 = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            #print(game_board[i][j])  prints out if we are on the right index for debug
            if game_board[i][j] == 1:
                p1 += 1
            elif game_board[i][j] == 2:
                p2 += 1
    if p1 > p2:
        return 1
    elif p2 > p1:
        return 2
    else:
        return 0


if __name__ == "__main__":
    go = [
        [0, 0, 0],
        [0, 2, 0],
        [1, 1, 2],
    ]
    print(who_won(go))

