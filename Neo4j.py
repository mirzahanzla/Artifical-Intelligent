import math

# def print_board(board):
#     for row in board:
#         print(" ".join(map(str, row)))

def print_board(board):
    for row in board:
        print(" ".join(map(lambda x: 'o' if x == 1 else 'x' if x == -1 else '.', row)))



# def is_winner(board, player):
#     for i in range(3):
#         if all(board[i][j] == player for j in range(3)) or \
#                 all(board[j][i] == player for j in range(3)):
#             return True
#     if all(board[i][i] == player for i in range(3)) or \
#             all(board[i][2 - i] == player for i in range(3)):
#         return True
#     return False


def is_winner(board, player):
    for i in range(3):
     
        row_win = all(board[i][j] == player for j in range(3))
        col_win = all(board[j][i] == player for j in range(3))
        if row_win or col_win:
            return True
    diag1_win = all(board[i][i] == player for i in range(3))
    diag2_win = all(board[i][2 - i] == player for i in range(3))

    if diag1_win or diag2_win:
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != 0 for i in range(3) for j in range(3))


def evaluate(board):
    if is_winner(board, 1):  # Max player wins
        return 1
    elif is_winner(board, -1):  # Min player wins
        return -1
    elif is_board_full(board):  # It's a draw
        return 0
    else:
        return None  # Game is not over


def get_available_moves(board):
    # Return a list of available moves (empty cells)
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                moves.append((i, j))
    return moves


def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    result = evaluate(board)

    if result is not None:
        return result

    if maximizing_player:
        max_eval = -math.inf
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = 1  # Max player's move
            eval_child = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_child)
            alpha = max(alpha, eval_child)
            board[i][j] = 0  # Undo move
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = -1  # Min player's move
            eval_child = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_child)
            beta = min(beta, eval_child)
            board[i][j] = 0  # Undo move
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval


# Example usage for playing Tic Tac Toe
initial_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print_board(initial_board)

while True:
    user_move = tuple(map(int, input("Enter your move (row and column): ").split()))
    if initial_board[user_move[0]][user_move[1]] == 0:
        initial_board[user_move[0]][user_move[1]] = -1  # Min player's move
        print_board(initial_board)

        if is_winner(initial_board, -1):
            print("You win!")
            break
        elif is_board_full(initial_board):
            print("It's a draw!")
            break

        # AI's move
        ai_move = None
        best_eval = -math.inf
        for move in get_available_moves(initial_board):
            i, j = move
            initial_board[i][j] = 1  # Max player's move
            eval_child = minimax_alpha_beta(initial_board, 5, -math.inf, math.inf, False)
            initial_board[i][j] = 0  # Undo move
            if eval_child > best_eval:
                best_eval = eval_child
                ai_move = move

        print("AI's move:", ai_move)
        initial_board[ai_move[0]][ai_move[1]] = 1  # Max player's move

        print_board(initial_board)

        if is_winner(initial_board, 1):
            print("AI wins!")
            break
        elif is_board_full(initial_board):
            print("It's a draw!")
            break
    else:
        print("Invalid move. Try again.")