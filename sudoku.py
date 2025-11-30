# class for keeping track of individual tiles
class Tile:
    def __init__(self, row, col, value=0):
        self.row = row
        self.col = col
        self.value = value

    def is_empty(self):
        return self.value == 0

    def set_value(self, new_value):
        self.value = new_value

    def clear(self):
        self.value = 0


# class for tracking and displaying the whole board
class Board:
    def __init__(self, startGrid=None):
        self.cells = []

        for r in range(9):
            row = []
            for c in range(9):
                if startGrid is None:
                    value = 0
                else:
                    value = startGrid[r][c]
                row.append(Tile(r, c, value))
            self.cells.append(row)

    def get_cell(self, row, col):
        return self.cells[row][col]

    def set_cell(self, row, col, value):
        self.cells[row][col].set_value(value)

    def print_board(self):
        for r in range(9):
            row_values = []
            for c in range(9):
                v = self.cells[r][c].value
                #prints . if a value isnt available
                row_values.append(str(v) if v != 0 else ".")
            print(" ".join(row_values))

    # check if any tiles are empty, if none are we hopefully have it solved
    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].is_empty():
                    return r, c
        return None

    def is_valid(self, row, col, value):
        # check row validity
        for c in range(9):
            if self.cells[row][c].value == value:
                return False

        # check column validity
        for r in range(9):
            if self.cells[r][col].value == value:
                return False

        # check 3x3 square validity
        box_r = (row // 3) * 3
        box_c = (col // 3) * 3
        for rr in range(box_r, box_r + 3):
            for cc in range(box_c, box_c + 3):
                if self.cells[rr][cc].value == value:
                    return False

        return True
    
    def clear_cell(self, row, col):
        # sets the tile back to empty for fixing mistakes
        self.cells[row][col].clear()

    def solve(self):
        empty = self.find_empty()
        if empty is None:
            return True  # should be solved

        row, col = empty

        for value in range(1, 10):
            if self.is_valid(row, col, value):
                self.cells[row][col].set_value(value)

                if self.solve():
                    return True

                # backtracking
                self.cells[row][col].clear()

        return False


def main():
    board = Board()
    print("Initial Empty Sudoku board:")
    board.print_board()
    print()
    print("Enter clues as row column value")
    print("Rows and columns are 1-9 (top-left is 1 1).")
    print("Type 'solve' when you are ready to solve.")
    print("Type 'erase' to erase a cell.")
    print("Type 'show' to display the current board.\n")

    while True:
        #make sure anything entered doesnt have unnecessary character or uppercase for conflicts
        line = input("Enter: ").strip().lower()

        #move on past this while loop to solve
        if line == "solve":
            break
        
        if line == "show":
            board.print_board()
            continue

        if line == "erase":
            print("enter row and column: ")


        #making sure not to run with an empty line
        if not line:
            continue

        parts = line.split()
        if len(parts) != 3:
            print("Please enter: row col value or 'solve'")
            continue

        try:
            # converts the split parts into 3 ints, row, column, and value
            r, c, v = map(int, parts)
        except ValueError:
            # ValueError makes sure that an int was entered
            print("Row, col, and value must be integers 1-9.")
            continue

        # make sure all entered numbers are between 1 and 9
        if not (1 <= r <= 9 and 1 <= c <= 9 and 1 <= v <= 9):
            print("Row, col, and value must be between 1 and 9.")
            continue

        # convert entered values to index for lists
        row = r - 1
        col = c - 1

        # check to make sure the clues aren't automatically invalidating the board
        if not board.is_valid(row, col, v):
            print("Value conflicts with board")
            continue

        board.set_cell(row, col, v)
        print("Updated board:")
        board.print_board()
        print()

    print("\nSolving...")
    if board.solve():
        print("Solved board:")
        board.print_board()
    else:
        print("No solution found.")


main()