import numpy as np

# A Tic-Tac-Toe Board is a list made of lists
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]

player = 'X'

locs = {'a': 0, 'b': 1, 'c': 2}

def switchTurns(currentPlayer):
    if currentPlayer == 'X':
        player = 'O'
    else:
        player = 'X'


def chooseCell(location):
    if location[0].lower() == 'a':
    	process_input(a)


def process_input():

