# TIC-TAC-TOE game

import random

import numpy as np

ROWS = 3
COLUMNS = 3


grid = np.full((ROWS, COLUMNS), "", dtype=str)
print("GitHub practice branch test")


# function for sumbol selection
def players_symbol_selection():
    player_choice = input("Choose X or O: ").strip().lower()
    if player_choice == "x":
        player_choice = "X"
        second_player_choice = "O"
    else:
        player_choice = "O"
        second_player_choice = "X"

    return player_choice, second_player_choice


# function intializing the grid
def grid_lines(board):
    def show(v):
        return v if v != "" else " "

    print(f" {show(board[0][0])} | {show(board[0][1])} | {show(board[0][2])} ")
    print("-----------")
    print(f" {show(board[1][0])} | {show(board[1][1])} | {show(board[1][2])} ")
    print("-----------")
    print(f" {show(board[2][0])} | {show(board[2][1])} | {show(board[2][2])} ")


def first_play():
    return random.randint(1, 2)


def check_winner(board):
    # vertical check
    if (
        board[0][0] == board[1][0] == board[2][0]
        and board[0][0] != ""
        and board[1][0] != ""
        and board[2][0] != ""
    ):
        return True
    elif (
        board[0][1] == board[1][1] == board[2][1]
        and board[0][1] != ""
        and board[1][1] != ""
        and board[2][1] != ""
    ):
        return True
    elif (
        board[0][2] == board[1][2] == board[2][2]
        and board[0][2] != ""
        and board[1][2] != ""
        and board[2][2] != ""
    ):
        return True

    # horizontal check
    elif (
        board[0][0] == board[0][1] == board[0][2]
        and board[0][0] != ""
        and board[0][1] != ""
        and board[0][2] != ""
    ):
        return True
    elif (
        board[1][0] == board[1][1] == board[1][2]
        and board[1][0] != ""
        and board[1][1] != ""
        and board[1][2] != ""
    ):
        return True
    elif (
        board[2][0] == board[2][1] == board[2][2]
        and board[2][0] != ""
        and board[2][1] != ""
        and board[2][2] != ""
    ):
        return True

    # diagonal check
    elif (
        board[0][0] == board[1][1] == board[2][2]
        and board[0][0] != ""
        and board[1][1] != ""
        and board[2][2] != ""
    ):
        return True
    elif (
        board[2][0] == board[1][1] == board[0][2]
        and board[2][0] != ""
        and board[1][1] != ""
        and board[0][2] != ""
    ):
        return True

    else:
        return False


def check_deuce(board):
    if np.isin(board, ["X", "O"]).all():
        return True, "Deuce!"

    return False, ""


def check_player_turn(row, col):
    if row > 2 or col > 2:
        print("Out of bounds. Choose from 0-2.")
        return True
    elif grid[row][col] == "X" or grid[row][col] == "O":
        print("You can not choose this cell")
        return True

    return False


def players_move(player_symbol):
    row = int(input(("Choose Row Position: ")))
    col = int(input(("Choose Column Position: ")))
    while check_player_turn(row=row, col=col):
        row = int(input(("Choose Row Position: ")))
        col = int(input(("Choose Column Position: ")))

    grid[row][col] = player_symbol


def first_player_turn(first_player_symbol):
    print()
    print("Player 1 Turn.........")
    players_move(player_symbol=first_player_symbol)


def second_player_turn(second_player_symbol):
    print()
    print("Player 2 Turn.........")
    players_move(player_symbol=second_player_symbol)


def display_grid():
    print()
    print("Displaying The Grid..................")
    print()
    grid_lines(board=grid)


### MAIN GAME - TEST
print("Welcome to TIC-TAC-TOE Game")
display_grid()
print()
players_choice, second_player_choice = players_symbol_selection()
starter = first_play()
while True:
    if starter == 1:
        # here
        if check_deuce(board=grid)[0]:
            print("DEUCE!!!!!!")
            break
        first_player_turn(first_player_symbol=players_choice)
        if check_winner(board=grid):
            print("Player 1 Won! ")
            break
        display_grid()
        print()

        # here
        if check_deuce(board=grid)[0]:
            print("DEUCE!!!!!!")
            break
        second_player_turn(second_player_symbol=second_player_choice)

        if check_winner(board=grid):
            print("Player 2 Won! ")
            break

        display_grid()

    else:
        # here
        if check_deuce(board=grid)[0]:
            print("DEUCE!!!!!!")
            break
        second_player_turn(second_player_symbol=second_player_choice)
        if check_winner(board=grid):
            print("Player 2 Won! ")
            break
        display_grid()
        # here
        if check_deuce(board=grid)[0]:
            print("DEUCE!!!!!!")
            break
        first_player_turn(first_player_symbol=players_choice)
        if check_winner(board=grid):
            print("Player 1 Won! ")
            break
        display_grid()
        print()
