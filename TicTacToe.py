# Board Layout
#    A   B   C
#  -------------
# 1 |   |   |   |
#  -------------
# 2 |   |   |   |
#  -------------
# 3 |   |   |   |
#  -------------
def board_layout(board):
    print("    A   B   C")
    print("  -------------")
    for i in range(len(board)):
        print(f"{i + 1} | {' | '.join(board[i])} |")
        print("  -------------")

# Player input and valid input check
def get_move(board, player):
    while True:
        # Get player move and change to upper to make it case-insensitive
        move = input("Player " + player + ", enter your move (e.g. A1): ").upper()
        # Allow user to input 1a or a1 either is fine
        if len(move) != 2 or move[0] not in ['A', 'B', 'C'] or move[1] not in ['1', '2', '3']:
            if len(move) == 2 and move[0] in ['1', '2', '3'] and move[1] in ['A', 'B', 'C']:
                move = move[1] + move[0]
            else:
                print("Invalid move. Please enter a valid move.")
                continue
        row = int(move[1]) - 1
        col = ord(move[0]) - ord('A')
        # Check if space is already used
        if board[row][col] != ' ':
            print("That space is already taken. Please enter a valid move.")
        else:
            return row, col


# Check win conditions. Horizontal/Vertical/Diagonal
def check_win(board):
    for i in range(3):
        # Horizontal Win
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        # Vertical Win
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    # Diagonal win, both sides
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False


def tic_tac_toe():
    # Board array
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    # Player symbols
    players = ['X', 'O']
    current_player = players[0]

    while True:
        # Display current board layout
        board_layout(board)
        # Get the row and col corresponding to the player input
        row, col = get_move(board, current_player)
        # update the board with the player position and symbol
        board[row][col] = current_player
        # Check win yet
        if check_win(board):
            board_layout(board)
            print("Player " + current_player + " wins!")
            break
        # Tie if the board is filled without winner
        elif all(' ' not in row for row in board):
            board_layout(board)
            print("Tie game!")
            break
        else:
            # switch player
            current_player = players[(players.index(current_player) + 1) % 2]


if __name__ == '__main__':
    tic_tac_toe()
