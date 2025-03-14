#BACKTRACKING
'''"Backtracking" is a problem-solving algorithm  where solutions are abandoned when they 
cannot lead to a valid solution, returning to a previous state to try a different path. '''
#ASCII
#WORKS ONLY WHEN n>=4
'''The N-Queens problem is a classic backtracking algorithm where we aim to place N queens on an
N*N chessboard such that no two queens attack each other.'''
def print_board_ascii(board, n):    
    for i in range(n):
        print(" " + " ----" * n)  #Top border 
        row = "|"
        for j in range(n):
            if board[i] == j:
                row += " Q  |"  #Queen
            else:
                row += "    |"  #Empty square
        print(row)
    print(" " + " ----" * n)  #Bottom border


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens(board, row, n):
    #Backtracking fn to solve N-Queens.
    if row == n:
        print_board_ascii(board, n)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_n_queens(board, row + 1, n):
                return True
            board[row] = -1  # Backtrack
    return False


def n_queens(n): #fn initialisation to solve
    board = [-1] * n
    solve_n_queens(board, 0, n)

n= int(input("Enter number of Queens: "))
n_queens(n)
