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


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if board[0] == board[1] and board[1] == board[2]:
        print_board(board)
        print(board[0], "has won")
        exit()
    elif board[3] == board[4] and board[4] == board[5]:
        print_board(board)
        print(board[3], "has won")
        exit()
    elif board[6] == board[7] and board[7] == board[8]:
        print_board(board)
        print(board[6], "has won")
        exit()
    elif board[0] == board[3] and board[3] == board[6]:
        print_board(board)
        print(board[0], "has won")
        exit()
    elif board[1] == board[4] and board[4] == board[7]:
        print_board(board)
        print(board[1], "has won")
        exit()
    elif board[2] == board[5] and board[5] == board[8]:
        print_board(board)
        print(board[2], "has won")
        exit()
    elif board[0] == board[4] and board[4] == board[8]:
        print_board(board)
        print(board[0], "has won")
        exit()
    elif board[2] == board[4] and board[4] == board[6]:
        print_board(board)
        print(board[0], "has won")
        exit()

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")