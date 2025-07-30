import random
from time import sleep


def print_board(board):
    print("-------------")
    # board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
    print("-------------")


def get_player_move(board):
    while True:
        move = input("Ingrese la fila y la columna (ej. 1,1): ")
        row, column = move.split(",")
        row = int(row) - 1
        column = int(column) - 1
        if 0 <= row < 3 and 0 <= column < 3 and board[row][column] == "-":
            return row, column
        else:
            print("Movimiento invalido. Intente de nuevo")


def check_winner(board):
    # validar lineas verticales
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return board[i][0]

    # validar lineas horizontales
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return board[0][i]

    # Validar las diagonales
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    elif board[2][0] == board[1][1] == board[0][2] != "-":
        return board[2][0]

    # Si no hay ganador retornar None
    return None


def main():
    print("Tres en Linea")
    # Inicializar el tablero
    # board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    board = [["-", "-", "-"] for _ in range(3)]
    # print(board)
    while True:
        # imprimir el tablero
        print_board(board)

        # Obtener el movimiento del jugador
        row, column = get_player_move(board)
        board[row][column] = "X"
        print_board(board)

        winner = check_winner(board)
        if winner is not None:
            break

        # Generar movimiento del computador
        computer_row = random.randint(0, 2)
        computer_column = random.randint(0, 2)
        while board[computer_row][computer_column] != "-":
            computer_row = random.randint(0, 2)
            computer_column = random.randint(0, 2)

        # Pintar la jugada del computador
        board[computer_row][computer_column] = "O"
        sleep(1)
        winner = check_winner(board)
        if winner is not None:
            break

    print_board(board)
    print(winner, "Gano!")


if __name__ == "__main__":
    main()
