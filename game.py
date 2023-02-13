def print_board(entries):
    line = "+---+---+---+"
    output = line
    n = 0
    for entry in entries:
        if n % 3 == 0:
            output = output + "\n| "
        else:
            output = output + " | "
        output = output + str(entry)
        if n % 3 == 2:
            output = output + " |\n"
            output = output + line
        n = n + 1
    print(output)
    print()

def game_over(board, i):

    print_board(board)
    print("GAME OVER")
    print(board[i], "has won")
    exit()
    return

def is_row_winner(board, row_num):
    if board[row_num] == board[row_num+1] and board[row_num+1] == board[row_num+2]:
        return True
    else:
        return False

def is_column_winner(board, column_num):
    if board[column_num] == board[column_num+3] and board[column_num+3] == board[column_num+6]:
        return True
    else:
        return False

def is_diagonal_winner(board, diagonal_num):
    if diagonal_num == 0 and board[diagonal_num] == board[diagonal_num+4] == board[diagonal_num+8]:
        return True
    if diagonal_num == 2 and board[diagonal_num] == board[diagonal_num+2] == board[diagonal_num+4]:
        return True
    return False

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if is_row_winner(board, 0):
        game_over(board, 0)
    elif is_row_winner(board, 3):
        game_over(board, 3)
    elif is_row_winner(board, 6):
        game_over(board, 6)
    elif is_column_winner(board, 0):
        game_over(board, 0)
    elif is_column_winner(board, 1):
        game_over(board, 1)
    elif is_column_winner(board, 2):
        game_over(board, 2)
    # elif board[0] == board[4] and board[4] == board[8]:
    #     game_over(board, 0)
    # elif board[2] == board[4] and board[4] == board[6]:
    #     game_over(board, 2)
    elif is_diagonal_winner(board, 0):
        game_over(board, 0)
    elif is_diagonal_winner(board, 2):
        game_over(board, 2)

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")
