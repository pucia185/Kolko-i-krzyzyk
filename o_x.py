def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        return "Remis"

    return None


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print("Ruch gracza", current_player)
        row = int(input("Podaj numer wiersza (0-2): "))
        col = int(input("Podaj numer kolumny (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print("Gracz", winner, "wygrywa!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            print("To pole jest już zajęte. Spróbuj ponownie.")


play_game()
