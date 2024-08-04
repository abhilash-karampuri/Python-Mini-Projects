#tic-tac-toe
def print_board(board):
    for row in board:
        print(' | '.join(str(cell) for cell in row))
        print('-' * 10)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Top row
        [board[1][0], board[1][1], board[1][2]],  # Middle row
        [board[2][0], board[2][1], board[2][2]],  # Bottom row
        [board[0][0], board[1][0], board[2][0]],  # Left column
        [board[0][1], board[1][1], board[2][1]],  # Middle column
        [board[0][2], board[1][2], board[2][2]],  # Right column
        [board[0][0], board[1][1], board[2][2]],  # Diagonal (top-left to bottom-right)
        [board[0][2], board[1][1], board[2][0]]   # Diagonal (top-right to bottom-left)
    ]
    return [player, player, player] in win_conditions

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

player1 = "X"
player2 = "O"


game_over = False
current_player = player1

print_board(board)

while not game_over:
    try:
        move = int(input(f"Player {current_player}, enter your move (1-9): "))
        if move < 1 or move > 9:
            print("Invalid move. Please choose a number between 1 and 9.")
            continue

        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = current_player
                    break
            else:
                continue
            break
        else:
            print("The cell is already taken. Choose another cell.")
            continue

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            game_over = True
        elif is_full(board):
            print("It's a tie!")
            game_over = True
        else:
            current_player = player2 if current_player == player1 else player1

    except ValueError:
        print("Invalid input. Please enter a number.")
