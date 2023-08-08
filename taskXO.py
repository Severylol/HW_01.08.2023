import os
os.system('cls')
import random

def print_board(board):
    print("|", board[0][0], "|", board[0][1], "|", board[0][2], "|")
    print("|", board[1][0], "|", board[1][1], "|", board[1][2], "|")
    print("|", board[2][0], "|", board[2][1], "|", board[2][2], "|")

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells

def bot_move(board, bot_player, human_player):
    empty_cells = get_empty_cells(board)

    # Check if the bot can win in the next move
    for cell in empty_cells:
        board[cell[0]][cell[1]] = bot_player
        if check_winner(board, bot_player):
            return

        board[cell[0]][cell[1]] = ' '

    # Check if the bot needs to block the human from winning in the next move
    for cell in empty_cells:
        board[cell[0]][cell[1]] = human_player
        if check_winner(board, human_player):
            board[cell[0]][cell[1]] = bot_player
            return

        board[cell[0]][cell[1]] = ' '

    # If no winning moves, make a random move
    cell = random.choice(empty_cells)
    board[cell[0]][cell[1]] = bot_player

def human_move(board, human_player):
    while True:
        row = int(input("Введите номер строки (0, 1 или 2): "))
        col = int(input("Введите номер столбца (0, 1 или 2): "))

        if board[row][col] == ' ':
            board[row][col] = human_player
            break
        else:
            print("Клетка уже занята! Попробуйте другую.")

def main():
    board = initialize_board()

    human_player = 'X'
    bot_player = 'O'

    while True:
        print_board(board)
        human_move(board, human_player)
        
        if check_winner(board, human_player):
            print_board(board)
            print("Поздравляю! Вы победили!")
            break

        if is_draw(board):
            print_board(board)
            print("Ничья!")
            break

        bot_move(board, bot_player, human_player)

        if check_winner(board, bot_player):
            print_board(board)
            print("Компьютер победил!")
            break

        if is_draw(board):
            print_board(board)
            print("Ничья!")
            break

if __name__ == "__main__":
    main()
