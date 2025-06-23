def print_board(board):
    print("\nBoard:")
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
    
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, is_ai):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_board_full(board):
        return 0

    if is_ai:
        best_score = -999
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = 999
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    if score < best_score:
                        best_score = score
        return best_score

def get_ai_move(board):
    best_score = -999
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe - You (X) vs AI (O)")

    while True:
        print_board(board)

        # Player move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter numbers only.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = get_ai_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
