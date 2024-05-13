def read_sudoku():
    """Reads a Sudoku board from user input."""
    sudoku_board = []
    for i in range(9):
        while True:
            line = input(f"Enter row {i+1} (9 digits): ")
            if len(line) == 9 and all(c.isdigit() for c in line):
                sudoku_board.append(list(map(int,line)))
                break
            else:
                print("Invalid input. Please enter 9 digits.")         
    return sudoku_board


def check_box(box):
    """Checks if a 9-element box (row, column, or 3x3 block) is valid."""
    return set(box) == set(range(1, 10))
   
        
def is_valid_sudoku(board):
    """Checks if a Sudoku board is valid."""
    # Check rows
    for row in board:
        if not check_box(row):
            return False

    # Check columns
    for col in range(9):
        if not check_box([board[row][col] for row in range(9)]):
            return False

    # Check 3x3 blocks
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
            if not check_box(block):
                return False
            
    return True

if __name__ == "__main__":
    board = read_sudoku()
if is_valid_sudoku(board):
    print("Yes")
else:
    print("No")