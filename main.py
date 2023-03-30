matrix = [1, 2, 3,
          4, 5, 6,
          7, 8, 9]

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def print_matrix():
    print(matrix[0], end=" ")
    print(matrix[1], end=" ")
    print(matrix[2])

    print(matrix[3], end=" ")
    print(matrix[4], end=" ")
    print(matrix[5])

    print(matrix[6], end=" ")
    print(matrix[7], end=" ")
    print(matrix[8])


player1 = True


def step_matrix(step, sym):
        global player1
        if step in matrix:
            ind = matrix.index(step)
            matrix[ind] = sym
        else:
            print("Ячейка занята")
            player1 = not(player1)


def check_res():
    winner = ""

    for i in victories:
        if matrix[i[0]] == "X" and matrix[i[1]] == "X" and matrix[i[2]] == "X":
            winner = "X"
        if matrix[i[0]] == "O" and matrix[i[1]] == "O" and matrix[i[2]] == "O":
            winner = "O"

    return winner


game_over = False


while game_over == False:

    print_matrix()

    if player1 == True:
        symbol = "X"
        step = int(input("Ход крестика: "))
    else:
        symbol = "O"
        step = int(input("Ход нолика: "))

    step_matrix(step, symbol)
    winner = check_res()
    if winner != "":
        game_over = True
    else:
        game_over = False

    player1 = not(player1)

print_matrix()
print("Победил", winner)