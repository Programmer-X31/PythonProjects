from tkinter import *

grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

root = Tk()
root.title("Sudoku Solver with Backtracking")


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global grid
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for n in range(1, 10):
                    if possible(row, column, n) == True:
                        grid[row][column] = n
                        solve()
                        grid[row][column] = 0
                return
    print_board(grid)
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            Label(text=str(grid[row][cell]), borderwidth=1, relief="solid", font="comicsans 10").grid(row=row, column=cell, ipadx=10, ipady=5)
    root.mainloop()


solve()

