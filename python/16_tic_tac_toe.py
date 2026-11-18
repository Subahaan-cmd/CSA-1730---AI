# Experiment 16: Tic Tac Toe (Human = X, Computer = O using minimax)

WIN_LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]


def show(b):
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(b[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()


def winner(b):
    for a, c, d in WIN_LINES:
        if b[a] != ' ' and b[a] == b[c] == b[d]:
            return b[a]
    return None


def minimax(b, is_computer):
    w = winner(b)
    if w == 'O': return 1
    if w == 'X': return -1
    if ' ' not in b: return 0
    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O' if is_computer else 'X'
            scores.append(minimax(b, not is_computer))
            b[i] = ' '
    return max(scores) if is_computer else min(scores)


def computer_move(b):
    best, move = -2, None
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            s = minimax(b, False)
            b[i] = ' '
            if s > best:
                best, move = s, i
    return move


def play():
    board = [' '] * 9
    print("Tic Tac Toe - you are X, computer is O. Enter 1-9 (positions):")
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9")
    while True:
        show(board)
        try:
            pos = int(input("Your move (1-9): ")) - 1
        except (ValueError, EOFError):
            print("Invalid input."); 
            if EOFError: break
            continue
        if pos not in range(9) or board[pos] != ' ':
            print("Invalid / occupied cell, try again."); continue
        board[pos] = 'X'
        if winner(board) or ' ' not in board:
            break
        board[computer_move(board)] = 'O'
        if winner(board) or ' ' not in board:
            break
    show(board)
    w = winner(board)
    print("You win!" if w == 'X' else "Computer wins!" if w == 'O' else "It's a draw!")


if __name__ == "__main__":
    play()
