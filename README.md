# Sudoku Solver

A command-line Sudoku solver written in Python. Enter your puzzle's clues interactively and the program will solve it instantly using a recursive backtracking algorithm.

---

## How It Works

The solver uses a backtracking algorithm to find the solution:

1. Scan the board for the next empty cell
2. Try placing digits 1–9, checking each against three constraints: no duplicates in the same row, column, or 3×3 box
3. If a digit is valid, place it and recurse to the next empty cell
4. If no digit works, backtrack — clear the cell and try the next option in the previous cell
5. Repeat until the board is fully filled (solved) or all possibilities are exhausted (no solution)

The board is modeled with two classes: `Tile` tracks an individual cell's position and value, and `Board` manages the full 9×9 grid, constraint checking, and the solve logic.

---

## Getting Started

**Requirements:** Python 3.x — no external libraries needed.

```bash
git clone https://github.com/Lmsulliv/python-sudoku-solver.git
cd sudoku-solver
python solver.py
```

---

## Usage

When you run the program, you'll see an empty board and a prompt. Enter clues one at a time as `row col value`, where rows and columns are numbered 1–9 from the top-left.

```
Enter: 1 1 5       # Places 5 in row 1, column 1
Enter: show        # Displays the current board
Enter: erase       # Erases a cell
Enter: solve       # Solves the puzzle
```

### Example

**Input puzzle (clues entered one by one):**
```
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

**Solved output:**
```
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

---

## Possible Future Improvements

- Add a GUI using `tkinter` or `pygame`
- Support importing puzzles from a text file or image (via OpenCV)
- Display solve time and number of backtracks taken
- Add puzzle difficulty detection

---

## What I Learned

- Implementing recursive backtracking and understanding how constraint propagation prunes the search space
- Designing object-oriented Python with clean separation between data (`Tile`) and logic (`Board`)
- Building an interactive CLI with input validation and error handling