# --------------------------------------------
#   Name: Raquib Khan Lavani
#   ID: 1622108
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise #6: OOMinimax
# --------------------------------------------

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)

Raquib Khan
CCID:  lavani
"""

from math import inf as infinity
from random import choice
from random import seed as randomseed       # Paul Lu
import platform
import time
from os import system
import copy


class Board:
    ''' A class which converts the previously global board to now, an object.
    Essentially, the class takes in a board, the player's choice,the
    computer's choice. It is then able to modify the board object
    by setting the move of either the player, or the computer. To do so, it
    also invokes other methods of the  same class, which check whether
    the move being set by the player is valid and
    checking if either player has won. Designed to encapsulate the board, and
    hides the implementation of setting and validating moves on
    the board, along with checking the board to see if a player has won. '''
    def __init__(self, h_choice,
                 c_choice, board=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.h_choice = h_choice
        self.c_choice = c_choice
        self.board = board
        self.cells = []
        self.player = 0

    def __str__(self):
        return ('Board with human choice as ' + self.h_choice
                + ' and computer choice as ' + self.c_choice)

    def __repr__(self):
        return 'Board object represented by nested list: ' + str(self.board)

    def get_h_choice(self):
        # Gets the choice of player
        return self.h_choice

    def get_c_choice(self):
        # Gets the choice of computer
        return self.c_choice

    def get_player(self):
        # Gets the value of player (1 for computer, -1 for human)
        return self.player

    def get_board(self):
        # Gets the nested list which represents the board
        return self.board

    def render(self):
        # Renders the board on std output (terminal). Formats the board
        # with the symbol which each player chose, and a blank space
        # if the cell on the board is unused.
        # Defines internal variable chars
        chars = {
            -1: self.get_h_choice(),
            +1: self.get_c_choice(),
            0: ' '
        }
        str_line = '---------------'
        # Prints the symbol chosen by each respective player (X or O) in the
        # stdout rendition of the board
        print('\n' + str_line)
        for row in self.get_board():
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)

    def empty_cells(self):
        # Returns the values and enumeration of an element which is unused (0)
        # in the nested list which represents the board.
        self.cells = []
        for x, row in enumerate(self.get_board()):
            for y, cell in enumerate(row):
                if cell == 0:
                    self.cells.append([x, y])

        return self.cells

    def valid_move(self, x, y):
        # Validates the moves a player, precisely the human makes. If
        # the particular cell of the board chosen by the human is already
        # occupied by a symol, this function return False.
        """
        A move is valid if the chosen cell is empty
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the board[x][y] is empty
        """
        if [x, y] in self.empty_cells():
            return True
        else:
            return False

    def set_move(self, x, y, player):
        # Sets the move of each respective player, if coordinates are valid.
        """
        Set the move on board, if the coordinates are valid
        :param x: X coordinate
        :param y: Y coordinate
        :param player: the current player
        """
        # Setting player of the instance to the player mentioned as parameter
        self.player = player
        # Validating move, and setting it if move is valid
        if self.valid_move(x, y):
            self.board[x][y] = self.player
            return True
        else:
            return False

    def get_depth(self):
        # Gets the number of empty cells in the board
        self.depth = len(self.empty_cells())
        return self.depth

    def win_state(self, player):
        # Checks each winning state with the board to see if either player
        # has won.

        self.win_board = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]

        # Checks if there are three consecutive 'player' values in
        # any win permutation
        if [player, player, player] in self.win_board:
            return True
        else:
            return False

    def game_over(self):
        # Returns True if either the human or the computer wins the game
        return self.win_state(HUMAN) or self.win_state(COMP)

    def evaluate(self):
        # Evaluates the board and defines internal variable 'score' as +1
        # if computer wins or -1 if human wins. Returns the score
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if self.win_state(COMP):
            score = +1
        elif self.win_state(HUMAN):
            score = -1
        else:
            score = 0

        return score


class Turn:
    ''' This class is called for each turn of either player, the Human, or
    the computer. It hides the working of setting the move of each player,
    and calling the board object and methods of the Board object to modify
    the state of the board (i.e. set the turn of the player). '''

    # Initializing the class with the state of the board, the choice (X or O)
    # of either player as parameters
    def __init__(self, state, c_choice, h_choice):
        self.state = state
        self.c_choice = c_choice
        self.h_choice = h_choice

    def __str__(self):
        return ('Turn object with human choice as ' + self.h_choice
                + ' and computer choice as ' + self.c_choice)

    def __repr__(self):
        return 'Board object which will be modified: ' + str(self.state)

    # Gets the choice of the computer
    def get_c(self):
        return self.c_choice

    # Gets the choice of the human
    def get_h(self):
        return self.h_choice

    # Method which is used to set the human turn. It takes the choice of each
    # player, as the parameter and prompts the human player in the terminal for
    # the position where the human wants to place their symbol.
    # It takes in the input, validates the move, and sets it on
    # the instance of the board passed in as the
    # parameter to this class
    def human_turn(self, c_choice, h_choice):
        if b.get_depth() == 0 or b.game_over():
            return

        # Setting internal variables
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        # Clears the terminal
        clean()
        print(f'Human turn [{self.h_choice}]')
        # Calling the instance of the 'Board' class passed in, and
        # rendering it on stdout
        b.render()
        # Checks if number inputted is a valid index of the board
        while move < 1 or move > 9:
            try:
                # Takes input
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]
                can_move = b.set_move(coord[0], coord[1], HUMAN)

                # Printing bad move if index is wrong/ already occupied
                if not can_move:
                    print('Bad move')
                    move = -1

            # Error handling
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

    def ai_turn(self, c_choice, h_choice):

        # Method which is used to set the computer's turn.
        # The computer uses Minimax to decide
        # the best move to play.
        """
        It calls the minimax function if the depth < 9,
        else it choices a random coordinate.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """

        # Passes the method without returning anything if depth of board is 0,
        # or if either player wins
        if b.get_depth() == 0 or b.game_over():
            return

        # Clears the terminal
        clean()
        print(f'Computer turn [{c_choice}]')
        # Renders the board which has been passed in as a parameter
        b.render()

        # Prompting the computer to play a random move if the computer
        # is starting the game
        if b.get_depth() == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            # If the computer is not starting the game, it calls the minimax
            # algorithm which does an exhaustive back and forth play of the
            # current board to get the optimum move for the computer
            move = minimax(b.get_board(), b.get_depth(), COMP)
            # Setting the optimum move on the board by first assigning it
            # to an internal varable
            x, y = move[0], move[1]

        b.set_move(x, y, COMP)
        # Paul Lu.  Go full speed.
        # time.sleep(1)


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """

    # Initiates best with an invalid move, and the worst
    # possible score for the computer
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        # Initiates best with an invalid move, and the worst
        # possible score for the human player
        best = [-1, -1, +infinity]

    # Passes the method with a score returning anything if depth of board is 0,
    # or if either player wins
    if b.get_depth() == 0 or b.game_over():
        score = b.evaluate()
        return [-1, -1, score]

    # Calls the instance of the board, and invokes a method on it to get it's
    # empty cells
    for cell in b.empty_cells():
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    # Paul Lu.  Do not clear screen to keep output human readable.
    print()
    return

    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def main():
    global HUMAN
    HUMAN = -1
    global COMP
    COMP = 1

    # Paul Lu.  Set the seed to get deterministic behaviour for each run.
    # Makes it easier for testing and tracing for understanding.

    randomseed(274 + 2020)

    # Clears the terminal
    clean()
    # Initializes the choices
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    global b
    b = Board(h_choice, c_choice)
    global t
    t = Turn(b.get_board(), c_choice, h_choice)

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(b.empty_cells()) > 0 and not b.game_over():
        if first == 'N':
            t.ai_turn(c_choice, h_choice)
            first = ''

        t.human_turn(c_choice, h_choice)
        t.ai_turn(c_choice, h_choice)

    # Game over message
    if b.win_state(HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        b.render()
        print('YOU WIN!')
    elif b.win_state(COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        b.render()
        print('YOU LOSE!')
    else:
        clean()
        b.render()
        print('DRAW!')


if __name__ == '__main__':
    main()
