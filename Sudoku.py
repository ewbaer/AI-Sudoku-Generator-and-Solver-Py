import random
import copy

def print_board(board):
    """Prints the Sudoku board in a readable 9x9 grid format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 38)  # Prints a horizontal line between 3x3 subgrids
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Prints a vertical line between 3x3 subgrids
            # Print each number with spacing for clarity
            print(board[i][j] if board[i][j] != 0 else ".", end="   ")
        print()  # Move to the next row

def find_empty(board):
    """Returns the (row, col) of an empty cell (denoted by 0)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # Empty cell is represented by 0
                return i, j
    return None  # No empty cells left

def is_valid(board, num, row, col):
    """Checks if it's valid to place num at (row, col)."""
    # Check the row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solves the Sudoku puzzle using backtracking."""
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # Puzzle solved, no empty cells

    row, col = empty_cell

    # Try placing numbers 1-9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num

            # Recur to try and solve with this assignment
            if solve_sudoku(board):
                return True

            # Backtrack if assigning num doesn't work
            board[row][col] = 0

    return False  # Trigger backtracking if no valid number found

def generate_sudoku():
    """Generates a random Sudoku puzzle by solving a board and removing cells."""
    # Initialize an empty board
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    # Solve the Sudoku to get a complete board
    solve_sudoku(board)
    
    return board

def remove_cells(board, difficulty):
    """Removes cells from the solved board to create a puzzle of the given difficulty."""
    puzzle = copy.deepcopy(board)
    
    # Set difficulty levels for number of cells to remove
    if difficulty == 'easy':
        cells_to_remove = random.randint(35, 40)
    elif difficulty == 'medium':
        cells_to_remove = random.randint(45, 50)
    else:  # hard
        cells_to_remove = random.randint(55, 60)
    
    for _ in range(cells_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:  # Ensure we don't remove from an already empty cell
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0
    
    return puzzle

def play_game():
    """Main function to run the Sudoku game."""
    while True:
        # Let the user choose difficulty
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        
        # Generate and remove cells based on difficulty
        board = generate_sudoku()
        puzzle = remove_cells(board, difficulty)
        
        print("\nSudoku Puzzle (Initial):")
        print_board(puzzle)
        
        # Ask the user when they want to see the completed result
        user_action = input("\nType 'check' to see the completed board: ").lower()
        
        if user_action == 'check':
            print("\nSudoku Puzzle (Completed):")
            print_board(board)
            
            # Ask the user if they want to play again
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("\nThanks for playing!")
                break
        else:
            print("Invalid input. Please type 'check' to see the completed board.")

if __name__ == "__main__":
    play_game()
