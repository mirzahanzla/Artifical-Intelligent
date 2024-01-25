import math

# SP21_BSE-057


# Printed board on game fill in_output show
# def showborad(board):
#     for row in board:
#         # print(" ".join(map(lambda x: 'o' if x == 1 else 'x' if x == -1 else '.', row)))
#           print("(" + ",".join(map(lambda x: 'o' if x == 1 else 'x' if x == -1 else '0', row)) + ")")
def print_board(board):
    print(" ".join(board))


def is_winner(board, player):
    for i in range(7):
        if all(board[i + j] == player for j in range(3)):
            return True
    return False


start_move = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def is_board_full(board):
    return all(cell != " " for cell in board)


def get_avai_agent_move(board):
    return [i for i in range(9) if board[i] == " "]


def _alpha_beta(board, depth, alpha, beta, maximizing_player):
    result = evaluate(board)

    if result is not None:
        return result

    if maximizing_player:
        max_eval = -math.inf
        for move in get_avai_agent_move(board):
            board[move] = "X"
            eval_child = _alpha_beta(board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_child)
            alpha = max(alpha, eval_child)
            board[move] = " "
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_avai_agent_move(board):
            board[move] = "O"  # user
            eval_child = _alpha_beta(board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_child)
            beta = min(beta, eval_child)
            board[move] = " "
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval


print_board(start_move)


def evaluate(board):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None


while True:
    user_move = int(input("Choose position(0-8): "))
    if start_move[user_move] == " ":
        start_move[user_move] = "O"
        print_board(start_move)

        if is_winner(start_move, "O"):
            print("You win the game!")
            break
        elif is_board_full(start_move):
            print("It is draw!")
            break

        ai_agent_move = None
        best_eval = -math.inf
        for move in get_avai_agent_move(start_move):
            start_move[move] = "X"
            eval_child = _alpha_beta(start_move, 9, -math.inf, math.inf, False)
            start_move[move] = " "
            if eval_child > best_eval:
                best_eval = eval_child
                ai_agent_move = move

        print("AI   Agent  move to:", ai_agent_move)
        start_move[ai_agent_move] = "X"

        print_board(start_move)

        if is_winner(start_move, "X"):
            print("AI wins  the game!")
            break
        elif is_board_full(start_move):
            print("It is draw!")
            break
    else:
        print("Invalid move.")
