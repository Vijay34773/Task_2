def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, symbol):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == symbol for s in row):
            return True
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):

        return True
    return False

def play_tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_symbol = "X"
        moves = 0
        while moves < 9:
            print_board(board)
            try:
                move = int(input(f"Player {current_symbol}, enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    board[row][col] = current_symbol
                    if check_winner(board, current_symbol):
                        print_board(board)
                        print(f"Player {current_symbol} wins!")
                        break
                    current_symbol = "O" if current_symbol == "X" else "X"
                    moves += 1
                else:
                    print("Spot already taken, try again.")
            except (ValueError, IndexError):
                print("Invalid input, try again.")
        else:
            print("It's a draw!")
        if input("Play again? (yes/no): ").lower() != "yes":
            break

play_tic_tac_toe()
