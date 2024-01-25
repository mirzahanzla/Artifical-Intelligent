import math

def show_board(board):
    for i in range(0, 9, 3):
        print(" ".join(map(lambda x: 'o' if x == 1 else 'x' if x == -1 else '.', board[i:i+3])))

def is_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        row_win = all(board[i + j] == player for j in range(3))
        if row_win:
            return True

    # Check columns
    for i in range(3):
        col_win = all(board[i + 3 * j] == player for j in range(3))
        if col_win:
            return True

    # Check diagonals
    diag1_win = all(board[i] == player for i in range(0, 9, 4))
    diag2_win = all(board[i] == player for i in range(2, 7, 2))

    if diag1_win or diag2_win:
        return True

    return False

def board_full(board):
    return all(cell != 0 for cell in board)

def evaluate(board):
    if is_winner(board, 1):  # Max 
        return 1
    elif is_winner(board, -1):  # Min
        return -1
    elif board_full(board):  # It is  draw
        return 0
    else:
        return None 

def get_available_moves(board):
    moves = []
    for i, cell in enumerate(board):
        if cell == 0:
            moves.append(i)
    return moves

def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    result = evaluate(board)

    if result is not None:
        return result

    if maximizing_player:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 1  # Max player's move
            eval_child = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_child)
            alpha = max(alpha, eval_child)
            board[move] = 0  # Undo move
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = -1  # Min player's move
            eval_child = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_child)
            beta = min(beta, eval_child)
            board[move] = 0  # Undo move
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

initial_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

show_board(initial_board)

while True:
    user_move = int(input("Enter your move (0-8): "))
    if initial_board[user_move] == 0:
        initial_board[user_move] = -1  # Min player move
        show_board(initial_board)

        if is_winner(initial_board, -1):
            print("You win!")
            break
        elif board_full(initial_board):
            print("It's a draw!")
            break

        # AI Agent move
        ai_agent_move = None
        best_eval = -math.inf
        for move in get_available_moves(initial_board):
            initial_board[move] = 1  # Max player's move
            eval_child = minimax_alpha_beta(initial_board, 5, -math.inf, math.inf, False)
            initial_board[move] = 0  # Undo move
            if eval_child > best_eval:
                best_eval = eval_child
                ai_agent_move = move

        print("AI agent to move it:", ai_agent_move)
        initial_board[ai_agent_move] = 1  # Max player's move

        show_board(initial_board)

        if is_winner(initial_board, 1):
            print("AI wins!")
            break
        elif board_full(initial_board):
            print("It's a draw!")
            break
    else:
        print("Invalid move. Try again.")
